#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:32:26 2022

@author: ref-f1
"""

import rospy
import tf
import tf.msg
import geometry_msgs.msg
from sensor_msgs.msg import NavSatFix, NavSatStatus, Imu

def callback(Imu): 
    t = tf.TransformBroadcaster()
    t.sendTransform((0,0,0), (Imu.orientation.x,Imu.orientation.y,-Imu.orientation.z,Imu.orientation.w), rospy.Time.now(), "adma", "world")
#    t.header.frame_id = "world"
#    t.header.stamp = rospy.Time.now()
#    t.child_frame_id = "adma"
#    t.transform.translation.x = 0.0
#    t.transform.translation.y = 0.0
#    t.transform.translation.z = 0.0
#
#    print(Imu)
#    print("hi")
#    t.transform.rotation.x = Imu.orientation.x
#    t.transform.rotation.y = Imu.orientation.y
#    t.transform.rotation.z = Imu.orientation.z
#    t.transform.rotation.w = Imu.orientation.w
#
#    tfm = tf.msg.tfMessage([t])
#    pub_tf.publish(tfm)
    

if __name__ == '__main__':
    rospy.init_node('adma_frame_transformer')
    rospy.Subscriber("imu/imu_data",Imu, callback, queue_size=10)
    rospy.spin()
