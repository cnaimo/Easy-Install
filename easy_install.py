import os
import subprocess
import platform
import logging
from datetime import datetime

class Error(Exception):
	"""Base exception class"""
	pass

class InstallError(Error):
	"""There was an error installing something..."""
	pass


def execute(cmd):
	print('\n___________________________________________________\n'+ cmd + '\n')
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	for x in p.stdout:
		print(x.strip().decode('utf-8'))
	p.wait()
	if p.returncode != 0:
		logging.critical("Error executing:  " +  cmd)
		raise InstallError("Error executing:  " +  cmd)
	else:
		logging.info("Success:  " + cmd)

if __name__ == "__main__":
	file = input("What instruction file would you like to run today?\n")

	logging.basicConfig(filename='LOGGING_' + file[:-4] + '_' + str(datetime.now())[:-7] + '.txt', level=logging.INFO)

	try:
		instruction = open(file, 'r').readlines()
		logging.info(file + ' was loaded successfully')
	except FileNotFoundError:
		logging.warning(file + " isn't found")
		raise FileNotFoundError

	instruction = [x.strip() for x in instruction]
	instruction = [x.split('#')[0] for x in instruction]
	for line in instruction:
		execute(line)
