#!/usr/bin/env python

"""
Purpose: Send test messages to a broker
Requirements: pynsq, and nsq.io instance configured as an openknot broker
"""

__author__ = "Duncan Hutty"
__email__ = "dhutty@allgoodbits.org"

import datetime
import json
import nsq
import tornado.ioloop
import uuid

def pub_message():
    msg = {"protocol": 'irc', 'source': 'dotplus@allgoodbits.org', 'content': 'the body of the message'}
    msg['id'] = "%s" % (uuid.uuid4(),)
    msg['timestamp'] = datetime.datetime.now().isoformat()
    writer.pub('test', json.dumps(msg), finish_pub)

def finish_pub(conn, data):
    print data

writer = nsq.Writer(['127.0.0.1:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 500).start()
nsq.run()
