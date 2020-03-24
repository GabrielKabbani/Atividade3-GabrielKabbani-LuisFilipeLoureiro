#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3

v = 10  # Velocidade linear
w = 5  # Velocidade angularen
x=0
vel_frente=Twist(Vector3(0.2,0,0), Vector3(0,0,0))
vel_stop=Twist(Vector3(0,0,0), Vector3(0,0,0))
vel_curva=Twist(Vector3(0.2,0,0), Vector3(0,0,np.pi/6))



if __name__ == "__main__":
    rospy.init_node("roda_exemplo")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():
            if x<20:
                pub.publish(vel_frente)
                rospy.sleep(5.0)
                pub.publish(vel_stop)
                rospy.sleep(0.5)
                pub.publish(vel_curva)
                rospy.sleep(3.0)
                pub.publish(vel_stop)
                x+=1
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")

