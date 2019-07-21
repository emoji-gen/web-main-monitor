#!/bin/bash

set -eu -o pipefail

exec gunicorn app:app_factory --config config/gunicorn.conf
