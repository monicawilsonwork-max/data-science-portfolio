# Telco Customer Churn — Decision Scientist Case Study

**Role Simulation:** Decision Scientist / Applied Data Scientist  
**Business Problem:** Customer churn (cancellations) costs telecom companies millions each year.  
**Goal:** Identify churn drivers, predict churn risk, and recommend strategies for retention.

---

## 📊 Dataset
- **Source:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- **Size:** 7,043 customers × 21 columns  
- **Key Features:**  
  - Demographics (gender, senior citizen, dependents)  
  - Services (phone, internet, streaming, tech support)  
  - Contract type, billing method, monthly charges  
  - Target: **Churn** (Yes/No)

---

## 🔎 Analysis Workflow
1. **Data Audit & Cleaning**  
   - Converted `TotalCharges` to numeric  
   - Checked missing values, imputed where needed  
   - Created tenure bins for easier segmentation  

2. **Exploratory Data Analysis (EDA)**  
   - Overall churn rate calculated  
   - Churn by contract type, payment method, and tenure  
   - Visualized churn trends with Seaborn & Matplotlib  

3. **SQL-style Questions (DuckDB integration)**  
   - Which services are most associated with churn?  
   - What is the churn rate by contract type and tenure segment?  
   - Which customer segments are highest-value + highest-risk?  

4. **Modeling (Scikit-learn)**  
   - Logistic Regression and Random Forest tested  
   - Evaluated with accuracy, precision, recall, AUC  
   - Saved best model as `models/churn_pipeline.joblib`  

5. **Executive Dashboard (Streamlit)**  
   - Interactive churn probability calculator  
   - Displays churn risk for a sample customer profile  
   - Future: Add cost-benefit optimization + SHAP explainability  

---

## 📈 Key Insights
- **Overall churn rate:** ~26%  
- **Month-to-month contracts** have the highest churn risk  
- **Longer-tenure and two-year contract customers** churn the least  
- **Electronic check payments** are strongly associated with higher churn  

---

## 💡 Business Recommendations
- Prioritize retention offers for **month-to-month customers** in their first 6 months.  
- Incentivize customers to move from **monthly → annual contracts**.  
- Targeted outreach to **electronic check payers** with discounts or auto-pay benefits.  
- Introduce **early tenure loyalty rewards** to reduce risk in the first 12 months.  

---

## 🛠️ Tech Stack
- **Language:** Python (pandas, seaborn, matplotlib, scikit-learn)  
- **SQL Engine:** DuckDB (embedded SQL for analytics)  
- **Dashboard:** Streamlit (interactive churn prediction demo)  
- **Version Control:** Git + GitHub  

---

## 🚀 Next Steps
- Tune classification threshold using **ROI-based retention scenarios**  
- Add SHAP feature importance for explainability  
- Deploy Streamlit dashboard to Hugging Face / Streamlit Cloud  
- Expand project with **time-series churn forecasting**

---

## 📂 Project Structure

# Data Science Portfolio — Dr. Monica M. Wilson, DBA

Remote-first Decision Scientist / Applied Data Scientist.  
I connect advanced business strategy with practical ML to drive measurable outcomes.

## Featured Projects
- **Telco Customer Churn** (Telecom/AT&T-style)  
  Predict churn, explain drivers, and propose ROI-based retention actions.  
  ➜ Read the case study: `01-data-cleaning-eda/telco-churn/README.md`

## Tech Stack
Python (pandas, scikit-learn, matplotlib/seaborn), DuckDB (SQL-in-Python), Streamlit, Git/GitHub.

## Run Locally
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

01-data-cleaning-eda/
  telco-churn/
    data/raw/telco_churn.csv
    notebooks/01_eda_telco_churn.ipynb
    app/app.py
    models/churn_pipeline.joblib
    README.md


---



**In VS Code (GUI):**
1. Click the **Source Control** icon (left sidebar).
2. Click **+** next to the three README files to stage them:
   - `README.md` (root)
   - `01-data-cleaning-eda/README.md`
   - `01-data-cleaning-eda/telco-churn/README.md`
3. Message: `Add portfolio READMEs (root, folder index, telco case study)`
4. Click **Commit** → **Sync/Push**.

**Or in the terminal:**
```bash
git add README.md 01-data-cleaning-eda/README.md 01-data-cleaning-eda/telco-churn/README.md
git commit -m "Add portfolio READMEs (root, folder index, telco case study)"
git push

