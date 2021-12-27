from time import sleep
from datetime import datetime
import schedule
import logging
import logging.handlers as handlers

from picamera import PiCamera
camera = PiCamera()
camera.rotation = 180
camera.resolution = (3280, 2464)

project_folder = '/home/pi/Projects/raspberry-pi-timelapse-collect/'

# log setup
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')
logHandler = handlers.RotatingFileHandler(project_folder + 'logs/' + 'camera.log',
											maxBytes=100000,
											backupCount=3)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


def get_image_name():
	now = datetime.now()
	return 'image_' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'

def take_photo():
	image_name = get_image_name()

	camera.start_preview()
	sleep(5)
	camera.capture(project_folder + 'images/' + image_name)
	camera.stop_preview()

	logger.info("Took photo: " + image_name)


if __name__ == "__main__":
	# Test
	#schedule.every(1).minute.do(take_photo)

	# Production
	schedule.every().day.at("06:00").do(take_photo)
	schedule.every().day.at("08:00").do(take_photo)
	schedule.every().day.at("10:00").do(take_photo)
	schedule.every().day.at("12:00").do(take_photo)
	schedule.every().day.at("14:00").do(take_photo)
	schedule.every().day.at("16:00").do(take_photo)

	logger.debug("Scheduled events, entering loop...")
	while True:
		schedule.run_pending()  # check if we need to run anything
		sleep(20)  # wait before checking each time again
