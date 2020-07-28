import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycol = mydb["customers"]
mycol.drop() 
mycol = mydb["customers"]
mydict = { "name": "Ashish", "address": "Bangalore" }
x = mycol.insert_one(mydict)
print(x.inserted_id) 
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id) 

dblist = myclient.list_database_names()

print(dblist)
print(mydb.list_collection_names())

if "mydatabase" in dblist:
    print("The database exits.")


collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")


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





mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids) 

# The find_one() method returns the first occurrence in the selection.
x = mycol.find_one()
print(x) 


# Return all documents in the "customers" collection, and print each document:
for x in mycol.find():
  print(x) 



# The second parameter of the find() method is an object describing which fields to include in the result.
# This parameter is optional, and if omitted, all fields will be included in the result.


for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x) 

for x in mycol.find({},{ "address": 0 }):
  print(x) 


#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
# for x in mycol.find({},{ "name": 1, "address": 0 }):
#   print(x) 

# Doubt ?
# for x in mycol.find({},{ "_id":0, "name": 1, "address": 0 }):
#   print(x) 


# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search.

myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) 

# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) 


# Filter With Regular Expressions
# You can also use regular expressions as a modifier.
# Regular expressions can only be used to query strings.
# To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:

myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x) 


#   Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x) 