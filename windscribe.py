import subprocess
import time

timeout = 15

def connect():
	print("Trying to connect")
	start_conn = subprocess.Popen(['windscribe', 'connect', 'vice'])

def isConnected():
	global timeout
	connected = False

	while connected == False:
		connect()
		get_status = subprocess.Popen(['windscribe', 'status'], stdout = subprocess.PIPE)
		status_response = get_status.communicate()

		if 'CONNECTED' in status_response:
			connected = True
		else:
			timeout += timeout
			time.sleep(timeout)
			isConnected()

isConnected()
