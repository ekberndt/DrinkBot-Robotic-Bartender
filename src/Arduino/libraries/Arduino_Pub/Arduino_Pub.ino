
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>
#include <HX711_ADC.h>
#include <std_msgs/Float32.h>
// #include <scale_msg/Float32.h>

#if defined(ESP8266)|| defined(ESP32) || defined(AVR)
#include <EEPROM.h>
#endif


//create the ros node nh. The node will be used to publish to Arduino
ros::NodeHandle node_handle;

//Define msg and local var for message
// float mass;
std_msgs::Float32 scale_msg;

//Define Publisher
ros::Publisher scale_publisher("/arduino/scalePour", &scale_msg);

//pins:
const int HX711_dout = 4; //mcu > HX711 dout pin
const int HX711_sck = 5; //mcu > HX711 sck pin

//HX711 constructor:
HX711_ADC LoadCell(HX711_dout, HX711_sck);

const int calVal_eepromAdress = 0;
unsigned long t = 0;

// float scale_func(){
//   //pins:
//   const int HX711_dout = 5; //mcu > HX711 dout pin
//   const int HX711_sck = 4; //mcu > HX711 sck pin

//   //HX711 constructor:
//   HX711_ADC LoadCell(HX711_dout, HX711_sck);

//   const int calVal_eepromAdress = 0;
//   unsigned long t = 0;

// // void setup() {


//   LoadCell.begin();
//   //LoadCell.setReverseOutput(); //uncomment to turn a negative output value to positive
//   float calibrationValue; // calibration value (see example file "Calibration.ino")
//   calibrationValue = 696.0; // uncomment this if you want to set the calibration value in the sketch
// #if defined(ESP8266)|| defined(ESP32)
//   //EEPROM.begin(512); // uncomment this if you use ESP8266/ESP32 and want to fetch the calibration value from eeprom
// #endif
//   //EEPROM.get(calVal_eepromAdress, calibrationValue); // uncomment this if you want to fetch the calibration value from eeprom

//   unsigned long stabilizingtime = 2000; // preciscion right after power-up can be improved by adding a few seconds of stabilizing time
//   boolean _tare = true; //set this to false if you don't want tare to be performed in the next step
//   LoadCell.start(stabilizingtime, _tare);
//   if (LoadCell.getTareTimeoutFlag()) {
//     Serial.println("Timeout, check MCU>HX711 wiring and pin designations");
//     while (1);
//   }
//   else {
//     LoadCell.setCalFactor(calibrationValue); // set calibration value (float)
//     Serial.println("Startup is complete");
//   }
// // }
//   //Loop for scale read
//   for (;true;){
//   static boolean newDataReady = 0;
//   const int serialPrintInterval = 0; //increase value to slow down serial print activity

//   // check for new data/start next conversion:
//   if (LoadCell.update()) newDataReady = true;

//   // get smoothed value from the dataset:
//   if (newDataReady) {
//     if (millis() > t + serialPrintInterval) {
//       float i = LoadCell.getData();
//       Serial.print("Load cell output val: ");
//       Serial.println(i);
//       newDataReady = 0;
//       t = millis();
//       return i;
//     }
//   }

//   // receive command from serial terminal, send 't' to initiate tare operation:
//   if (Serial.available() > 0) {
//     char inByte = Serial.read();
//     if (inByte == 't') LoadCell.tareNoDelay();
//   }

//   // check if last tare operation is complete:
//   if (LoadCell.getTareStatus() == true) {
//     Serial.println("Tare complete");
//   }

// }
// }

void setup()
{
  //Scale Readout Code
  node_handle.initNode();
  node_handle.advertise(scale_publisher);
  Serial.begin(57600); delay(10);
  Serial.println();
  Serial.println("Starting...");

  LoadCell.begin();
  //LoadCell.setReverseOutput(); //uncomment to turn a negative output value to positive
  float calibrationValue; // calibration value (see example file "Calibration.ino")
  calibrationValue = 400.0; // uncomment this if you want to set the calibration value in the sketch
#if defined(ESP8266)|| defined(ESP32)
  //EEPROM.begin(512); // uncomment this if you use ESP8266/ESP32 and want to fetch the calibration value from eeprom
#endif
  //EEPROM.get(calVal_eepromAdress, calibrationValue); // uncomment this if you want to fetch the calibration value from eeprom

  unsigned long stabilizingtime = 2000; // preciscion right after power-up can be improved by adding a few seconds of stabilizing time
  boolean _tare = true; //set this to false if you don't want tare to be performed in the next step
  LoadCell.start(stabilizingtime, _tare);
  if (LoadCell.getTareTimeoutFlag()) {
    Serial.println("Timeout, check MCU>HX711 wiring and pin designations");
    while (1);
  }
  else {
    LoadCell.setCalFactor(calibrationValue); // set calibration value (float)
    Serial.println("Startup is complete");
  }
}


void loop()
{ 
  static boolean newDataReady = 0;
  const int serialPrintInterval = 0; //increase value to slow down serial print activity

  // check for new data/start next conversion:
  if (LoadCell.update()) newDataReady = true;

  // get smoothed value from the dataset:
  if (newDataReady) {
    // if (millis() > t + serialPrintInterval) {
      float i = LoadCell.getData();
      Serial.print("Load_cell output val: ");
      Serial.println(i);
      // newDataReady = 0;
      // t = millis();
      scale_msg.data = i;
      scale_publisher.publish(&scale_msg);
    }
  // }

  // receive command from serial terminal, send 't' to initiate tare operation:
  // if (Serial.available() > 0) {
  //   char inByte = Serial.read();
  //   if (inByte == 't') LoadCell.tareNoDelay();
  // }

  // // check if last tare operation is complete:
  // if (LoadCell.getTareStatus() == true) {
  //   Serial.println("Tare complete");
  // }

  node_handle.spinOnce();
  
  // delay(5);
}