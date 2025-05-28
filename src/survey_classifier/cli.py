import typer
from survey_classifier.classify_and_update import classify_questions, tag_questions_in_mongo

app = typer.Typer()

@app.command()
def classify(
    mongo_uri: str,
    db_name: str,
    collection_name: str,
    question_field: str = "question_text"
):
    """
    Classify questions in a MongoDB collection using rule-based tagging.
    """
    typer.echo(f"Tagging questions in {db_name}.{collection_name}...")
    tag_questions_in_mongo(
        mongo_uri=mongo_uri,
        db_name=db_name,
        collection_name=collection_name,
        question_field=question_field
    )
    typer.echo("Classification complete...... ")

def main():
    app()

if __name__ == "__main__":
    main()
