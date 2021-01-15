#!/bin/bash

# log ip address
ip_addr=`ip addr show wlan0 | awk '/inet / {print $2}'`
echo `date +"%Y-%m-%d-%H-%M-%S"` $ip_addr >> camera.log

# move files
rclone move --exclude .gitkeep images gdrive:images_$HOSTNAME
rclone move --exclude .gitkeep logs gdrive:logs_$HOSTNAME

