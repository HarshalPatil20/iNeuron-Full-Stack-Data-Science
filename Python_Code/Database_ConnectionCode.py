# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 16:14:18 2022

@author: Admin
"""

import mysql.connector as conn 
mydb = conn.connect(host = "localhost" , user = "root" , passwd= "Harshal@1999")
print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database Harshal")
#cursor.execute("show databases")

#print(cursor.fetchall())

#s = "create table Harshal.ineuron(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
#q1 = cursor.execute(s)

q2 = cursor.execute("select * from Harshal.ineuron")
print(q2)

