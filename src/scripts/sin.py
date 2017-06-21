#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import numpy as np

def main():
    pub = rospy.Publisher('publisher', Float64, queue_size=10)
    rospy.init_node('sin', anonymous=True)
    r = rospy.Rate(10)
    angle = 0.0
    while not rospy.is_shutdown():
        rad = np.radians(angle)
        sin = np.sin(rad)
        rospy.loginfo(sin)
        pub.publish(sin)
        angle += 1
        r.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
