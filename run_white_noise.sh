#!/bin/sh

if ps -ef | grep -v grep | grep white_noise.py ; then
    exit 0
else
    /home/pi/whiteNoise/white_noise.py &
    exit 0
fi
