#!/bin/bash 
cd /shop/randomsilo/rpi-gpio-api/
git reset --hard
git pull
export FLASK_APP=rpi-gpio-api.py
flask run --host=0.0.0.0