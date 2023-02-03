import mysql.connector
from mysql.connector import Error

# CONNECTING TO MYSQL
def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='kielo5401')
    return connection

def close_connection(cursor,connection):
    if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")    
# ---------------------------------------


# Creating data
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
        
def create_data():
    try:
        connection = get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            
            create_hospital_table(cursor)
            create_doctor_table(cursor)
            connection.commit()
            close_connection(cursor,connection)
            
    except Error as e:
        print("Error occured MySQL", e)
# ---------------------------------------



create_data()
# Q1 
def read_version():
    try:
        connection = get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            connection.commit()
            close_connection(cursor,connection)

    except Error as e:
        print("Error occured MySQL", e)
        
print("Question 1: Print Database version")
read_version()
print("\n")

# Q2
def get_hospital_record(id):
    try:
        connection = get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            select_query = """SELECT * FROM Hospital WHERE Hospital_Id = %s"""
            cursor.execute(select_query,(id,))
            records = cursor.fetchall()
            
            print("Printing Hospital record")
            for row in records:
                print("Hospital Id:", row[0], )
                print("Hospital Name:", row[1])
                print("Bed Count:", row[2])
                
            connection.commit()
            close_connection(cursor,connection)

    except Error as e:
        print("Error occured MySQL", e)
        
def get_doctor_record(id):
    try:
        connection = get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            select_query = """SELECT * FROM Doctor WHERE Doctor_Id = %s"""
            cursor.execute(select_query,(id,))
            records = cursor.fetchall()
            
            print("Printing Doctor record")
            for row in records:
                print("Doctor Id:", row[0])
                print("Doctor Name:", row[1])
                print("Hospital Id:", row[2])
                print("Joining Date:", row[3])
                print("Specialty:", row[4])
                print("Salary:", row[5])
                print("Experience:", row[6])
                
            connection.commit()
            close_connection(cursor,connection)

    except Error as e:
        print("Error occured MySQL", e)

print("Question 2: Read given hospital and doctor details \n")
get_hospital_record(2)
print("\n")
get_doctor_record(105)
print("\n")