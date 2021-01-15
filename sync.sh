#!/bin/bash

rclone move images gdrive:images
rclone sync camera.log gdrive:logs
