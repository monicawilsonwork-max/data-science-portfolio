import pandas as pd, joblib, pathlib
from sklearn.metrics import classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

X = pd.read_csv('data/processed/test.csv')
y = X.pop('target')

model = joblib.load('models/model.pkl')
pred = model.predict(X)
proba = model.predict_proba(X)[:,1]

print(classification_report(y, pred))
auc = roc_auc_score(y, proba)
print('ROC-AUC:', auc)

fpr, tpr, _ = roc_curve(y, proba)
plt.figure()
plt.plot(fpr, tpr, label=f'AUC={auc:.3f}')
plt.plot([0,1],[0,1],'--')
plt.xlabel('FPR'); plt.ylabel('TPR'); plt.title('ROC Curve'); plt.legend()
pathlib.Path('reports').mkdir(exist_ok=True, parents=True)
plt.savefig('reports/roc_curve.png', bbox_inches='tight')
print('Saved reports/roc_curve.png')
