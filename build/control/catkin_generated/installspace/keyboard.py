#!/usr/bin/env python3

import pygame
import sys
import rospy
from std_msgs.msg import Int32

# Initialize the ROS node
rospy.init_node('key_publisher')

# Create a publisher, publishing to the 'key_press' topic
pub = rospy.Publisher('key_press', Int32, queue_size=10)

pygame.init()

while not rospy.is_shutdown():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            rospy.signal_shutdown('Quit')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pub.publish(1)
            elif event.key == pygame.K_DOWN:
                pub.publish(2)
            elif event.key == pygame.K_LEFT:
                pub.publish(3)
            elif event.key == pygame.K_RIGHT:
                pub.publish(4)
        elif event.type == pygame.KEYUP:
            pub.publish(0)
