import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from playsound import playsound

import yaml


class VoicevoxSpeaker(Node):
    def __init__(self, voice_dict):
        super().__init__('voicevox_speaker')

        self.voice_dict = voice_dict  # 音声ファイルの名前とパスを格納する辞書
        self.setlist = list()  # 再生する音声ファイルを保存するキュー

        self.subscription = self.create_subscription(
            String,
            'voice',
            self.listener_callback,
            10)  # サブスクライバ
        self.subscription
        self.update()

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.setlist.append(msg.data)

    def update(self):
        while rclpy.ok():
            if len(self.setlist) > 0:
                playsound(self.voice_dict[self.setlist[0]])
                self.setlist.pop(0)
            rclpy.spin_once(self, timeout_sec=0.1)
            
def main(args=None):
    voice_dict = dict()  # 音声ファイルの名前とパスを格納する辞書
    with open("voice_lib/voicevox_speaker/config/catch2023_voice.yaml") as file:
        config = yaml.safe_load(file)  # yamlファイルを読み込む
        for i in range(len(config["voice"])):
            if "file" not in config["voice"][i]:
                voice_dict[config["voice"][i]["name"]] = config["default_path"] + config["voice"][i]["name"] + ".wav"
            else:
                voice_dict[config["voice"][i]["name"]] = config["default_path"] + config["voice"][i]["file"]
        print(voice_dict)
    rclpy.init(args=args)
    node = VoicevoxSpeaker(voice_dict=voice_dict)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
