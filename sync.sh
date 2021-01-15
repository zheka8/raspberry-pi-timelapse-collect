#!/bin/bash

# log ip address
ip_addr=`ip addr show wlan0 | awk '/inet / {print $2}'`
echo `date +"%Y-%m-%d-%H-%M-%S"` Sync from $HOSTNAME  $ip_addr >> logs/camera.log

# move files
mv_images="rclone move --exclude .gitkeep images gdrive:images_$HOSTNAME"
mv_logs="rclone move --exclude .gitkeep logs gdrive:logs_$HOSTNAME"

# repeat  if fails
eval $mv_images
eval $mv_logs
while [ $? -ne 0 ]; do
	eval $mv_images
	eval $mv_logs
	echo "repeat"
done
