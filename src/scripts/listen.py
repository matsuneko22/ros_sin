#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(data.data)

def main():
    rospy.init_node('plot_graph', anonymous=True)
    rospy.Subscriber("publisher", Float64, callback)

    rospy.spin();
    

if __name__=="__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

