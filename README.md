## About
survey-classifier is a command-line tool designed to automatically classify and tag survey questions stored in MongoDB collections using a rule-based classification system. It connects to your MongoDB instance, scans survey question texts, and applies predefined rules to assign meaningful tags or categories. This helps streamline survey data analysis, improve data organization, and accelerate insights generation by automating the tedious manual tagging process.


## Structure

```
rule-based-classifier/
├── pyproject.toml
├── setup.cfg
├── README.md
├── src/
│   └── survey_classifier/
│       ├── __init__.py
│       ├── cli.py
│       ├── classifier.py
│       ├── keywords_config.py
│       ├── classify_and_update.py
│       └── utils.py
```

## How to run
1. Run this command at the root of the project: ```pip install -e .``` (You may want to do so in a virtual environment):
```
python3 -m venv venv
```

Thhen:
```
source venv/bin/activate
```

2. Then run this bash command to test the cli:

```
python -m survey_classifier.cli --help
```

3. Run this command passing your mongo uri and the collection name of your questions collection

```
survey-classifier classify \
  --mongo-uri "mongodb://localhost:27017" \
  --db-name "survey_data" \
  --collection-name "questions"
```

For help:
```
survey-classifier --help
```
