#Port Scanner
import sys
import socket
from datetime import datetime

print("Please put the IP of the target you want to port scan.")
target = input()

#Define our target
#if len(sys.argv) == 2:
#	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
#else:
#	print("Invalid amount of arguments.")
#	print("Syntax: python3 scanner.py <ip>")


#Add a pretty banner
print('-' * 50)
print("Scanning target " + target)
print("Time Started: " + str(datetime.now()))
print('-' * 50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(.05)
		result =s.connect_ex((target,port)) #returns an error indicator
		#print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open.".format(port))
		if port == 500: #65535
			print("The Scanning is complete!")
		s.close()

except KeyboardInterrupt:
	print("\n Exiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()




input("Press Enter to continue...")
