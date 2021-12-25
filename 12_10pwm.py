'''Pin out based on the key'''
import RPi.GPIO as GPIO 
import pygame
import threading
import time

GPIO.setmode(GPIO.BOARD)    # Set Pi to use pin number when referencing GPIO pins
                            # GPIO.setmode(GPIO.BCM) lets you use broadcom channel names instead of numbers

GPIO.setup(12, GPIO.OUT)    #set GPIO pin 12 to output mode
GPIO.setup(10, GPIO.OUT)    #set GPIO pin 12 to output mode

pwm_12 = GPIO.PWM(12, 100)     # Initialize PWM on pwmPin 100Hz frequency
pwm_10 = GPIO.PWM(10, 100)     # Initialize PWM on pwmPin 100Hz frequency

dc = 0
pwm_12.start(dc)
pwm_10.start(dc)

pygame.display.init()
SCR = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def move():
    try:
        while True:

            for e in pygame.event.get():
                print("Ready....\n")

                if e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_w:
                        for dc in range(0, 101, 5):     # Loop 0 to 100 stepping dc by 5 each loop
                            pwm_12.ChangeDutyCycle(dc)
                            time.sleep(0.05)            # wait 0.05 seconds at current LED brightness
                            if e.type != pygame.KEYDOWN:
                                break

                    if e.key == pygame.K_s:
                        for dc in range(0, 101, 5):     # Loop 0 to 100 stepping dc by 5 each loop
                            pwm_10.ChangeDutyCycle(dc)
                            time.sleep(0.05)            # wait 0.05 seconds at current LED brightness
                            if e.type != pygame.KEYDOWN:
                                break

                else:
                    pwm_12.ChangeDutyCycle(0)
                    pwm_10.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        stop_run()
        return


def stop_run():
    pwm_12.stop()      # stop PWM
    pwm_10.stop()      # stop PWM
      

print("Starting....\n")
move()
print("Stopping")
GPIO.cleanup()  # Reset GPIO pins used.
