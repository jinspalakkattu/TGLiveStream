#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @lnc3f3r Jins Mathew Re-Create

import asyncio
from main import main
from .bot import Bot

app = Bot()
asyncio.get_event_loop().run_until_complete(main(app))
# app.run()
