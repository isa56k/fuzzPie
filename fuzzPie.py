#!/usr/bin/python
"""
     Author: t:@isa56k e:me@isa56k.com w:www.isa56k.com

       File: fuzzPie.py

    version: 0.1

      About: Based on the fuzzing example from iOS hackers handbook by Charlie Miller.
             Rather than be wrapped in a full loop as per the book this will just fuzz  
             one test case so can be added into fuzzyDuck.sh or fuzzyCactus wrapper script 
             instead of zzuf. It simply takes an original test case and spits out a mutated 
             file to test with.

   Pre-Reqs: You will need to have python installed on your machine or device.

      Usage: ./fuzzPie.py <original input file> <mutated ouput file>
		     copy to /usr/bin and chmod +x if you want to run directly from cmd line.
"""

import random
import math
import sys

def fuzz_buffer(buffer, FuzzFactor):
	buf = list(buffer)
	numwrites=random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
	for j in range(numwrites):
		rbyte = random.randrange(256)
		rn = random.randrange(len(buf))
		buf[rn] = "%c"%(rbyte);
	return "".join(buf)

def fuzz(buf, outputfile):
	fuzzed = fuzz_buffer(buf, 1000)
        out = open(outputfile, "wb")
        out.write(fuzzed)
        out.close()

if(len(sys.argv)<2):
        print "fuzzPie <originalfile> <mutatedfile>"
        sys.exit(0)
else:
		f = open(sys.argv[1], "r")
		inbuf = f.read()
		f.close()
		fuzz(inbuf, sys.argv[2])
