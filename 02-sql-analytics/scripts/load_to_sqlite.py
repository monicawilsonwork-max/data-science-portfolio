import pandas as pd, sqlite3, pathlib, glob
db_path = pathlib.Path('data/processed/warehouse.db')
db_path.parent.mkdir(parents=True, exist_ok=True)
con = sqlite3.connect(db_path)
for csv in glob.glob('data/raw/*.csv'):
    df = pd.read_csv(csv)
    table = pathlib.Path(csv).stem
    df.to_sql(table, con, if_exists='replace', index=False)
print('Loaded CSVs into', db_path)
