import mysql.connector

#connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin123',
        database='indigo'
    )
    mycursor = conn.cursor()
    print('Connection established')
except:
    print('Connection error')

# create a Database on the DB server
#mycursor.execute('create database indigo')
#conn.commit()

#create a table
#mycursor.execute("""
#Create table airport(
#    airport_id integer Primary key,
#    code varchar(10) not null,
#    name varchar(255) not null,
#    city varchar(50) not null
#)
#""")
#conn.commit()

#insert data to table

# mycursor.execute("""
# Insert into airport values
# (1,'DEL','New Delhi','IGIA'),
# (2,'CCU','Kolkata','NSCA'),
# (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()


# mycursor.execute("select * from airport where airport_id > 1")
# data = mycursor.fetchall()
# print(data)

# mycursor.execute("""
# update airport
# set name = 'Bombay'
# where airport_id = 3
# """)
# conn.commit()
#
# mycursor.execute("select * from airport")
# data = mycursor.fetchall()
# print(data)
#
# mycursor.execute("""
# delete from airport
# where airport_id = 3
# """)
# conn.commit()
#
# mycursor.execute("select * from airport")
# data = mycursor.fetchall()
# print(data)