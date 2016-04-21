#!/usr/bin/python

import glob, os

for name in glob.glob("/home/nasim/Desktop/dpdncy/antlr-3.4.jar"):
	print name
	cmd = 'dosocs2 oneshot /home/nasim/Desktop/dpdncy/'
	os.system(cmd)
