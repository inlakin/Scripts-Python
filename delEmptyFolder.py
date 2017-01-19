#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Delete Empty Folder

Script that remove empty directories recursively
 
Usage:
    delEmptyFolder.py <path> 
    AudioConverter.py -h | --help
    AudioConverter.py -v | --version
 
Options:
  -h, --help      
  -v, --version      
"""

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

finish = False

path = "/media/goa/Oumra/Oumra/Musique"
os.chdir(path)
path = os.getcwd()

print ""
print "Cleaning folder : '%s'" % path
print ""

for root, dirs, files in os.walk(path):

    # Ignoring hidden folders/files
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']

    for d in dirs:
        
        content = os.listdir(root+"/" +d)

        if not content:
            print "[*] Deleting folder %s " % d
            try:
                os.removedirs(root+ "/" +d)
            except Exception, e:
                print e

print "Cleaned!"



