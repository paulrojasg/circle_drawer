#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
import requests

def velocity_callback(msg, token):
    # Check if the robot is moving forward while rotating
    linear_velocity = msg.linear.x
    angular_velocity = msg.angular.z

    # For simple circle motion, linear velocity should be constant, and angular velocity should also be constant
    if abs(linear_velocity - 0.8) < 0.05 and abs(angular_velocity + 0.4) < 0.05:  # Adjust based on your values
        rospy.loginfo("The robot is moving in a circle.")
        res = requests.put('http://192.168.0.160/competencies/control-panel/activity-attempt/update/', json= {
            "token":{"PIN":token},
            "evaluaciones": [
                {
                    "index":1,
                    "name": "Robot is making a circle",
                    "percentage_grade": 100
                },
                {
                    "index":2,
                    "name": "Total",
                    "percentage_grade": 100
                },
            ]
        })
        print("Status Code:", res.status_code)

        print("Response Body:", res.json())
        rospy.signal_shutdown("Circle detected, stopping monitor.")
    else:
        rospy.loginfo("The robot is not moving in a circle.")

def circle_monitor():
    # Initialize the ROS node
    token = input("Ingresa token: ")
    rospy.init_node('turtlebot3_test', anonymous=True)
    
    # Subscribe to the cmd_vel topic
    rospy.Subscriber('/cmd_vel', Twist, callback=velocity_callback, callback_args=(token))
    
    rospy.loginfo("Monitoring velocity to detect circular motion...")
    rospy.spin()

if __name__ == '__main__':
    try:
        circle_monitor()
    except rospy.ROSInterruptException:
        pass
