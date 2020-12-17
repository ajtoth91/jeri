#!/usr/bin/env python

import rospy
from std_msgs.msg import Twist
import pi_servo_hat
import time
import sys


#instantiate the servo hat
myServoHat= pi_servo_hat.PiServoHat()
myServoHat.restart()

#move the servos
def camera_servo_cmd(data):
     #pan servo is in poisition 1
    mySensor.move_servo_position(1, data.angular.x * 130)

    #pan servo is in poisition 0
    mySensor.move_servo_position(0, data.angular.y * 130)

    #

#camera_cmd is the node that moves the camera servos after changing the position of the camera_orientation frame
def camera_cmd():
    rospy.init_node('camera_cmd', anonymous=True)
    sub = rospy.Subscriber('camera_orientation',Twist, camera_servo_cmd)
    rospy.spin()
