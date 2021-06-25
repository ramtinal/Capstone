#Ramtin Alikhani, June 2021 - Parse data for each table for each parameter and input into db 

import pymysql
import sys
import csv

path = '/home/ramtin/Desktop/Capstone1/Capstone/test_files/testmod.csv'
#path = '/home/ramtin/Desktop/Capstone1/Capstone/test_files/testmod2.csv'


mydb = pymysql.connect(host=sys.argv[1], #for test, "localhost"
                           user=sys.argv[2], #for test, "root"
                           #passwd='123456',
                           db=sys.argv[3]) #for test, "test"
cursor = mydb.cursor()
csv_data = csv.reader(open(path))


for row in csv_data:
      date = mydb.escape_string(row[0])
      nodeID = mydb.escape_string(row[1])       #var1
      magnet_xaxis = mydb.escape_string(row[2]) #var2
      magnet_yaxis = mydb.escape_string(row[3])  #var3
      magnet_zaxis = mydb.escape_string(row[4])  #var4
      accel_x = mydb.escape_string(row[5])  #var5
      accel_y = mydb.escape_string(row[6])  #var6
      accel_z = mydb.escape_string(row[7])  #var7
      humidity = mydb.escape_string(row[8])  #var8
      temp = mydb.escape_string(row[9])      #var9
      baropress = mydb.escape_string(row[10])  #var10

      
      cursor.execute('INSERT INTO acceleration(Timestamp,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}");'.format(date,nodeID,accel_x,accel_y,accel_z))
      cursor.execute('INSERT INTO magnetometer(Timestamp,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}");'.format(date,nodeID,magnet_xaxis,magnet_yaxis,magnet_zaxis))
      cursor.execute('INSERT INTO baropress(Timestamp,NodeID,hectopa) VALUES ("{}","{}","{}");'.format(date,nodeID,baropress))
      cursor.execute('INSERT INTO temperature(Timestamp,NodeID,degcelc) VALUES ("{}","{}","{}");'.format(date,nodeID,temp))
      cursor.execute('INSERT INTO humidity(Timestamp,NodeID,relativeperc) VALUES ("{}","{}","{}");'.format(date,nodeID,humidity))

mydb.commit()
cursor.close()

#for test, tables are acceleration, magnetometer, baropress, humidity, temperature. 

##Old code, might need later:
#cursor.execute('INSERT INTO {table} ({var1},{var2},{var3}) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(magnet_xaxis,magnet_yaxis,magnet_zaxis, accel_x, accel_y, accel_z, humidity, temp, baropress))