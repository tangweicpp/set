#!/bin/bash
cd /root/projs/mjpg/mjpg-streamer-master/mjpg-streamer-experimental
STREAMER=mjpg_streamer
DEVICE=/dev/video0
RESOLUTION=640x480
FRAMERATE=50
HTTP_PORT=8080

PLUGINPATH=/usr/lib
#./$STREAMER -i "$PLUGINPATH/input_uvc.so -n -d $DEVICE -r $RESOLUTION -f $FRAMERATE" -o "$PLUGINPATH/output_http.so -n -p $HTTP_PORT -w ./www" &
./$STREAMER -i "$PLUGINPATH/input_uvc.so -n -d $DEVICE -r $RESOLUTION -f $FRAMERATE -y YUYV" -o "$PLUGINPATH/output_http.so -n -p $HTTP_PORT -w ./www" &
