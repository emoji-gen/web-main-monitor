# -*- coding: utf-8 -*-

import sys
import os
from aiohttp.web import run_app
from pathlib import Path

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

# ---------------------------------------------------------

from time import sleep

from inspector import Inspector
from notifier import Notifier

INTERVAL = 60 * 5 # 5 min

if __name__ == '__main__':
    inspector = Inspector()
    notifier = Notifier()

    while True:
        print('Inspection started')
        try:
            inspector.inspect()
            print('Inspection successful')
        except RuntimeError as err:
            print(err, file=sys.stderr)
            notifier.notify(err)

        sleep(INTERVAL)
