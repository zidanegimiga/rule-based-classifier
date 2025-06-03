from survey_classifier.classify_and_update import tag_questions_in_mongo

MONGO_URI = (
    "mongodb://adminstaging:admin_staging_123@localhost:27017/"
    "survey_db_staging"
)
DB_NAME = "survey_db_staging"
COLLECTION_NAME = "questions"
QUESTION_FIELD = "text"


def main():
    print(f"\n📘 Starting classification in {DB_NAME}.{COLLECTION_NAME}...\n")
    tag_questions_in_mongo(
        mongo_uri=MONGO_URI,
        db_name=DB_NAME,
        collection_name=COLLECTION_NAME,
        question_field=QUESTION_FIELD
    )
    print("Classification complete.\n")


if __name__ == "__main__":
    main()
