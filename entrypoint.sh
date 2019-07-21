#!/bin/bash

set -eu -o pipefail

exec parallel ::: \
  "gunicorn server:app_factory --config config/gunicorn.conf" \
  "python worker.py"
