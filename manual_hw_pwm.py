# pinout

# PWM pins
# used to simulate the battery voltage and current inputs on the CCU(BMS)
#    GPIO 18 - PIN 12 - PWM channel 0
#    GPIO 19 - PIN 35 - PWM channel 1

# INPUT pins
#    GPIO 2 - PIN 3 - increase duty cycle
#    GPIO 3 - PIN 5 - decrease duty cycle
#    GPIO 4 - PIN 7 - select PWM channel for duty cycle manipulation


import time
import RPi.GPIO as GPIO
from rpi_hardware_pwm import HardwarePWM

def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	current_pwm = HardwarePWM(pwm_channel=0, hz=7000)
	voltage_pwm = HardwarePWM(pwm_channel=1, hz=7000)

	current_pwm.start(0)
	voltage_pwm.start(0)

	increase_value_pin = 3
	decrease_value_pin = 5
	choose_pwm_pin = 7

	GPIO.setup(increase_value_pin, GPIO.IN)
	GPIO.setup(decrease_value_pin, GPIO.IN)
	GPIO.setup(choose_pwm_pin, GPIO.IN)

	state = 0
	current_duty_cycle = 0
	voltage_duty_cycle = 0

	while True:
		print(f"Current duty cycle: {current_duty_cycle}")
		print(f"Voltage duty cycle: {voltage_duty_cycle}\n")


		if GPIO.input(choose_pwm_pin): # if the selector pin value is log 1, manipulate the PWM 0 -> current pwm
			print(f"fucking works")
			if GPIO.input(increase_value_pin) and state == 0: #if the increase duty cycle pin is pressed
				current_duty_cycle  = current_duty_cycle + 1 if current_duty_cycle < 100 else 0
				state = 1
				print(f"state high")

			elif (not GPIO.input(increase_value_pin)) and state == 1:
				state = 0
				print(f"state low")

			elif GPIO.input(decrease_value_pin) and state == 0:
				current_duty_cycle = current_duty_cycle - 1 if current_duty_cycle > 0 else 100
				state = 2
				print(f"fuck")

			elif not GPIO.input(decrease_value_pin) and state == 2:
				state = 0


		else: # if the selector pin value is log 0
			if GPIO.input(increase_value_pin) and state == 0:
				voltage_duty_cycle = voltage_duty_cycle + 1 if voltage_duty_cycle <= 100 else 0
				state = 1

			elif (not GPIO.input(increase_value_pin)) and state == 1:
				state = 0

			elif GPIO.input(decrease_value_pin) and state == 0:
				voltage_duty_cycle = voltage_duty_cycle - 1 if voltage_duty_cycle > 1 else 100
				state = 2

			elif not GPIO.input(decrease_value_pin) and state == 2:
				state = 0


		current_pwm.change_duty_cycle(current_duty_cycle)
		voltage_pwm.change_duty_cycle(voltage_duty_cycle)
		time.sleep(0.1)




if __name__ == "__main__":
	main()
