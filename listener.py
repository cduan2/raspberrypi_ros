#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter1', Float32, callback)
    pub = rospy.Publisher('chatter2', Float32, queue_size=10)
    rate = rospy.Rate(1)
    my_data = 3.14 % rospy.get_time()
    while not rospy.is_shutdown():
	pub.publish(my_data)
	my_data = my_data+1
	if my_data>15:
		my_data = 3.14
	rate.sleep()
	


    rospy.spin()

if __name__ == '__main__':
	try:
    		listener()
	except rospy.ROSInterruptException:
        	pass
