#!/usr/bin/env python3

import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')

import rospy
from std_msgs.msg import Bool
import smach

from candybot_v2.msg import BotSpeechText, MotionPattern, Emotion, UserSpeechText
import time
import actionlib
from candybot_v2.msg import MakePhotoAction, MakePhotoGoal, MakePhotoCommand


class BotAnswerState(smach.State):
    '''
    Bot text existance state
    '''

    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'outcome2'],
                                   input_keys=['bot_text_answer', 'bot_action_answer']
                            )
        self.speech_synthesis_publisher = self.speech_synthesis_publisher = rospy.Publisher('/core_decision_manager/bot_speech_text', BotSpeechText, queue_size=1)
        self.pattern_publisher = rospy.Publisher('/core_decision_manager/pattern', MotionPattern, queue_size=1)

    def execute(self, userdata):
        if isinstance(userdata.bot_text_answer, str) and isinstance(userdata.bot_action_answer, str):
            len_text = len(userdata.bot_text_answer)
            len_action = len(userdata.bot_action_answer)

            if len_text == 0 and len_action == 0:
                return 'outcome2'
            else:
                if len_text > 0:
                    print('\n\n\nDECISON!: ', userdata.bot_text_answer)
                    bot_speech_text_msg = BotSpeechText(text=userdata.bot_text_answer)
                    self.speech_synthesis_publisher.publish(bot_speech_text_msg)
                if len_action > 0:
                    print('bot_action_answer', userdata.bot_action_answer)
                    pattern_msg = MotionPattern()
                    if userdata.bot_action_answer == 'action.hello':
                        pattern_msg.name = 'sayHello'
                    elif userdata.bot_action_answer == 'action.hello.doIntroduction':
                        pattern_msg.name = 'dointroduction'
                    elif userdata.bot_action_answer == 'action.service.coffeOrder':
                        pattern_msg.name = 'coffeOrder'
                    elif userdata.bot_action_answer == 'action.service.promo.feedback':
                        pattern_msg.name = 'feedback'
                    elif userdata.bot_action_answer == 'action.service.goodbye':
                        pattern_msg.name = 'goodbye'
                    elif userdata.bot_action_answer == 'action.makephoto':
                        make_photo_action_client = actionlib.SimpleActionClient('make_photo', MakePhotoAction)
                        make_photo_command = MakePhotoCommand(make_photo=True, photo_file_name=time.ctime() + '.png')
                        goal = MakePhotoGoal(make_photo_command=make_photo_command)
                        make_photo_action_client.wait_for_server(rospy.Duration(3))
                        make_photo_action_client.send_goal(goal)
                        make_photo_action_client.wait_for_result(rospy.Duration(5))

                    elif userdata.bot_action_answer == 'action.givecandy':
                        vk_scan_command_publisher = rospy.Publisher('/social/vk/newsfeed_scanner/scan_command', Bool, queue_size=1)
                        twitter_scan_command_publisher = rospy.Publisher('/social/twitter/code_scanner/scan_command', Bool, queue_size=1)

                        vk_scan_command_publisher.publish(True)
                        twitter_scan_command_publisher.publish(True)

                    if len(pattern_msg.name) > 0:
                        self.pattern_publisher.publish(pattern_msg)

                return 'outcome1'

        return 'outcome2'


class SmileExistsState(smach.State):
    '''
    User smile existance state
    '''
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'],
                                   input_keys=['smile_exists']
                            )
        self.emotion_publisher = rospy.Publisher('/core_decision_manager/emotion', Emotion, queue_size=1)
        self.dialog_bot_publisher = rospy.Publisher('/speech_recognition/user_speech_text', UserSpeechText, queue_size=1)

    def execute(self, userdata):
        if userdata.smile_exists is True:
            #set happy emotion as reaction on human smile
            emotion_msg = Emotion(name='happy')
            self.emotion_publisher.publish(emotion_msg)

            user_speech_text_msg = UserSpeechText(text='привет')
            self.dialog_bot_publisher.publish(user_speech_text_msg)

        return 'outcome1'
