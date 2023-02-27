import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class voicepy:
    def __init__(self,node_handle):
        self.voice_pub = node_handle.create_publisher(String, 'voice', 10)
    def say(self, text):
        msg = String()
        msg.data = text
        self.voice_pub.publish(msg)
        