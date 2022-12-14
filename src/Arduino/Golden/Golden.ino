/*
 * rosserial PubSub Example
 * Prints "hello world!" and toggles led
 */

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>
#include <HX711_ADC.h>
#include <std_msgs/Float32.h>
// #include <scale_msg/Float32.h>

ros::NodeHandle  nh;

std_msgs::Float32 scale_msg;
ros::Publisher chatter("/arduino/scalePour", &scale_msg);

//arduino pinout config---------------------------------------
const int HX711_dout = 5; //mcu > HX711 dout pin
const int HX711_sck = 4; //mcu > HX711 sck pin

//HX711 constructor:
HX711_ADC LoadCell(HX711_dout, HX711_sck);

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
  Serial.begin(57600); delay(10);
  Serial.println();
  Serial.println("Starting...");

  LoadCell.begin();

  float calibrationValue; // calibration value (see example file "Calibration.ino")
  calibrationValue = 400.0; // uncomment this if you want to set the calibration value in the sketch
// #if defined(ESP8266)|| defined(ESP32)
//   //EEPROM.begin(512); // uncomment this if you use ESP8266/ESP32 and want to fetch the calibration value from eeprom
// #endif
  //EEPROM.get(calVal_eepromAdress, calibrationValue); // uncomment this if you want to fetch the calibration value from eeprom

  unsigned long stabilizingtime = 2000; // preciscion right after power-up can be improved by adding a few seconds of stabilizing time
  boolean _tare = false; //set this to false if you don't want tare to be performed in the next step
  LoadCell.start(stabilizingtime, _tare);
  if (LoadCell.getTareTimeoutFlag()) {
    // Serial.println("Timeout, check MCU>HX711 wiring and pin designations");
    printf("Timeout, check MCU>HX711 wiring and pin designations");
    while (1);
  }
  else {
    LoadCell.setCalFactor(calibrationValue); // set calibration value (float)
  //   // Serial.println("Startup is complete");
    // printf("Startup is complete");
  }
}

void loop()
{
  boolean newDataReady = 0;

  // check for new data/start next conversion:
  if (LoadCell.update()) newDataReady = true;

  // get smoothed value from the dataset:
  if (newDataReady) {
    // if (millis() > t + serialPrintInterval) {
      // LoadCell.update();
      float i = LoadCell.getData();
      // float i = 1;
      Serial.print("Load cell output val: ");
      Serial.println(i);
      // newDataReady = 0;
      // t = millis();
      scale_msg.data = i;
      // return i;
    }
  // }

  chatter.publish( &scale_msg );
  nh.spinOnce();
  delay(1000);
}