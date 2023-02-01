import mysql.connector
from mysql.connector import Error

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='kielo5401')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)

def create_hospital_table(cursor):
    table_query = """CREATE TABLE Hospital (
                    Hospital_Id INT UNSIGNED NOT NULL, 
                    Hospital_Name TEXT NOT NULL, 
                    Bed_Count INT, 
                    PRIMARY KEY (Hospital_Id)
                );"""
    cursor.execute(table_query)
    print("Table created successfully ")
    insert_data_hospital(cursor)
    
def create_doctor_table(cursor):
    table_query = """CREATE TABLE Doctor(
                    Doctor_Id INT UNSIGNED NOT NULL,
                    Doctor_Name TEXT NOT NULL, 
                    Hospital_Id INT NOT NULL, 
                    Joining_Date DATE NOT NULL, 
                    Speciality TEXT NULL, 
                    Salary INT NULL, 
                    Experience INT NULL, 
                    PRIMARY KEY (Doctor_Id)
                );"""
    cursor.execute(table_query)
    print("Table created successfully ")
    insert_data_doctor(cursor)

def insert_data_hospital(cursor):
    insert_query = """INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
                VALUES  (%s,%s,%s)"""
    toInsert = [('1', 'Mayo Clinic', 200),
                ('2', 'Cleveland Clinic', 400), 
                ('3', 'Johns Hopkins', 1000), 
                ('4', 'UCLA Medical Center', 1500)]
    cursor.executemany(insert_query,toInsert)
    print(cursor.rowcount, "Multiple insert successful into table")
    
def insert_data_doctor(cursor):
    insert_query = """INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
                        VALUES   (%s,%s,%s,%s,%s,%s,NULL)"""
    toInsert = [('101', 'David', '1', '2005-2-10', 'Pediatric', '40000'), 
                ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000'), 
                ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000'), 
                ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000'), 
                ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000'), 
                ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000'), 
                ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000'), 
                ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000')]
    cursor.executemany(insert_query,toInsert)
    print(cursor.rowcount, "Multiple insert successful into table")
        

print("Question 1: Print Database version")
try:
    connection = get_connection()
    if connection.is_connected():
        read_database_version()
        cursor = connection.cursor()
        
        create_hospital_table(cursor)
        create_doctor_table(cursor)
        connection.commit()
        
except Error as e:
    print("Error occured MySQL", e)
    
finally:
    if connection.is_connected():
        cursor.close()
        close_connection(connection)
        print("MySQL connection is closed")
        

