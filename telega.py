#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys

token = "This_is_you_token"


class sending_message:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
    def send_message(self, chat_id,summary, text):   # here typography https://core.telegram.org/bots/api#formatting-options
        text = "*" + summary + "*" + "```" + text + "```" # you must to choose this typography in bot father
        params = {'chat_id': chat_id, 'text': text, "parse_mode" : "markdown"}
        method = 'sendMessage'
        requests.post(self.api_url + method, params)
try:
    to = sys.argv[1]
except:
    exit("ERROR: No to argument given")
try:
    subject = sys.argv[2]
except:
    exit("ERROR: No to argument given")
try:
    body = sys.argv[3]
except:
    exit("ERROR: No to argument given")


greet_bot = sending_message(token)
greet_bot.send_message(to,subject,body)
