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
1. Run this command at the root of the project: ```pip install -e .``` (You may want to do so in a virtual environment)
2. Then run this bash command:

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