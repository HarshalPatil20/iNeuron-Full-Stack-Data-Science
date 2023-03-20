# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:47:11 2022

@author: Admin
"""

import pymongo



client = pymongo.MongoClient("mongodb+srv://Harshal281999:Harshal@cluster0.mt4dotu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)



mydb = client["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

x = mycol.find_one()
print(x)

for x in mycol.find():
    print(x)
  
  
  
  
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
  

  
myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
    print(x)

mycol.drop()
