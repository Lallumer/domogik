#!/usr/bin/python
# -*- coding: utf-8 -*-                                                                           

import zmq
from domogik.mq.pubsub.subscriber import MQAsyncSub
from zmq.eventloop.ioloop import IOLoop
from domogik.mq.message import MQMessage

class Test(MQAsyncSub):

    def __init__(self):
        MQAsyncSub.__init__(self, zmq.Context(), 'test', ['package.detail'])
        IOLoop.instance().start()

    def on_message(self, msgid, content):
        print(u"New pub message {0}".format(msgid))
        print(u"{0}".format(content))

if __name__ == "__main__":
    Test()
