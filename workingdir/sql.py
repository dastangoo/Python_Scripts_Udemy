#!/usr/bin/env python
import MySQLdb as mdb

sql_host = "localhost"
sql_username = "teopy"
sql_password = "python"
sql_database = "NetMon"

sql_connection = mdb.connect(sql_host, sql_username, sql_password, sql_database)
#print sql_connection


cursor = sql_connection.cursor()
cursor.execute("Use NetMon")

#cursor.execute("create table FromPython(Column1 VARCHAR(10), Column2 INT, Column3 FLOAT(6,2))")
cursor.execute("insert into FromPython(Column1, Column2, Column3) VALUES('string', 10, 123.45)")
cursor.execute("select * from FromPython")

output = cursor.fetchone()
print output

sql_connection.commit()

sql_connection.close()
