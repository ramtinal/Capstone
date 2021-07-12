#Ramtin Alikhani, June 2021 - Parse data for each table for each parameter and input into db 

import pymysql
import sys
import csv

path = '/home/ramtin/Desktop/Capstone1/Capstone/test_files/testmod2.csv'

mydb = pymysql.connect(host=sys.argv[1], #for test, "localhost"
                           user=sys.argv[2], #for test, "root"
                           #passwd='123456',
                           db=sys.argv[3]) #for test, "test"
cursor = mydb.cursor()
csv_data = csv.reader(open(path))


for row in csv_data:
      date = mydb.escape_string(row[0])          #timestamp
      gatewayID = mydb.escape_string(row[1])     #gateway ID 
      nodeID = mydb.escape_string(row[2])        #node ID 
      magnet_xaxis = mydb.escape_string(row[3])  #magentometer x-axis
      magnet_yaxis = mydb.escape_string(row[4])  #magnetometer y-axis
      magnet_zaxis = mydb.escape_string(row[5])  #magnetometer z-axis 
      accel_x = mydb.escape_string(row[6])       #accelerometer x-axis 
      accel_y = mydb.escape_string(row[7])       #accelerometer y-axis 
      accel_z = mydb.escape_string(row[8])       #accelerometer z-axis 
      humidity = mydb.escape_string(row[9])      #humidity 
      temp = mydb.escape_string(row[10])         #temperature in C
      baropress = mydb.escape_string(row[11])    #air pressure 

      
      cursor.execute('INSERT INTO baropress(Timestamp,GatewayID,NodeID,hectopa) VALUES ("{}","{}","{}","{}");'.format(date,gatewayID,nodeID,baropress))
      cursor.execute('INSERT INTO temperature(Timestamp,GatewayID,NodeID,degcelc) VALUES ("{}","{}","{}","{}");'.format(date,gatewayID,nodeID,temp))
      cursor.execute('INSERT INTO humidity(Timestamp,GatewayID,NodeID,relativeperc) VALUES ("{}","{}","{}","{}");'.format(date,gatewayID,nodeID,humidity))
      
      if (magnet_xaxis == "x" and magnet_yaxis == "x"):
            cursor.execute('INSERT INTO magnetometer(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}",NULL,NULL,NULL);'.format(date,gatewayID,nodeID,magnet_xaxis,magnet_yaxis,magnet_zaxis))
            cursor.execute('INSERT INTO acceleration(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}","{}");'.format(date,gatewayID,nodeID,accel_x,accel_y,accel_z))
      elif (accel_x == "x" and accel_y == "x"):
            cursor.execute('INSERT INTO acceleration(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}",NULL,NULL,NULL);'.format(date,gatewayID,nodeID))
            cursor.execute('INSERT INTO magnetometer(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}","{}");'.format(date,gatewayID,nodeID,magnet_xaxis,magnet_yaxis,magnet_zaxis))
      else:
            cursor.execute('INSERT INTO acceleration(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}","{}");'.format(date,gatewayID,nodeID,accel_x,accel_y,accel_z))
            cursor.execute('INSERT INTO magnetometer(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}","{}");'.format(date,gatewayID,nodeID,magnet_xaxis,magnet_yaxis,magnet_zaxis))
            

mydb.commit()
cursor.close()

#for test, tables are acceleration, magnetometer, baropress, humidity, temperature. 

##Old code, might need later:
#cursor.execute('INSERT INTO {table} ({var1},{var2},{var3}) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(magnet_xaxis,magnet_yaxis,magnet_zaxis, accel_x, accel_y, accel_z, humidity, temp, baropress))