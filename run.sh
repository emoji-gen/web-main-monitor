#!/bin/bash

set -eu -o pipefail

pyppeteer-install
exec gunicorn app:app_factory --config config/gunicorn.conf
