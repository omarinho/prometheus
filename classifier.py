#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.utils.encoding import smart_str, smart_unicode

import facebook
import urllib
import urlparse
import subprocess
import warnings
import json
import MySQLdb

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

connector = MySQLdb.connect('localhost', 'admint6WDQQJ', '7IfhKdKAYHZK', 'korkoban', unix_socket="/var/lib/openshift/539735404382ecc2e500008a/mysql//socket/mysql.sock")
cursor = connector.cursor()
cursor.execute("""
                    SELECT *
                    FROM places
                    WHERE classified IS NULL
       			""")
rows = cursor.fetchall()

facebook_graph = facebook.GraphAPI(oauth_access_token)

for row in rows:
    try:
        page = facebook_graph.get_object(str(row[0]))
        cursor.execute("""
              	            UPDATE places
                            SET
                                number_likes = %s,
                                classified = 1,
                                url = %s
                            WHERE
                                id = %s
           			  """, (page['likes'], page['link'], str(row[0])) )
        print str(row[0])
    except Exception, e:
        continue

connector.commit()
cursor.close()
connector.close()
