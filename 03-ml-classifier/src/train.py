import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib, pathlib

# Placeholder dataset: expects data/processed/train.csv with 'target' column
X = pd.read_csv('data/processed/train.csv')
y = X.pop('target')

pipe = Pipeline([('scaler', StandardScaler()),
                 ('clf', LogisticRegression(max_iter=1000))])

param_grid = {'clf__C':[0.1,1,10]}
grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
grid.fit(X, y)

pathlib.Path('models').mkdir(exist_ok=True, parents=True)
joblib.dump(grid.best_estimator_, 'models/model.pkl')
print('Best params:', grid.best_params_)
