import RPi.GPIO as GPIO     # import the GPIO library
import time                 # import time

GPIO.setmode(GPIO.BOARD)    # Set Pi to use pin number when referencing GPIO pins
                            # GPIO.setmode(GPIO.BCM) lets you use broadcom cahnnel names instead of numbers

GPIO.setup(10, GPIO.OUT)    #set GPIO pin 12 to output mode
pwm = GPIO.PWM(10, 100)     # Initialize PWM on pwmPin 100Hz frequency

#   Main loop
print("\n   Press Ctrl C to quit\n")
dc = 0          # Set duty cycle to 0 for 0%
pwm.start(dc)   # start with the 0% duty cyle

try:
    while True:                         # Loop until cancelled
        for dc in range(0, 101, 5):     # Loop 0 to 100 stepping dc by 5 each loop
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)            # wait 0.05 seconds at current LED brightness
            print(dc)

        for dc in range(95, 0, -5):     # Loop 95 to 5 stepping dc down by 5 each Loop
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
            print(dc)

except KeyboardInterrupt:
    print("Ctrl C pressed - Ending program")

pwm.stop()      # stop PWM
GPIO.cleanup()  # Reset GPIO pins used.
