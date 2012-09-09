#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Twface - retrieve Twitter profile images

Written by amp
'''

import csv
import urllib2

csvReader = csv.reader(open('tweets.csv', 'rb'), delimiter=',', quotechar='"')

for row in csvReader:
    filename = row[0] #row[0] has the user ID which will be the filename
    url = row[1] #row[1] has the picture URL
    
    print(url)
    try:
        u = urllib2.urlopen(url)
        localFile = open('twface/' + filename, 'w')
        localFile.write(u.read())
        localFile.close()
    except:
        u = urllib2.urlopen('https://twimg0-a.akamaihd.net/sticky/default_profile_images/default_profile_6_normal.png')
        localFile = open('twface/' + filename, 'w')
        localFile.write(u.read())
        localFile.close()

