#Ramtin Alikhani, June 2021 - Parse data for each table for each parameter and input into db 

import pymysql
import sys
import csv
import shutil
import os

path_inbox = '/home/capstone/project/data_inbox'
path_working = '/home/capstone/project/data_working/data'
path_archive = '/home/capstone/project/data_archive'

Files_to_Process = []

for files in os.listdir(path_inbox):
      if files.endswith(".csv"):
            file_path_inbox = f"{path_inbox}/{files}"
            file_path_working = f"{path_working}/{files}"
            shutil.copy(file_path_inbox,file_path_working)
            Files_to_Process.append(files)

mydb = pymysql.connect(host=sys.argv[1], #for actual database, "localhost"
                           user=sys.argv[2], #for actual database, "root"
                           #passwd='123456',
                           db=sys.argv[3]) #for actual database, "WEMS_Data"
cursor = mydb.cursor()
for files in Files_to_Process:
      file_path_working = f"{path_working}/{files}"
      csv_data = csv.reader(open(file_path_working))

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

            
            if ((magnet_xaxis == "x" and magnet_yaxis == "x") and magnet_zaxis == "x"):
                  cursor.execute('INSERT INTO magnetometer(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}",NULL,NULL,NULL);'.format(date,gatewayID,nodeID))
            else: 
                  cursor.execute('INSERT INTO magnetometer(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}","{}");'.format(date,gatewayID,nodeID,magnet_xaxis,magnet_yaxis,magnet_zaxis))
            if ((accel_x == "x" and accel_y == "x") and accel_z == "x"):
                  cursor.execute('INSERT INTO acceleration(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}",NULL,NULL,NULL);'.format(date,gatewayID,nodeID))
            else:
                  cursor.execute('INSERT INTO acceleration(Timestamp,GatewayID,NodeID,xaxis,yaxis,zaxis) VALUES ("{}","{}","{}","{}","{}","{}");'.format(date,gatewayID,nodeID,accel_x,accel_y,accel_z))
            if (humidity == "x"):
                  cursor.execute('INSERT INTO humidity(Timestamp,GatewayID,NodeID,relativeperc) VALUES ("{}","{}","{}",NULL);'.format(date,gatewayID,nodeID))
            else:
                  cursor.execute('INSERT INTO humidity(Timestamp,GatewayID,NodeID,relativeperc) VALUES ("{}","{}","{}","{}");'.format(date,gatewayID,nodeID,humidity))
            if (baropress == "x"):
                  cursor.execute('INSERT INTO baropress(Timestamp,GatewayID,NodeID,hectopa) VALUES ("{}","{}","{}",NULL);'.format(date,gatewayID,nodeID))
            else: 
                  cursor.execute('INSERT INTO baropress(Timestamp,GatewayID,NodeID,hectopa) VALUES ("{}","{}","{}","{}");'.format(date,gatewayID,nodeID,baropress))
            if (temp == "x"):
                  cursor.execute('INSERT INTO temperature(Timestamp,GatewayID,NodeID,degcelc) VALUES ("{}","{}","{}",NULL);'.format(date,gatewayID,nodeID))
            else: 
                  cursor.execute('INSERT INTO temperature(Timestamp,GatewayID,NodeID,degcelc) VALUES ("{}","{}","{}","{}");'.format(date,gatewayID,nodeID,temp))

mydb.commit()
cursor.close()

for files in Files_to_Process:
      file_path_working = f"{path_working}/{files}"
      file_path_archive = f"{path_archive}/{files}"
      shutil.move(file_path_working,file_path_archive)

for files in Files_to_Process:
      file_path_inbox = f"{path_inbox}/{files}"
      os.remove(file_path_inbox)

#for test, tables are acceleration, magnetometer, baropress, humidity, temperature. 

##Old code, might need later:
#cursor.execute('INSERT INTO {table} ({var1},{var2},{var3}) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(magnet_xaxis,magnet_yaxis,magnet_zaxis, accel_x, accel_y, accel_z, humidity, temp, baropress))
