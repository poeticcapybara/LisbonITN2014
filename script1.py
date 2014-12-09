#!/usr/bin/python

import os
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
	ext = sys.argv[1]
	for filename in os.listdir('.'):
            if os.path.isfile(filename) and ''.join(['.',ext]) in filename:
		print filename
    else:
        print 'No extension selected. Please choose file extension'
        ext = raw_input()
        for filename in os.listdir('.'):
	    if ''.join(['.',ext]) in filename:
	        print filename

    for root, dirs, files in os.walk("."):
        path = root.split('/')
        print (len(path) - 1) *'---' , os.path.basename(root)       
        for file in files:
            print len(path)*'---', file

#    files = [f for f in os.listdir('.') if os.path.isfile(f)]

