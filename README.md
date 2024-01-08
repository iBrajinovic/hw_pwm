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

Connect PIN 3 and 5 to a button that has a pull down resistor connected to the input so that the inputs are activated by a logical HIGH (on release of the button because the GPIO 18 and 19 have an internal pull up ressistor).By default you will have a resolution of **1** and will manipulate the `GPIO 18 | PWM channel 0`. 

## 0.1 Resolution

To use the **0.1** resolultion you need to press and hold the opposite button(if you want to increase the value, press and hold the decrease button) and use the other button as you would usually and you will see the resolution is now 0.1.











