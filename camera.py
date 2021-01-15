from time import sleep
from datetime import datetime
import schedule
import logging

from picamera import PiCamera
camera = PiCamera()

def get_image_name():
	now = datetime.now()
	return 'images/image_' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'

def take_photo():
	image_name = get_image_name()

	camera.start_preview()
	sleep(5)
	camera.capture(image_name)
	camera.stop_preview()

	logging.info("Taking photo: " + image_name)


if __name__ == "__main__":
	logging.basicConfig(filename='camera.log',
	 					level=logging.DEBUG,
						format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')

	schedule.every(1).minute.do(take_photo)
	'''
	schedule.every().day.at("08:00").do(take_photo)
	schedule.every().day.at("12:00").do(take_photo)
	schedule.every().day.at("15:00").do(take_photo)
	schedule.every().day.at("15:31").do(take_photo)
	schedule.every().day.at("15:32").do(take_photo)
	schedule.every().day.at("15:33").do(take_photo)
	'''

	logging.debug("Scheduled events, entering loop...")
	while True:
		schedule.run_pending()  # check if we need to run anything
		sleep(10)  # wait 10 seconds before checking each time again
