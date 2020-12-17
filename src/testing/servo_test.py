
import pi_servo_hat
import time
import sys


def runExample():

    print("\nSparkFun Pi Servo Hat Demo\n")
    mySensor = pi_servo_hat.PiServoHat()

#    if mySensor.isConnected() == False:
#        print("The Qwiic PCA9685 device isn't connected to the system. Please check your connection", sys.stderr)
#        return

    mySensor.restart()

    # Test Run
    #########################################
    # Moves servo position to 0 degrees (1ms), Channel 0
    mySensor.move_servo_position(1, 0)

    # Pause 1 sec
    time.sleep(1)


    mySensor.move_servo_position(1,54)

    # Moves servo position to 90 degrees (2ms), Channel 0
#    mySensor.move_servo_position(1, 20)
    h = 2
#    print("Servo 1 at position 0")
#    for i in range(-10,140,10):
#        print ("Servo " ,h, " at position ",i)
#        mySensor.move_servo_position(h, i)
#        time.sleep(3)

    #Forard is near 50, left is  0 and right is 130-ish
    print("Test in the forward position = 54")
    mySensor.move_servo_position(h, 54)
    time.sleep(2)
#    for i in range(52,56,1):
#        print ("Servo " ,h, " at position ",i)
#        mySensor.move_servo_position(h, i)
#        time.sleep(5)

    print("Test in the right position =130")
    mySensor.move_servo_position(h, 130)
    time.sleep(2)
#    for i in range(120,140,1):
#        print ("Servo " ,h, " at position ",i)
#        mySensor.move_servo_position(h, i)
#        time.sleep(3)

    print("Test in the left position=-21")
    mySensor.move_servo_position(h,-21)
#    for i in range(-30,10,1):
#        print("Servo " ,h, " at position ",i)
#        mySensor.move_servo_position(h, i)
#        time.sleep(3)



runExample()
