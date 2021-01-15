#!/bin/bash

rclone move --exclude .gitkeep images gdrive:images_$HOSTNAME
rclone move --exclude .gitkeep logs gdrive:logs_$HOSTNAME
