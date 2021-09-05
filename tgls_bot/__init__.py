#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @lnc3f3r Jins Mathew Re-Create

import os
import logging
import time

from logging.handlers import RotatingFileHandler

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", "3607361"))

API_HASH = os.environ.get("API_HASH", "c57bcc4b09591db4f90f60b469e8870f")
    
try:
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "631110062").split())
except ValueError:
    raise Exception("Your OWNER_ID env variable is not a valid integer.")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1725624123:AAEk5bSDRZoWpECQf3CAgrjBPEB6esHmXx8")

CHAT_ID = os.environ.get("CHAT_ID", "@ufstest")

INPUT_SOURCE = os.environ.get("INPUT_SOURCE", "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
