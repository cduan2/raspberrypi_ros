#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', data.data)
    x = data.data
    pub.publish(x+1)

def talker():
    global pub 
    pub = rospy.Publisher('chatter1', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.Subscriber('chatter2', Float32, callback)
    rate = rospy.Rate(1) # 1hz
    rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
