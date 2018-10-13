#!/usr/bin/env python
#
#
#
#
import sys
import csv

infile = "/var/log/direwolf/2018-09-30.log"
counter = 0
        #channel, time_int, time_iso, src_addr, station_heard, audio_lvl, error_corr, dti, obj_name, symb, latitude, longitude, speed, course, altitude, freq, offset, tone,
 system, status, telemetry, comment = line.split ( ',' )

with open ( infile ) as f :
        reader = csv.reader ( line.replace ( '\0', '' ) for line in f )
        for row in reader :
                if len ( row ) == 0 :
                        continue

                if row [ 4 ] != "KK4EHJ-6" :
                        counter = counter + 1
                        print ( "Station : " + row [ 3 ] )

f.close ()

print ( "Found " + repr ( counter ) + " messages." )
