# -*- coding: utf-8 -*-

import sys
import os
from aiohttp.web import run_app
from pathlib import Path

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

# ---------------------------------------------------------

import asyncio
import uvloop

from server import app_factory

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    run_app(app_factory(), host='0.0.0.0', port=5000)
