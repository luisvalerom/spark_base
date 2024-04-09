#!/bin/bash

set -e

spark-submit --master yarn ${SUBMIT_ARGS} --deploy-mode client app.py ${APP_ARGS}