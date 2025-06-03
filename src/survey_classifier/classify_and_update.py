from pymongo import MongoClient
from .classifier import classify_question


def tag_questions_in_mongo(
    mongo_uri: str,
    db_name: str,
    collection_name: str,
    question_field: str = "text",
):
    client = MongoClient(mongo_uri)
    collection = client[db_name][collection_name]
    print("Connected to mongo instance")
    
    cursor = collection.find({question_field: {"$exists": True}})

    for doc in cursor:
        question = doc.get(question_field, "")
        print(f"Question: {question}")
        modules = classify_question(question)
        collection.update_one(
            {"_id": doc["_id"]},
            {
                "$set": {
                    "module_tags": modules,
                    "classification_method": "rule-based"
                }
            }
        )
