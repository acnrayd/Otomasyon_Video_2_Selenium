# Caner Aydin Youtube Kanali Guvenlik Otomasyonu 2 videosu icin hazirlanmistir. Bu adresteki ilgili orjinal script'in fork'udur: https://gist.github.com/marcelom/4218010

#!/usr/bin/env python
from datetime import datetime
import signal

## Tiny Syslog Server in Python.
##
## This is a tiny syslog server that is able to receive UDP based syslog
## entries on a specified port and save them to a file.
## That's it... it does nothing else...
## There are a few configuration parameters.

bugun = (datetime.now()) #su anki tarih saat
bugun2 = bugun.strftime("%m-%d-%Y-%H:%M") #bugunun tarih saati

LOG_FILE = "zararliip_" + bugun2 + ".log"
print(LOG_FILE)
HOST, PORT = "0.0.0.0", 5144

# NO USER SERVICEABLE PARTS BELOW HERE...
#

import logging
import socketserver
import re

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

class SyslogUDPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		try:

			data = bytes.decode(self.request[0].strip())
			ip_regexim = "src=([^:]+:[^@]+@)?(\d{1,3}\.){3}\d{1,3}(\d)?" ## SRC=IP adresi bulmak icin satir
			src_li_ip = re.search(ip_regexim, data) #REGEX match 1
			f = src_li_ip.group(0) #REGEX match yapıidl, ama src=192.168.2.1 şeklinde
			ip_regexim2 = "([^:]+:[^@]+@)?(\d{1,3}\.){3}\d{1,3}(\d)?" ## SRC='i silmek gerekiyor, bu sadece IP adresini match'leyecek
			src_li_ip2 = re.search(ip_regexim2, f) #sadece IP adresini match'ledi
			socket = self.request[1]
			print(src_li_ip2.group(0))
			logging.info(str(src_li_ip2.group(0))) #sadece ip adresini iceren src_li_ip2 degiskenini diske yazdi
		except:
			pass


if __name__ == "__main__":
	try:
		server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
		signal.signal(signal.SIGALRM,SyslogUDPHandler) #Belirli bir sure sonra hata verip kapansin
		signal.alarm(86400) #Hata verip kapanacagi sure (saniye bakimindan) 60sn*60dk*24sa = 86400 sn
		server.serve_forever(poll_interval=0.5)

	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")
