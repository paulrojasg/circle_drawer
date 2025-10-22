#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist

def draw_circles():
    rospy.init_node('turtlebot3_circles', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    clockwise_circle = Twist()
    clockwise_circle.linear.x = 0.8
    clockwise_circle.angular.z = -0.4

    while not rospy.is_shutdown():
        pub.publish(clockwise_circle)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        draw_circles()
    except rospy.ROSInterruptException:
        pass
