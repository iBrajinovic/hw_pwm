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

Depending on the use case, you might need only the raw PWM signal. If you use the PWM to manage the brighness of a LED, your eyes do the signal avereging because they are unable to see the LED going off and on and hence you see the light as brighter or darker. Also, if you have an input that you are delivering the PWM signal to, the reading speed of the signal might be slow enough so that you don't need an evener(the input would be the eyes in the previous example).

But for me that is not the case. I need to be able to get 2 voltage ranges, 0 -> 5 V and 0 -> 12 V. Given that the RPi gives out 3.3V on the outputs I have to use some additional components (NPN Transistor in my case) to manipulate the higher supply voltage and I also need to even out the PWM signal I would get from the transistor so I am using a Low-Pass filter(capacitor shorted to ground).

# 