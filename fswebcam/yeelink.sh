#!/bin/bash
fswebcam -d /dev/video0 -r 320x240 --bottom-banner --title "RaspberryPi@Yeelink" --no-timestamp /root/projs/fswebcam/yeelink.jpg
curl --request POST --data-binary @"/root/projs/fswebcam/yeelink.jpg" --header "U-ApiKey:51cbf13bf93f679e00c31292aa26ca45"  http://api.yeelink.net/v1.0/device/356823/sensor/405013/photos
