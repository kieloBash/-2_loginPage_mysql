import tkinter as tk
import mysql.connector

from mysql.connector import Error

def createTable():
    mySql_Create_Table_Query = """CREATE TABLE student_profile ( 
                             id int NOT NULL,
                             f_name varchar(250) NOT NULL,
                             l_name varchar(250) NOT NULL,
                             password varchar(250) NOT NULL,
                             email varchar(250) NOT NULL,
                             PRIMARY KEY (id)) """
    return mySql_Create_Table_Query

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='student_database',
                                         user='root',
                                         password='kielo5401')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        
    
        # selecting a database
        # cursor = connection.cursor()
        # cursor.execute('select database();')
        # record = cursor.fetchone()
        # print("You're connected to base: ", record)
        
        
        # creating a table
        # mySql_Create_Table_Query = createTable()
        # cursor = connection.cursor()
        # result = cursor.execute(mySql_Create_Table_Query)
        # connection.commit()
        # print("Table created successfully ")
        
        
        # deleting a table
        # cursor = connection.cursor()
        # delete_table_query = """DROP TABLE Laptop"""
        # cursor.execute(delete_table_query)
        # connection.commit()
        # print("Table and Database Deleted successfully ")
        
        
        # deleting single data
        # delete_data_query = """DELETE from student_profile WHERE id = %s"""
        # index = 3
        # cursor = connection.cursor()
        # cursor.execute(delete_data_query,(index,))
        # connection.commit()
        # print(cursor.rowcount, "Record delete successfully into table")
        
        
        # deleting multiple data
        # delete_data_query = """DELETE from student_profile WHERE id = %s"""
        # toDelete = [(1,),(2,)]
        # cursor = connection.cursor()
        # cursor.executemany(delete_data_query,toDelete)
        # connection.commit()
        # print(cursor.rowcount, "Multiple delete successfully into table")
        
        
        # inserting data
        # index = 3
        # insert_data_query = """INSERT INTO student_profile(id,f_name,l_name,password,email)
        #                 VALUES
        #                 (%s,'Kielo','Mercado','kielo5401','kielo.mercado04@gmail.com')"""
        # cursor = connection.cursor()
        # cursor.execute(insert_data_query, (index,))
        # connection.commit()
        # print(cursor.rowcount, "Record inserted successfully into table")
        
        
        # inserting multiple data
        # insert_data_query = """INSERT INTO student_profile(id,f_name,l_name,password,email)
        #                 VALUES
        #                 (%s,%s,%s,%s,%s)"""
        # toInsert = [(1,'Kielo','Mercado','kielo5401','kielo.mercado04@gmail.com'),
        #             (2,'Brent','Mercado','brent6','brent.mercado12@friendster.com'),
        #             (3,'Klark','Mercado','klark123','klark.mercado26@yahoo.com'),]
        # cursor = connection.cursor()
        # cursor.executemany(insert_data_query, toInsert)
        # connection.commit()
        # print(cursor.rowcount, "Multiple insert successful into table")
        
        
        # selecting
        # select_query = """SELECT * FROM student_profile"""
        # cursor = connection.cursor()
        # cursor.execute(select_query)
        # # get all records
        # records = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        # for row in records:
        #     print("id = ", row[0], end=", ")
        #     print("f_name = ", row[1], end=", ")
        #     print("l_name = ", row[2], end=", ")
        #     print("password = ", row[3], end=", ")
        #     print("email = ", row[4])
            
        #     # trial if condition
        #     # if row[1] == 'Kielo':
        #     #     print("CONNECTION USER KIELO SUCCESSFUL")
        
        
        #  update data
        # update_query = """UPDATE student_profile set f_name = %s WHERE id = %s"""
        # toUpdate = 'Kielo Bash'
        # toUpdateIndex = 1
        # cursor = connection.cursor()
        # cursor.execute(update_query,(toUpdate,toUpdateIndex))
        # connection.commit()
        # print("Record Updated successfully ")
        
        
except Error as e:
    print("Error occured MySQL", e)
    # print("Error while connecting to MySQL", e)
    # print("Failed to create table in MySQL: {}".format(e))
    # print("Failed to Delete table and database: {}".format(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")