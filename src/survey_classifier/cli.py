import typer
from survey_classifier.classify_and_update import tag_questions_in_mongo

app = typer.Typer(help="Survey Classifier CLI - Tag MongoDB survey questions using rule-based classification.")

@app.command("classify")
def classify(
    mongo_uri: str = typer.Option(..., help="MongoDB connection URI"),
    db_name: str = typer.Option(..., help="Name of the MongoDB database"),
    collection_name: str = typer.Option(..., help="Collection name containing the questions"),
    question_field: str = typer.Option("question_text", help="Field name containing the question text")
):
    """
    Classify questions in a MongoDB collection using rule-based tagging.
    """
    typer.echo(f"\n📘 Starting classification in {db_name}.{collection_name}...\n")
    tag_questions_in_mongo(
        mongo_uri=mongo_uri,
        db_name=db_name,
        collection_name=collection_name,
        question_field=question_field
    )
    typer.echo("✅ Classification complete.\n")

def main():
    app()

if __name__ == "__main__":
    main()
