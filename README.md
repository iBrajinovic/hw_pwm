# About

This is a hardware PWM generator for the RPi(4 in my case). In my case, the software simulated PWM was not percise enough and I had to use the PWM chip inside the RPi to generate a real, reliable PWM signal. 

## Pinout

### OUTPUT/PWM pins

- GPIO 18 - PIN 12 - PWM channel 0
- GPIO 19 - PIN 35 - PWM channel 1

### INPUT pins

- GPIO 2 - PIN 3 - increase duty cycle
- GPIO 3 - PIN 5 - decrease duty cycle
- GPIO 4 - PIN 7 - channel select

# How to

Depending on the use case, you might need only the raw PWM signal but for me that is not the case. I need to be able to get 2 voltage ranges, 0 -> 5 V and 0 -> 12 V. Given that the PWM signal is just a 

# 