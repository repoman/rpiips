# RPIIPS (Raspberry Pi IPs)

Make your Raspberry Pi email its local and external IPs to you on reboot.

### Setting it up
Put the rpiips folder in /home/pi

Make python email script executable

	sudo chmod +x /home/pi/rpiips/mail-ip

Make script run on reboot

	sudo vi /etc/rc.local

Write the following before "exit 0"

	# email ip address on reboot
	python /home/pi/rpiips/mail-ip.py

### Notes
You could put the rpiips folder other places than /home/pi but you will have to change mail-ip.py.