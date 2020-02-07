#!/usr/bin/python
import time


# Python memory Eater program for eating 10mb of memory at a time. this gets Stopped when used with Cgroups setting the memory
limit to 100mb

biglist=[]
for i in xrange(1,10):
   biglist.append(''*1024 * 100000) #10mb
   print("allocated {0} MB of memory".format(i+1))
   time.sleep(2.4)
print("Done")
