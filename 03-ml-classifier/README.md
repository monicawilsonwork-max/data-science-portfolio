# ML Classifier (Binary)

**Goal:** Build a baseline binary classifier and document performance & trade‑offs.

## Tasks
- Split data; try Logistic Regression, RandomForest, and XGBoost (optional)
- Use cross‑validation; tune with GridSearchCV
- Report precision/recall, ROC‑AUC, confusion matrix
- Write a 1‑page **Model Card** in `reports/model_card.md`

## Acceptance Criteria
- `src/train.py` trains & saves model to `models/model.pkl`
- `src/evaluate.py` prints metrics & saves plots to `reports/`
- Clear discussion of metrics aligned to a use case (e.g., fraud detection)
