#!/usr/bin/python3

#####  Ramtin Alikhani, April 2 2021
import pymysql.cursors
import sys



#path ='/home/ramtin/Desktop/Capstone1/'
# sysargv[1] = dbname
# sysargv[2] = measurement/table name

# The connection to the SQL database will be with the following data structure
client = pymysql.connect(host=sys.argv[1],
                            #port="8080",
                            user=sys.argv[2],
                            #passwd=" ",
                            database=sys.argv[3],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with client:
    with client.cursor() as cursor:
        # extraction
        cursor.execute("SELECT xaxis, yaxis, zaxis FROM {table};".format(table=sys.argv[4]))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    client.commit()

result = cursor.fetchall()

path = sys.argv[5]

for row in result:
  textlist = ("%d,%d,%d" % (row['xaxis'], row['yaxis'], row['zaxis']))
  print(textlist)
  with open(path + "test_pull_data", 'a+') as out:
    out.write(textlist + '\n')

#   windows: TEST COMMAND: D:\Python\python.exe data_extract.py localhost root test 3dspace D:\
#  Linux: TEST COMMAND: python3 data_extract.py localhost root test 3dspace /home/ramtin/Desktop/Capstone1/