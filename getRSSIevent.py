#!/usr/bin/env python

# GET EVENT DATA

import os
import psutil
import sys
import time
import requests
import logging

logging.basicConfig(filename='log-file.log',level=logging.DEBUG)

#guidance
## Failure and event reporting of the device (process not running, processor overheat, lost
## connection to GSPS terminal, CPU more than 80% etc)
loop = True

while loop == True: #initate infinite loop every 60 seconds
	
	epoch = int(time.time()) # time on current loop
	
	# detecting connection to User Terminal
	usb_found = False
	while usb_found == False:
		import serial.tools.list_ports
		ports = list(serial.tools.list_ports.comports())
		if ports == []:
			print()
			print('Device not Found. Please check the connection.')
			print('Waiting 5 seconds ...')
			logging.debug('USB not found ' + str(epoch))
			usb_found = False
		else:
			print()
			print('Device found')
			usb_found = True
		
		time.sleep(5)

	# detecting process
	from subprocess import Popen

	found_process = False
	for process in psutil.process_iter():
		if process.cmdline() == ['python', 'getrssi.py']:
			#sys.exit('Process found: exiting.')
			found_process = True
			print("Process is running")

	if found_process == False:
		found_process = False
		response = requests.post("https://vms.inmarsat.com/apiv2", json={"event":"process not running","ts": epoch, "severity":0})
		print("Process Status code: ", response.status_code)
		logging.debug('Process not running ' + str(epoch))
		print('Process not found: starting it.')
		Popen(['python', 'getrssi.py'])
		
	# detecting processor overheat
	def get_cpu_temp():
		tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
		cpu_temp = tempFile.read()
		tempFile.close()
		return round(float(cpu_temp)/1000, 2)

	cpu_temp = get_cpu_temp()
	print("CPU Temperature: " + str(cpu_temp) + " deg Celsius")

	## deciding overheat or not
	### from several literature and documents said that raspi should be working normally below 80 deg celsius.
	overheat = False
	if cpu_temp > 70: # if cpu temp more than 80 deg celsius
		print('CPU Overheating ...')
		overheat = True
		response = requests.post("https://vms.inmarsat.com/apiv2", json={"event":"processor overheat","ts": epoch, "severity":1})
		print("Heat Status code: ", response.status_code)
		logging.debug('CPU overheat ' + str(epoch))
	else:
		#print('CPU is on Working temperature')
		overheat = False

	# detecting CPU overload
	overload = False
	cpu_usage = psutil.cpu_percent()
	print("CPU Usage: " + str(cpu_usage) + "%")

	if cpu_usage > 80: # if cpu usage more than 80 percent
		print('CPU Overload ... ')
		overload = True
		response = requests.post("https://vms.inmarsat.com/apiv2", json={"event":"processor overheat","ts": epoch, "severity":1})
		print("CPU Status code: ", response.status_code)
		logging.debug('CPU usage overload ' + str(epoch))
	else:
		#print('CPU is working normally')
		overload = False

	# detecting memory overload
	mem_overload = False
	memory_usage = psutil.virtual_memory().percent
	print("Memory Usage: " + str(memory_usage) + "%")

	if memory_usage > 80: # if cpu usage more than 80 percent
		print('Caution. High usage on memory ')
		mem_overload = True
		response = requests.post("https://vms.inmarsat.com/apiv2", json={"event":"processor overheat","ts": epoch, "severity":1})
		print("Memory Status code: ", response.status_code)
		logging.debug('Memory usage overload ' + str(epoch))
	else:
		#print('Memory is working normally')
		overload = False	
	
	print()	
	time.sleep(5)

