#!/usr/bin/python3

#####  Ramtin Alikhani, April 2 2021
import pymysql.cursors
import sys

#path = '/opt/lampp/bin'
path = '/home/ramtin/Desktop/Capstone/test_directory'


# The connection to the SQL database will be with the following data structure.
client = pymysql.connect(host=sys.argv[1],
                            #port="8080",
                            user=sys.argv[2],
                            #passwd=" ",
                            database=sys.argv[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)



with client:
    with client.cursor() as cursor:
        # insertion test
        cursor.execute("INSERT INTO {table} ({param1},{param2},{param3}) VALUES ({val1}, {val2}, {val3});".format(table=sys.argv[4],param1=sys.argv[5],param2=sys.argv[6],param3=sys.argv[7],val1=sys.argv[8],val2=sys.argv[9],val3=sys.argv[10]))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    client.commit()

result = cursor.fetchall()

# TEST COMMAND: D:\Python\python.exe data_injest2.py localhost root test 3dspace xaxis yaxis zaxis 155 20 3
#  Linux: TEST COMMAND: python3 data_injest2.py localhost root test 3dspace xaxis yaxis zaxis 155 20 3