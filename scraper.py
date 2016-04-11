#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.utils.encoding import smart_str, smart_unicode
from BeautifulSoup import BeautifulSoup

import urllib
import urlparse
import subprocess
import warnings
import json
import MySQLdb
import urllib2
import re

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

connector = MySQLdb.connect('localhost', '***', '***', 'korkoban', unix_socket="/var/lib/openshift/539735404382ecc2e500008a/mysql//socket/mysql.sock")
cursor = connector.cursor()
cursor.execute("""
                    SELECT *
                    FROM places
                    WHERE scraped IS NULL
                    AND number_likes >= 250
       			""")
rows = cursor.fetchall()

for row in rows:
    try:
        if row[7]:
            response = urlsdslib2.urlopen(str(row[7]) + '?id='+ str(row[0]) +'&sk=info')
            html = response.read()

            #Isolate email
            starting =  html.find('<a href="mailto:')
            if starting != -1:
                offset = html.find('</td>', starting)
                if offset != -1:
                    diff = offset - starting
                    end = starting + diff
                    theEmailTemp = remove_html_tags(html[starting:end])
                    theEmail = theEmailTemp.replace('&#064;','@')
                    cursor.execute("""
              	                      UPDATE places
                                      SET
                                        email = %s
                                      WHERE
                                        id = %s
               			              """, (theEmail, str(row[0])) )
                    print theEmail

        cursor.execute("""
              	            UPDATE places
                            SET
                                scraped = 1
                            WHERE
                                id = %s
               			""", (str(row[0]), ) )
    except Exception, e:
        continue

connector.commit()
cursor.close()
connector.close()