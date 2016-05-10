#!/usr/bin/env python

"""
Purpose: Read messages from the broker, write to IRC
Requirements: pynsq, and nsq.io instance configured as an openknot broker
"""

__author__ = "Duncan Hutty"
__email__ = "dhutty@allgoodbits.org"

import json
import nsq

def pub_to_irc(irc, message):
    pass

def handler(message):
    print type(message.body)
    print json.dumps(message.body)
    return True

r = nsq.Reader(message_handler=handler,
            lookupd_http_addresses=['http://127.0.0.1:4161'],
            topic='test', channel='tail450747#ephemeral', lookupd_poll_interval=15)
nsq.run()
