#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class RogiVoice {
 public:
  RogiVoice(rclcpp::Node *node);
  void say(std::string voice_name);

 private:
  rclcpp::Node *node;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr voice_pub;
};