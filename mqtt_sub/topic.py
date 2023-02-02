#!/usr/bin/env python3
import rospy
from mqtt_bridge.msg import msgMqttSub
from std_msgs.msg import  String

rospy.init_node('topic')
ros_pub = rospy.Publisher('/mqtt_sub' , msgMqttSub , queue_size=10)
msg_mqtt_sub = msgMqttSub()
rate = rospy.Rate()
while not rospy.is_shutdown():
    ros_pub.publish(msg_mqtt_sub)
    rate.sleep()


