#!/bin/bash

rclone move --exclude .gitkeep images gdrive:images
rclone move --exclude .gitkeep logs gdrive:logs
