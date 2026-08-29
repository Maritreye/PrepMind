from database import db

test_collection = db["test_collection"]
result = test_collection.insert_one({"message": "Hello from PrepMind!"})
print("Inserted document ID:", result.inserted_id)

found = test_collection.find_one({"_id": result.inserted_id})
print("Found document:", found)