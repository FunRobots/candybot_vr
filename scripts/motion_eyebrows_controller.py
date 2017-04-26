#!/usr/bin/env python3

import rospy
from coffebot.motion.eyebrows.eyebrows_controller import Eyebrows
from coffebot.msg import EyebrowsMotion, EyebrowsState
from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':
    rospy.init_node('motion_eyebrows_controller')

    eyebrows = Eyebrows()
    eyebrows_motion_lock = Lock()
    rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, eyebrows_motion_lock.callback)
    eyebrows_state_publisher = rospy.Publisher('/motion_eyebrows_controller/eyebrows_state', EyebrowsState, queue_size=1)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        eyebrows_msg = eyebrows_motion_lock.message
        if isinstance(yebrows_msg, EyebrowsMotion):
            eyebrows.set_left_servo_position(angle=eyebrows_msg.l_angle)
            eyebrows.set_right_servo_position(angle=eyebrows_msg.r_angle)
            eyebrows.set_emotion(emotion=eyebrows_msg.emotion)

            eyebrows_state_msg = EyesState()
            eyebrows_state_msg.l_angle, eyebrows_state_msg.r_angle = eyebrows.get_eyebrows_position()
            eyebrows_state_publisher.publish(eyebrows_state_msg)
            
        if eyebrows_motion_lock.message == eyebrows_msg:
            eyebrows_motion_lock.message = None

        time.sleep(0.5)
