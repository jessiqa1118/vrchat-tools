# -*- coding: utf-8 -*-
import sys
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder


def main():
    # 受信先のVRChat
    IP = '127.0.0.1'
    PORT = 9000

    # OSCメッセージ情報の読み込み
    address = sys.argv[1]
    arg = sys.argv[2]

    print('Address: '+address)
    print('Arg: '+arg)

    # OSCメッセージの構築
    client = udp_client.UDPClient(IP, PORT)
    msg = OscMessageBuilder(address=address)
    msg.add_arg(arg)
    m = msg.build()

    # OSCメッセージの送信
    client.send(m)


if __name__ == '__main__':
    main()
