#!/usr/bin/env python3

'''
face recognition node
'''

import rospy
from coffebot.msg import FaceFeatures
import ros_numpy
from sensor_msgs.msg import Image

from coffebot.vision.utils import image_format_converter
from coffebot.vision import face_recognition

import time

from coffebot.topic_controller import Lock


if __name__ == '__main__':

    rospy.init_node('vision_face_recognition')

    if rospy.has_param('algorithmia_api_key'):
        face_recognition.set_algorithmia_key(key=rospy.get_param('algorithmia_api_key'))
        face_info_publisher = rospy.Publisher('/vision_face_recognition/face_info', FaceFeatures, queue_size=1)

        lock_recognize = Lock()
        rospy.Subscriber('/vision_face_tracking/face_image', Image, lock_recognize.callback)
        print('vision face recognition start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            face_image_msg = lock_recognize.message
            if isinstance(face_image_msg, Image):
                face_image = ros_numpy.numpify(face_image_msg)
                print(type(face_image))
                if face_image is not None:

                    #search other features: emotions, celebrities similarity, gender, age
                    binary_face_image = image_format_converter.ndarray2format(face_image)
                    face_features_msg = FaceFeatures()
                    face_features_msg.emotion = face_recognition.recognize_emotion(binary_face_image)
                    face_features_msg.celebrity_name = face_recognition.recognize_celebrities_similarity(binary_face_image)
                    face_features_msg.gender = face_recognition.recognize_gender(binary_face_image)
                    age_interval = face_recognition.recognize_age(binary_face_image)
                    if age_interval is not None:
                        face_features_msg.min_age, face_features_msg.max_age = age_interval

                    print(face_features_msg)
                    face_info_publisher.publish(face_features_msg)

            if lock_recognize.message == face_image_msg:
                lock_recognize.message = None
            time.sleep(0.5)
