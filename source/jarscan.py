#!/usr/bin/python

import glob
import os

for name in glob.glob('*.jar'):
 #print name
 os.system("dosocs2 oneshot %s" % (name))
