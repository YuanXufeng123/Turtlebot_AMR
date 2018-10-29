#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from kobuki_msgs.msg import BumperEvent
from math import radians

bumper_state = 0
bumper_bumper = 0

def bumperCallback(data):
    rospy.loginfo("bumper = %u", data.bumper)
    rospy.loginfo("bumper state = %d ", data.state)
    global bumper_state
    bumper_state = data.state
    bumper_bumper = data.bumper
    
def main():
    vel_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1)
    rospy.init_node('turtlebot_turn', anonymous=True)
    rospy.Subscriber("/mobile_base/events/bumper", BumperEvent,bumperCallback)
    rate = rospy.Rate(10)
    global bumper_state
    #vel = Twist()
    #vel.angular.z = 1
    #count = 0
    vel = Twist()
    vel.linear.x = 0.1
    count=0
    
    while not rospy.is_shutdown():
        vel_pub.publish(vel)
        rate.sleep()
	if (bumper_state==1):
	    rospy.loginfo("bumper!!")
	    vel.linear.x=0
            for count in range (20):
	    	vel.angular.z= 0.5
		vel_pub.publish(vel)
        	rate.sleep()
		
	    vel.angular.z = 0
	    vel.linear.x=0.1


if __name__ == "__main__":
    main()

