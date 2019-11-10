#!/usr/bin/env python

__author__ =  'Shreyasi Pal'
__version__=  '1.0'

from __future__ import print_function
import roslib
import sys 
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

class ugan_image_subscriber:
	def __init__(self):
		rospy.Subscriber("ugan_image_topic", Image, self.image_callback, queue_size=1)
		self.bridge = CvBridge()

	def image_callback(self,msg):
		try:
			# Convert your ROS Image message to OpenCV2
			cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
			cv2.imwrite('camera_image.jpeg', cv2_img)
	    	except CvBridgeError as e:
			print(e)
	    #else:
		# Save your OpenCV2 image as a jpeg 
		#cv2.imwrite('camera_image.jpeg', cv2_img)

def main(args):
	ugan_sub=ugan_image_subscriber()
	rospy.init_node('image_subscriber', anonymous=True)
	
	try:
		# Spin until ctrl + c
		rospy.spin()
	except KeyboardInterrupt:
		print("ROS UGAN Image SUbscriber shutting down")

if __name__ == '__main__':
	main(sys.argv)
