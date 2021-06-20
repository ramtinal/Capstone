#Ramtin Alikhani, June 2021 - Parse data from CSV and put into test database

import pymysql
import sys
import csv

path = '/home/ramtin/Desktop/Capstone1/test_files/test.csv'


mydb = pymysql.connect(host=sys.argv[1], #for test, "localhost"
                           user=sys.argv[2], #for test, "root"
                           #passwd='123456',
                           db=sys.argv[3]) #for test, "test"
cursor = mydb.cursor()
csv_data = csv.reader(open(path))

for row in csv_data:
    var1 = mydb.escape_string(row[0])
    var2 = mydb.escape_string(row[1])
    var3 = mydb.escape_string(row[2])
    cursor.execute('INSERT INTO 3dspace(xaxis,yaxis,zaxis) VALUES ("{}","{}","{}");'.format(var1,var2,var3))

mydb.commit()
cursor.close()
