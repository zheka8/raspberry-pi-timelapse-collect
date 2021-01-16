from time import sleep
from datetime import datetime
import schedule
import logging
import logging.handlers as handlers

from picamera import PiCamera
camera = PiCamera()

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
	schedule.every(10).minutes.do(take_photo)
	'''
	schedule.every().day.at("08:00").do(take_photo)
	schedule.every().day.at("12:00").do(take_photo)
	schedule.every().day.at("15:00").do(take_photo)
	schedule.every().day.at("15:31").do(take_photo)
	schedule.every().day.at("15:32").do(take_photo)
	schedule.every().day.at("15:33").do(take_photo)
	'''

	logger.debug("Scheduled events, entering loop...")
	while True:
		schedule.run_pending()  # check if we need to run anything
		sleep(10)  # wait 10 seconds before checking each time again
