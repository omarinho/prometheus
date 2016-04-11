#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlencode
from slugify import slugify

import sys
import urllib2
import simplejson
import os
import subprocess
import MySQLdb
import xlwt

theArgs = sys.argv
fistParam = slugify(theArgs[1])
citiesList = []

if fistParam == 'omar52hjb':
    connector = MySQLdb.connect('localhost', '***', '***', 'korkoban', unix_socket="/var/lib/openshift/539735404382ecc2e500008a/mysql//socket/mysql.sock")
    cursor = connector.cursor()
    cursor.execute("""
                    SELECT *
                    FROM cities
        		    ORDER by id
       			""")
    rows = cursor.fetchall()
    for row in rows:
        citiesList.append( str(row[1]) );
    cursor.close()
    connector.close()
else:
    citiesList.append( theArgs[1] );

for aCity in citiesList:
    theCity = urlencode({'address':aCity})
    theFileName = slugify(aCity)

    req = urllib2.Request('http://maps.googleapis.com/maps/api/geocode/json?'+ theCity +'&sensor=true', None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    theCoorData = simplejson.load(f)

    centerLatitude = str(theCoorData['results'][0]['geometry']['location']['lat']).strip()
    centerLongitude = str(theCoorData['results'][0]['geometry']['location']['lng']).strip()
    centerCoordinates = centerLatitude + ',' + centerLongitude
    print 'Center coordinates: ' + centerCoordinates

    try:
        northeastLatitude = str(theCoorData['results'][0]['geometry']['bounds']['northeast']['lat']).strip()
        northeastLongitude = str(theCoorData['results'][0]['geometry']['bounds']['northeast']['lng']).strip()
    except Exception, e:
        northeastLatitude = str(theCoorData['results'][0]['geometry']['viewport']['northeast']['lat']).strip()
        northeastLongitude = str(theCoorData['results'][0]['geometry']['viewport']['northeast']['lng']).strip()
    northeastCoordinates = northeastLatitude + ',' + northeastLongitude
    print 'Northeast coordinates: ' + northeastCoordinates

    try:
        southwestLatitude = str(theCoorData['results'][0]['geometry']['bounds']['southwest']['lat']).strip()
        southwestLongitude = str(theCoorData['results'][0]['geometry']['bounds']['southwest']['lng']).strip()
    except Exception, e:
        southwestLatitude = str(theCoorData['results'][0]['geometry']['viewport']['southwest']['lat']).strip()
        southwestLongitude = str(theCoorData['results'][0]['geometry']['viewport']['southwest']['lng']).strip()
    southwestCoordinates = southwestLatitude + ',' + southwestLongitude
    print 'Southwest coordinates: ' + southwestCoordinates

    northwestCoodinates = northeastLatitude + ',' + southwestLongitude
    print 'Northwest coordinates: ' + northwestCoodinates

    southeastCoordinates = southwestLatitude + ',' + northeastLongitude
    print 'Southeast coordinates: ' + southeastCoordinates

    A1CoordinatesLat = float(southwestLatitude) + ( 0 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A1CoordinatesLong = float(southwestLongitude) + ( 0 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A1Coordinates = str(A1CoordinatesLat) + ',' + str(A1CoordinatesLong)
    print 'A1 coordinates: ' + A1Coordinates

    A2CoordinatesLat = float(southwestLatitude) + ( 0 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A2CoordinatesLong = float(southwestLongitude) + ( 1 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A2Coordinates = str(A2CoordinatesLat) + ',' + str(A2CoordinatesLong)
    print 'A2 coordinates: ' + A2Coordinates

    A3CoordinatesLat = float(southwestLatitude) + ( 0 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A3CoordinatesLong = float(southwestLongitude) + ( 2 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A3Coordinates = str(A3CoordinatesLat) + ',' + str(A3CoordinatesLong)
    print 'A3 coordinates: ' + A3Coordinates

    A4CoordinatesLat = float(southwestLatitude) + ( 0 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A4CoordinatesLong = float(southwestLongitude) + ( 3 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A4Coordinates = str(A4CoordinatesLat) + ',' + str(A4CoordinatesLong)
    print 'A4 coordinates: ' + A4Coordinates

    A5CoordinatesLat = float(southwestLatitude) + ( 0 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A5CoordinatesLong = float(southwestLongitude) + ( 4 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A5Coordinates = str(A5CoordinatesLat) + ',' + str(A5CoordinatesLong)
    print 'A5 coordinates: ' + A5Coordinates

    A6CoordinatesLat = float(southwestLatitude) + ( 1 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A6CoordinatesLong = float(southwestLongitude) + ( 0 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A6Coordinates = str(A6CoordinatesLat) + ',' + str(A6CoordinatesLong)
    print 'A6 coordinates: ' + A6Coordinates

    A7CoordinatesLat = float(southwestLatitude) + ( 1 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A7CoordinatesLong = float(southwestLongitude) + ( 1 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A7Coordinates = str(A7CoordinatesLat) + ',' + str(A7CoordinatesLong)
    print 'A7 coordinates: ' + A7Coordinates

    A8CoordinatesLat = float(southwestLatitude) + ( 1 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A8CoordinatesLong = float(southwestLongitude) + ( 2 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A8Coordinates = str(A8CoordinatesLat) + ',' + str(A8CoordinatesLong)
    print 'A8 coordinates: ' + A8Coordinates

    A9CoordinatesLat = float(southwestLatitude) + ( 1 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A9CoordinatesLong = float(southwestLongitude) + ( 3 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A9Coordinates = str(A9CoordinatesLat) + ',' + str(A9CoordinatesLong)
    print 'A9 coordinates: ' + A9Coordinates

    A10CoordinatesLat = float(southwestLatitude) + ( 1 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A10CoordinatesLong = float(southwestLongitude) + ( 4 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A10Coordinates = str(A10CoordinatesLat) + ',' + str(A10CoordinatesLong)
    print 'A10 coordinates: ' + A10Coordinates

    A11CoordinatesLat = float(southwestLatitude) + ( 2 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A11CoordinatesLong = float(southwestLongitude) + ( 0 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A11Coordinates = str(A11CoordinatesLat) + ',' + str(A11CoordinatesLong)
    print 'A11 coordinates: ' + A11Coordinates

    A12CoordinatesLat = float(southwestLatitude) + ( 2 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A12CoordinatesLong = float(southwestLongitude) + ( 1 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A12Coordinates = str(A12CoordinatesLat) + ',' + str(A12CoordinatesLong)
    print 'A12 coordinates: ' + A12Coordinates

    A13CoordinatesLat = float(southwestLatitude) + ( 2 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A13CoordinatesLong = float(southwestLongitude) + ( 2 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A13Coordinates = str(A13CoordinatesLat) + ',' + str(A13CoordinatesLong)
    print 'A13 coordinates: ' + A13Coordinates

    A14CoordinatesLat = float(southwestLatitude) + ( 2 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A14CoordinatesLong = float(southwestLongitude) + ( 3 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A14Coordinates = str(A14CoordinatesLat) + ',' + str(A14CoordinatesLong)
    print 'A14 coordinates: ' + A14Coordinates

    A15CoordinatesLat = float(southwestLatitude) + ( 2 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A15CoordinatesLong = float(southwestLongitude) + ( 4 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A15Coordinates = str(A15CoordinatesLat) + ',' + str(A15CoordinatesLong)
    print 'A15 coordinates: ' + A15Coordinates

    A16CoordinatesLat = float(southwestLatitude) + ( 3 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A16CoordinatesLong = float(southwestLongitude) + ( 0 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A16Coordinates = str(A16CoordinatesLat) + ',' + str(A16CoordinatesLong)
    print 'A16 coordinates: ' + A16Coordinates

    A17CoordinatesLat = float(southwestLatitude) + ( 3 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A17CoordinatesLong = float(southwestLongitude) + ( 1 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A17Coordinates = str(A17CoordinatesLat) + ',' + str(A17CoordinatesLong)
    print 'A17 coordinates: ' + A17Coordinates

    A18CoordinatesLat = float(southwestLatitude) + ( 3 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A18CoordinatesLong = float(southwestLongitude) + ( 2 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A18Coordinates = str(A18CoordinatesLat) + ',' + str(A18CoordinatesLong)
    print 'A18 coordinates: ' + A18Coordinates

    A19CoordinatesLat = float(southwestLatitude) + ( 3 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A19CoordinatesLong = float(southwestLongitude) + ( 3 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A19Coordinates = str(A19CoordinatesLat) + ',' + str(A19CoordinatesLong)
    print 'A19 coordinates: ' + A19Coordinates

    A20CoordinatesLat = float(southwestLatitude) + ( 3 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A20CoordinatesLong = float(southwestLongitude) + ( 4 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A20Coordinates = str(A20CoordinatesLat) + ',' + str(A20CoordinatesLong)
    print 'A20 coordinates: ' + A20Coordinates

    A21CoordinatesLat = float(southwestLatitude) + ( 4 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A21CoordinatesLong = float(southwestLongitude) + ( 0 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A21Coordinates = str(A21CoordinatesLat) + ',' + str(A21CoordinatesLong)
    print 'A21 coordinates: ' + A21Coordinates

    A22CoordinatesLat = float(southwestLatitude) + ( 4 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A22CoordinatesLong = float(southwestLongitude) + ( 1 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A22Coordinates = str(A22CoordinatesLat) + ',' + str(A22CoordinatesLong)
    print 'A22 coordinates: ' + A22Coordinates

    A23CoordinatesLat = float(southwestLatitude) + ( 4 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A23CoordinatesLong = float(southwestLongitude) + ( 2 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A23Coordinates = str(A23CoordinatesLat) + ',' + str(A23CoordinatesLong)
    print 'A23 coordinates: ' + A23Coordinates

    A24CoordinatesLat = float(southwestLatitude) + ( 4 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A24CoordinatesLong = float(southwestLongitude) + ( 3 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A24Coordinates = str(A24CoordinatesLat) + ',' + str(A24CoordinatesLong)
    print 'A24 coordinates: ' + A24Coordinates

    A25CoordinatesLat = float(southwestLatitude) + ( 4 * ((float(northeastLatitude) - float(southwestLatitude))/4) )
    A25CoordinatesLong = float(southwestLongitude) + ( 4 * ((float(northeastLongitude) - float(southwestLongitude))/4) )
    A25Coordinates = str(A25CoordinatesLat) + ',' + str(A25CoordinatesLong)
    print 'A25 coordinates: ' + A25Coordinates

    B1Coordinates = northeastLatitude + ',' + centerLongitude
    print 'B1 coordinates: ' + B1Coordinates
    B2Coordinates = centerLatitude + ',' + northeastLongitude
    print 'B2 coordinates: ' + B2Coordinates
    B3Coordinates = southwestLatitude + ',' + centerLongitude
    print 'B3 coordinates: ' + B3Coordinates
    B4Coordinates = centerLatitude + ',' + southwestLongitude
    print 'B4 coordinates: ' + B4Coordinates

    connector = MySQLdb.connect('localhost', '***', '***', 'korkoban', unix_socket="/var/lib/openshift/539735404382ecc2e500008a/mysql//socket/mysql.sock")
    cursor = connector.cursor()

    print "Truncating data..."
    cursor.execute("""
                        TRUNCATE TABLE places
       	    		""")

    print "Running search engine..."
    child = subprocess.Popen("/var/lib/openshift/539735404382ecc2e500008a/app-root/runtime/dependencies/python/virtenv/bin/python /var/lib/openshift/539735404382ecc2e500008a/app-root/repo/prometeus/search-engine.py " + centerCoordinates + " " + northeastCoordinates + " " + southwestCoordinates + " " + northwestCoodinates + " " + southeastCoordinates + " " + A1Coordinates + " " + A2Coordinates + " " + A3Coordinates + " " + A4Coordinates + " " + A5Coordinates + " " + A6Coordinates + " " + A7Coordinates + " " + A8Coordinates + " " + A9Coordinates + " " + A10Coordinates + " " + A11Coordinates + " " + A12Coordinates + " " + A13Coordinates + " " + A14Coordinates + " " + A15Coordinates + " " + A16Coordinates + " " + A17Coordinates + " " + A18Coordinates + " " + A19Coordinates + " " + A20Coordinates + " " + A21Coordinates + " " + A22Coordinates + " " + A23Coordinates + " " + A24Coordinates + " " + A25Coordinates + " " + B1Coordinates + " " + B2Coordinates + " " + B3Coordinates + " " + B4Coordinates, shell=True)
    child.wait()

    print "Running classifier..."
    child = subprocess.Popen("/var/lib/openshift/539735404382ecc2e500008a/app-root/runtime/dependencies/python/virtenv/bin/python /var/lib/openshift/539735404382ecc2e500008a/app-root/repo/prometeus/classifier.py", shell=True)
    child.wait()

    print "Running scraper..."
    child = subprocess.Popen("/var/lib/openshift/539735404382ecc2e500008a/app-root/runtime/dependencies/python/virtenv/bin/python /var/lib/openshift/539735404382ecc2e500008a/app-root/repo/prometeus/scraper.py", shell=True)
    child.wait()

    print "Exporting data..."
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Data")

    style = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['light_green']
    style.pattern = pattern

    ws.write(0, 0, 'CITY', style)
    ws.write(0, 1, 'RESTAURANT NAME', style)
    ws.write(0, 2, 'EMAIL', style)
    ws.write(0, 3, 'LIKES', style)
    ws.write(0, 4, 'FB URL', style)
    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 50
    ws.col(2).width = 256 * 27
    ws.col(3).width = 256 * 7
    ws.col(4).width = 256 * 100

    style2 = xlwt.XFStyle()
    pattern2 = xlwt.Pattern()
    pattern2.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern2.pattern_fore_colour = xlwt.Style.colour_map['light_yellow']
    style2.pattern = pattern2

    cursor.execute("""
                    SELECT city,name,email,number_likes,url
                    FROM places
                    WHERE email IS NOT NULL
                    AND number_likes >= 250
       			""")
    rows = cursor.fetchall()

    rowNumber = 1
    for row in rows:
        ws.write(rowNumber, 0, unicode(str(row[0]), errors='replace'),style2)
        ws.write(rowNumber, 1, unicode(str(row[1]), errors='replace'),style2)
        ws.write(rowNumber, 2, unicode(str(row[2]), errors='replace'),style2)
        ws.write(rowNumber, 3, row[3],style2)
        ws.write(rowNumber, 4, unicode(str(row[4]), errors='replace'),style2)
        rowNumber = rowNumber + 1

    style3 = xlwt.XFStyle()
    pattern3 = xlwt.Pattern()
    pattern3.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern3.pattern_fore_colour = xlwt.Style.colour_map['sky_blue']
    style3.pattern = pattern3

    cursor.execute("""
                    SELECT city,name,email,number_likes,url
                    FROM places
                    WHERE email IS NULL
                    AND number_likes >= 250
       			""")
    rows = cursor.fetchall()

    for row in rows:
        ws.write(rowNumber, 0, unicode(str(row[0]), errors='replace'),style3)
        ws.write(rowNumber, 1, unicode(str(row[1]), errors='replace'),style3)
        ws.write(rowNumber, 2, unicode(str(row[2]), errors='replace'),style3)
        ws.write(rowNumber, 3, row[3],style3)
        ws.write(rowNumber, 4, unicode(str(row[4]), errors='replace'),style3)
        rowNumber = rowNumber + 1

    cursor.execute("""
                    SELECT city,name,email,number_likes,url
                    FROM places
                    WHERE number_likes < 250
       			""")
    rows = cursor.fetchall()

    for row in rows:
        ws.write(rowNumber, 0, unicode(str(row[0]), errors='replace'))
        ws.write(rowNumber, 1, unicode(str(row[1]), errors='replace'))
        ws.write(rowNumber, 2, unicode(str(row[2]), errors='replace'))
        ws.write(rowNumber, 3, row[3])
        ws.write(rowNumber, 4, unicode(str(row[4]), errors='replace'))
        rowNumber = rowNumber + 1

    wb.save('data/' + theFileName + '.xls')

    cursor.close()
    connector.close()