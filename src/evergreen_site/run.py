#run it all python!
import subprocess
import time
import signal
import sys

announce_handler_process = None
beacon_handler_process = None
django_server_process = None

def signal_handler(signal, frame):
	print "Handling signal, killing processes"
	print "killing announce handler"
	announce_handler_process.kill()
	print "killing beacon handler"
	beacon_handler_process.kill()
	print "killing django server"
	django_server_process.kill()
	sys.exit(0)

def start_announce_handler():
	print "starting announce handler"
	return subprocess.Popen(["python", "announce_listener.py"])

def start_beacon_handler():
	print "starting beacon handler"
	return subprocess.Popen(["python", "beacon_handler.py"], shell=False)


def start_django_server():
	print "starting djanog server"
	return subprocess.Popen(["python", "manage.py", "runserver", "0.0.0.0:80"], shell=False)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_handler)
	announce_handler_process = start_announce_handler()
	beacon_handler_process = start_beacon_handler()
	django_server_process = start_django_server()

	while(1):
		time.sleep(1)


