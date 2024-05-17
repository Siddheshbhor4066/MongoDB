
import pymongo

if __name__ == "__main__":

# Connect MongoDB to Python
    student = pymongo.MongoStudent("mongodb://localhost:27017/")
    print(student)
    
# Create Database
    db = student['Siddhesh']

# Create Connection
    connection = db['data']

# Insert Documents
    # One
    dict1 = {"Name":"Siddhesh","Location":"ozar","Gender":
             "Male","Roll no":6}
    connection.insert_one(dict1)

    # Many 
    dict2 = ([
        {"Name":"Siddhesh","Location":"ozar","Gender":"Male","Roll no":6},
        {"Name":"Akash","Location":"Pune","Gender":"Male","Roll no":2},
        {"Name":"Shree","Location":"Mumbai","Gender":"Male","Roll no":7}
        ])

    connection.insert_many(dict2)
    
# Read Documents
    # All
    All_docs = connection.find()
    for items in All_docs:
        print(items)

    # Specific
    print("For Specific")
    docs = connection.find_one({"Name":"Siddesh"})
    print(docs)

# Update 
    # One
    connection.update_one({"Name":"Akash"},{'$set':{"Location":"Ozar"}})

    # Many
    connection.update_many({"Name":"Akash"},{"$set":{"Roll no":5}})

# Delete
    # One
    connection.delete_one({"Name":"Varun"})

    # Many
    connection.delete_many({"Name":"Varun"})

    
# Export Database
  # mongodump
  # run on cmd
    # mongodump ---> for export all database

    # mongodump -d databasename --->for Specific database

    # mongodump -d databasename -c connectionname --->for specific connection


# Import
  # mongorestore
  # run on cmd
    # mongorestore -d newdatabasename pathofdatabase --->import database

    # mongorestore -d newdatabasename -c newconnectionname pathofconnection --->import single connection
