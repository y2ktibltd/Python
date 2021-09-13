#!/usr/bin/env python3
#import serial, keyboard
import serial
s=serial.Serial("/dev/ttyS4")
while True:
    #Attempt to get keyboard output
    #s.data=s.readline()
    #keyboard.write(str(s.data))

    #Slice output to only show weight numbers
    #print(s.readline()[3:-3],chr(236))

    #Regular print output (raw dump) to newline
    print (s.readline())

