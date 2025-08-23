# Data Science Portfolio

This repository showcases end‑to‑end projects demonstrating skills in Python, SQL, statistics, machine learning, NLP, and dashboards.

## Highlights
- Clean code with clear READMEs and reproducible steps
- Realistic business questions and acceptance criteria
- Modular structure: each project stands alone

## Projects
- `01-data-cleaning-eda`: Exploratory data analysis & data quality report
- `02-sql-analytics`: SQL business questions with a lightweight SQLite db
- `03-ml-classifier`: Binary classification with scikit-learn, model card
- `04-nlp`: Text classification / sentiment with spaCy or scikit-learn
- `05-dashboard`: Streamlit dashboard using outputs from prior projects

## How to run
```bash
# create environment
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt

# run a project
cd 03-ml-classifier
python src/train.py
```

## License
MIT
