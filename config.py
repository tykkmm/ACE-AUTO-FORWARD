#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To")
    # The Telegram API things
    API_ID = int(os.environ.get("29426486"))
    API_HASH = os.environ.get("d71ad4ec048ab41677a1a439b21ff0c9")
    AUTH_USERS = os.environ.get("5976437467")

