#!/usr/bin/python
# coding: utf-8

from django.utils.encoding import smart_str, smart_unicode

import facebook
import urllib
import urlparse
import subprocess
import warnings
import json
import MySQLdb
import sys

theArgs = sys.argv

#PARAMETERS BEGIN
allcoordinates = [str(theArgs[1]),str(theArgs[2]),str(theArgs[3]),str(theArgs[4]),str(theArgs[5]),str(theArgs[6]),str(theArgs[7]),str(theArgs[8]),str(theArgs[9]),str(theArgs[10]),str(theArgs[11]),str(theArgs[12]),str(theArgs[13]),str(theArgs[14]),str(theArgs[15]),str(theArgs[16]),str(theArgs[17]),str(theArgs[18]),str(theArgs[19]),str(theArgs[20]),str(theArgs[21]),str(theArgs[22]),str(theArgs[23]),str(theArgs[24]),str(theArgs[25]),str(theArgs[26]),str(theArgs[27]),str(theArgs[28]),str(theArgs[29]),str(theArgs[30]),str(theArgs[31]),str(theArgs[32]),str(theArgs[33]),str(theArgs[34])]
shift = 1000
limit = 1000
distance = 50000
type = 'place'

#Possible queries = ['restaurant','restorant','restoran','restaurace','restauracia','restavracija','restaurante','restoracio','restawran','ravintola','bwyty','gidan abincin','tsev noj mov','etterem','ulo oriri na onunu','bialann','veitingahus','ristorante','restorans','restoranas','pectopaht','pectopah','ristorant','wharekai','restauracja','makhaayad','restaurang','mgahawa','jatetxea','nha hang','ounje']
allq = ['restaurant','ristorante','restaurante','pectopah']

#PARAMETERS END

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = 250493921820593,
                  client_secret = 'aa4d8f31fe85c311e5932e022c6f336c',
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]
try:
    oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()

facebook_graph = facebook.GraphAPI(oauth_access_token)

for coordinates in allcoordinates:
    for q in allq:
        try:
        	myRecords = facebook_graph.request("search", {'q' : q, 'type' : type, 'limit' : limit, 'offset' : 0, 'center' : coordinates, 'distance' : distance})
        	connector = MySQLdb.connect('localhost', 'admint6WDQQJ', '7IfhKdKAYHZK', 'korkoban', unix_socket="/var/lib/openshift/539735404382ecc2e500008a/mysql//socket/mysql.sock")
        	cursor = connector.cursor()

        	offset = shift
        	all_posts = []
        	try:
        		while myRecords["data"]:
        			all_posts = all_posts + myRecords["data"]
        		        myRecords = facebook_graph.request("search", {'q' : q, 'type' : type, 'limit' : limit, 'offset' : offset, 'center' : coordinates, 'distance' : distance})
        			offset = offset + shift
        	        counter = 1
        		for post in all_posts:
        			print counter
        	            	print post
                	     	print '----------------------------------------------------------------'
                        	counter = counter + 1
        			try:
        				cursor.execute("""
                		        	            INSERT INTO places (id, city, name) values (%s,%s,%s)
                                			""", (post['id'], smart_unicode(post['location']['city']), smart_unicode(post['name'])))
        			except Exception, e:
        				print e.message

        	except Exception, e:
        		print e.message

        	connector.commit()
        	cursor.close()
        	connector.close()
        except Exception, e:
            continue