#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node("teleop")
    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
    while not rospy.is_shutdown():
        vel = Twist()
        direction = raw_input ("push_keyboard:,,,")
        #前に進む
        if "" in direction:
            vel.linear.x = +
        #後ろに進む
        if "" in direction:
            vel.linear.x = -
        #右に曲がる
        if "" in direction:
            vel.angular.z = +
        #左に曲がる
        if "" in direction:
            vel.angular.z = -

        pub.publish(vel)

if __name__ == '__main__':
    talker()

