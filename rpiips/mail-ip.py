import subprocess, smtplib, re
# email auth
to = 'receiver@email.com'
gmail_user = 'example@gmail.com'
gmail_password = 'gmail password'
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(gmail_user, gmail_password)
# run get-ip.sh, get-local-ip.sh and mail output
IP = subprocess.Popen('sh /home/pi/rpiips/get-ip.sh', shell = True, stdout = subprocess.PIPE)
IP = IP.communicate()
IP = IP[0]
localIP = subprocess.Popen('sh /home/pi/rpiips/get-local-ip.sh', shell = True, stdout = subprocess.PIPE)
localIP = localIP.communicate()
localIP = localIP[0]
reLocalIP = re.compile("r:(\d*\.\d*\.\d*\.\d*)")
localIP = reLocalIP.findall(localIP)[1]
message = 'External IP: ' + str(IP) + '\nLocal IP: ' + str(localIP)
msg = ('Subject: Raspberry Pi reboot\n\n%s' % message)
s.sendmail(gmail_user, to, msg)
s.quit()