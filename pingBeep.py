#! /usr/bin/python
#
# Ping a host/IP address every N minutes,  Beep once if host responds, five times if not.
#
# Usage:
#	pingBeep.py [host]
# 
# Why?  Because I want to do something else while waitig for a host to possibly go down 
# due to some mysterious bug
#

import os,time,datetime,sys

def usage():
    print >>sys.stderr, "Usage: pingBeep.py [host [seconds [tries]]]"

pingMe = "192.168.1.9"
secondsBetweenTries = 10
howManyTries = sys.maxint
    
if len(sys.argv) == 1:
    pass

if len(sys.argv) == 2:
    pingMe = sys.argv[1]
    
if len(sys.argv) == 3:
    secondsBetweenTries = float(sys.argv[2])
    
if len(sys.argv) == 4:
    howManyTries = int(sys.argv[3])        

if len(sys.argv) > 4:
    usage()

beepsIfUp = 1
beepsIfDown = 5

def beep(howMany):
    for i in range(howMany):
        print '\a'  # make sure this works on your "terminal" first

def ping(who):
    response = os.system("ping -c 1 -W 2000 -t 3 " + who)
    return response

pingsSent = 0

while (pingsSent < howManyTries):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not ping(pingMe):
        print >>sys.stderr, "%s: %s is up at %s" % (sys.argv[0],pingMe,now)
        beep(beepsIfUp)
    else:
        print >>sys.stderr, "%s: %s is down at %s" % (sys.argv[0],pingMe,now)
        beep(beepsIfDown)

    pingsSent += 1
    time.sleep(secondsBetweenTries)
    

