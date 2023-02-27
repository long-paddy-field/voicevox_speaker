#include "rogivoice.hpp"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

RogiVoice::RogiVoice(rclcpp::Node *node):node(node){
  voice_pub = node->create_publisher<std_msgs::msg::String>("voice", 10);
}

void RogiVoice::say(std::string voice_name){
  auto msg = std_msgs::msg::String();
  msg.data = voice_name;
  voice_pub->publish(msg);
}