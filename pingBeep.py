#! /usr/bin/python
#
# Ping a host/IP address every N minutes,  Beep once if host responds, five times if not.
#
# Usage:
#	pingBeep.py [host]
# 
# Why?  Because I want to do something else while waitig for a host to possibly go down 
# due to some mysterious bug

import os,time,datetime,sys

def usage():
    print >>sys.stderr, "Usage: pingBeep.py [host]"

if len(sys.argv) == 1:
    pingMe = "192.168.1.9"
elif len(sys.argv) == 2:
    pingMe = sys.argv[1]
else:
    usage()
    
secondsBetweenTries = 10
howManyTries = 3
beepsIfUp = 1
beepsIfDown = 5

def beep(howMany):
    for i in range(howMany):
        print '\a'  # make sure this works on your "terminal" first

def ping(who):
    response = os.system("ping -c 1 -W 2000 -t 3 " + who)
    return response

for i in range (howManyTries):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not ping(pingMe):
        print >>sys.stderr, "%s: %s is up at %s" % (sys.argv[0],pingMe,now)
        beep(beepsIfUp)
    else:
        print >>sys.stderr, "%s: %s is down at %s" % (sys.argv[0],pingMe,now)
        beep(beepsIfDown)

    time.sleep(secondsBetweenTries)
    

