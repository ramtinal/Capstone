#Ramtin Alikhani, June 2021 - Parse data for each table for each parameter and input into db 

import pymysql
import sys
import csv

path = '/home/ramtin/Desktop/Capstone1/Capstone/test_files/testmod.csv'


mydb = pymysql.connect(host=sys.argv[1], #for test, "localhost"
                           user=sys.argv[2], #for test, "root"
                           #passwd='123456',
                           db=sys.argv[3]) #for test, "test"
cursor = mydb.cursor()
csv_data = csv.reader(open(path))


for row in csv_data:
      nodeID = mydb.escape_string(row[0])       #var1
      magnet_xaxis = mydb.escape_string(row[1]) #var2
      magnet_yaxis = mydb.escape_string(row[2])  #var3
      magnet_zaxis = mydb.escape_string(row[3])  #var4
      accel_x = mydb.escape_string(row[4])  #var5
      accel_y = mydb.escape_string(row[5])  #var6
      accel_z = mydb.escape_string(row[6])  #var7
      humidity = mydb.escape_string(row[7])  #var8
      temp = mydb.escape_string(row[8])      #var9
      baropress = mydb.escape_string(row[9])  #var10

      
      cursor.execute('INSERT INTO acceleration(NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}");'.format(nodeID,accel_x,accel_y,accel_z))
      cursor.execute('INSERT INTO magnetometer(NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}");'.format(nodeID,magnet_xaxis,magnet_yaxis,magnet_zaxis))
      cursor.execute('INSERT INTO baropress(NodeID,hectopa) VALUES ("{}","{}");'.format(nodeID,baropress))
      cursor.execute('INSERT INTO temperature(NodeID,degcelc) VALUES ("{}","{}");'.format(nodeID,temp))
      cursor.execute('INSERT INTO humidity(NodeID,relativeperc) VALUES ("{}","{}");'.format(nodeID,humidity))

mydb.commit()
cursor.close()

#for test, tables are acceleration, magnetometer, baropress, humidity, temperature. 

##Old code, might need later:
#cursor.execute('INSERT INTO {table} ({var1},{var2},{var3}) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(magnet_xaxis,magnet_yaxis,magnet_zaxis, accel_x, accel_y, accel_z, humidity, temp, baropress))