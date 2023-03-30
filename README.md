# FlowBot-Robotic-Mixer

Check out our website for a more in depth description of this Project!
Link to website: https://tinyurl.com/flowbot-automation

*Note - most commits are pushed on Eric Berndt's account because we all worked on his account at the computer lab to access the Sawyer Robots

Goals of this Project:
Design a robot control system with the ability to mix two arbitrary ingredients of desired quantity into a product cup.

Motivation:
Everyday people consume water, coffee, tea, milk, etc. to maintain a healthy being.  Pouring liquid is something people learn intuitively 
but is tricky enough that even a grown adult spills from time to time.  Beyond the food industry, transferring liquid has many other general 
applications such as pharmaceuticals, lab work, manufacturing, etc.  In most of these cases, precision is of importance.  People don’t want 
too much milk in their coffee and a lab technician would be especially cautious mixing two chemicals.  

The benefits of automating of these applications would amount to:
- Lower operating costs
- Increase production output
- Increase efficiency
- Improve worker safety
- Improve consistency in quality of product

Engineering Challenges:
- Finding a method of picking up a cup with gripper
- How to find a position in dexterous workspace and then move end effector to that position
- Ensure the cup carried would not spill
- Incorporate precision measurement in the amount poured

The engineering complexity of this problem was a fascinating project.  It composed of five main components:
- Computer Vision
- Scale Module
- Gripper Design
- Path Planning
- Control and Actuation
