'''
    Database : database which is contain data in the from of table

    pymysql


    pip install <packagename>


'''
import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

# execute respective query

mycursor.execute("create database IF NOT EXISTS mydb2023")

# to save this ststement
mydb.commit()

#db connection

mydb = pymysql.connect(host="localhost",user="root",password="",database="mydb2023")
mycursor = mydb.cursor()

mydb.commit()
