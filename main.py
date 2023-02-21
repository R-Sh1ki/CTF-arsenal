import os
import sys
import socket
import getopt

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Local Network Info: host name is {}, ip addr is {}.".format(host_name, host_ip))


def usage():
	usage_doc = """
	---------------------------------------------
	|        CTF Arsenal v1.0                   |
	---------------------------------------------
	| Usage: python main.py -options [input]    |
	---------------------------------------------
	"""

	print(usage_doc)



try:
	opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
except getopt.GetoptError as e:
	opts = None
	print('[Error] {}'.format(e))
	usage()
	exit()

for o, a in opts:
	if o in ['-h', '--help']:
		usage()
		exit()