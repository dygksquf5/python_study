#!/bin/bash


# shellcheck disable=SC2164
source flask/bin/activate
cd flask
export FLASK_APP=pybo
export FLASK_ENV=development


