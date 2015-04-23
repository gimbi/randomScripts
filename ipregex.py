"""
Quick CLI regex for IP addrs. Great for... finding IP addrs. 
@gimbi
"""
import re, sys, subprocess

ipaddrs = []
ip_regex = re.compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')

def usage(name):
	print "Usage: %s <inputFile>" % name

def scanForIpAddresses(txt):
    for ip in ip_regex.findall(txt):
		ipaddrs.append(ip)

def main():
	if len(sys.argv) != 2: 
		usage(sys.argv[0])
		exit()
	else: fname = sys.argv[1]

	fd = file(fname,'rU')
	
	for line in fd.readlines():
		scanForIpAddresses(line)

	for ip in sorted(set(ipaddrs)):
		print ip
		
if __name__ == '__main__':
	exit(main())
