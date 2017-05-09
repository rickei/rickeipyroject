##
## read ciscolist.txt
## format : IP HOSTNAME USER PASSORD ENABLEPASSWORD
## delimiter : \t (TAB)

import pexpect
import sys
import csv
import time
#from __future__ import print_function
a = time.strftime("%Y%m%d")
reader = csv.reader(open('ciscolist.txt'), delimiter='\t')
for row in reader:
	f1=open(str(row[1]) + '_' + a + '.txt', 'w')
	try:

		hostip = str(row[0])
		username = str(row[2])
		password = str(row[3])
		enable = str(row[4])

		ssh = 'ssh -o StrictHostKeyChecking=no ' + username + '@' +hostip

		s=pexpect.spawn(ssh)

		s.expect('word')
		s.sendline(password)
		s.expect('>');
		s.sendline('en')
		s.expect('word')
		s.sendline(enable)
		s.expect('#')
		s.sendline('terminal length 0')
		s.expect('#')
		s.sendline('show running-config')

		s.expect('end\r')
		output =  s.before

		s.sendline('exit')
		s.expect('#')
		s.sendline('exit')
		s.expect(pexpect.EOF)
		#print output
		f1.write(output)
		f1.close

	except Exception, e:
		print "The Script failed to login"
		print str(e)

