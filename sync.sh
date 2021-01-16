#!/bin/bash

# setup absolute paths
images_dir="images"
log_dir="logs"
 
full_path=$(realpath $0)
dir_path=$(dirname $full_path)

# log ip address
ip_addr=`ip addr show wlan0 | awk '/inet / {print $2}'`
echo `date +"%Y-%m-%d-%H-%M-%S"` Sync from $HOSTNAME  $ip_addr >> $dir_path/logs/camera.log

# move files
mv_images="rclone move --exclude .gitkeep $dir_path/$images_dir gdrive:images_$HOSTNAME"
mv_logs="rclone move --exclude .gitkeep $dir_path/$log_dir gdrive:logs_$HOSTNAME"

# repeat  if fails
counter=0
eval $mv_images
eval $mv_logs
while [[ $? -ne 0 && $counter -lt 5 ]]; do
	let counter=counter+1
	sleep 4
	eval $mv_images
	eval $mv_logs
done
