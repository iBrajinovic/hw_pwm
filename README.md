# About

This is a hardware PWM generator for the RPi(4 in my case). In my case, the software simulated PWM was not percise enough and I had to use the PWM chip inside the RPi to generate a real, reliable PWM signal. It has the ability to increment by 1 or by 0.1.

# Requirements

Before working with the hardware pwm, you need to edit the config.txt file that is located on the SD card of the RPi. I didn't have success in editing it live so I had to edit it by inserting the card in my laptop. Once you locate and open the config.txt file, insert this line of code `dtoverlay=pwm-2chan`. For more info, visit [this website](https://pypi.org/project/rpi-hardware-pwm/).

## Pinout

### OUTPUT/PWM pins

- GPIO 18 - PIN 12 - PWM channel 0
- GPIO 19 - PIN 35 - PWM channel 1

### INPUT pins

- GPIO 2 - PIN 3 - increase duty cycle
- GPIO 3 - PIN 5 - decrease duty cycle
- GPIO 4 - PIN 7 - channel select

# Usage

## Connecting the buttons

Connect PIN 3 and PIN 5 to a button connected to a pull down resistor. By default you will have a resolution of **1** and will manipulate the *GPIO 18 | PWM channel 0*. If you don't have buttons you can use wires connected to the input pins and then connect them to ground or 3.3V to simulate the button press/release. 

## 0.1 Resolution

To use the **0.1** resolultion you need to press and hold the opposite button(if you want to increase the value, press and hold the decrease button) and use the button as you would usually and you will see the resolution is now 0.1.

## Changing PWM channels

To change the PWM channel you are manipulating, toggle the switch connected to the GPIO 4 | PIN 7. I don't have a switch, I use a regular wire and move it from GND to 3.3V.











