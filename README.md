# Credit Card Default Prediction — Exploratory Analysis

Exploratory data analysis of the **Default of Credit Card Clients** dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients), as part of the Data Science & Artificial Intelligence course at PUCRS.

## Dataset Overview

| Detail | Value |
|--------|-------|
| **Source** | UCI ML Repository / Kaggle |
| **Records** | 30,000 |
| **Features** | 25 (including target) |
| **Target** | `default payment next month` (binary: 0/1) |
| **Missing values** | None |
| **Format** | XLS (original), CSV (cleaned) |
| **License** | CC BY 4.0 |

The dataset contains demographic info, credit limit, payment history, bill amounts, and payment amounts for 30,000 credit card clients from a Taiwanese bank (April–September 2005). The target variable indicates whether the client defaulted in the following month.

## Key Findings

- **Default rate:** 22.1% (6,636 out of 30,000 clients)
- **Most common credit limit:** NT$ 50,000
- **Average age:** 35.5 years
- **Gender split:** 60.4% female, 39.6% male
- **Education:** 46.8% university, 35.3% graduate school

## Project Structure

```
├── README.md
├── data/
│   └── default_credit_card_clients.csv
├── analysis/
│   └── exploratory_analysis.py
└── docs/
    └── phase1_report.pdf
```

## How to Run

```bash
# Clone the repo
git clone https://github.com/glizardx/credit-card-default-analysis.git
cd credit-card-default-analysis

# Install dependencies
pip install pandas matplotlib openpyxl

# Run the analysis
python analysis/exploratory_analysis.py
```

## Selected Features (11 columns)

| Column | Type | Description |
|--------|------|-------------|
| `LIMIT_BAL` | Numeric | Credit limit (NT$) |
| `SEX` | Nominal | 1 = Male, 2 = Female |
| `EDUCATION` | Ordinal | 1 = Grad school, 2 = University, 3 = High school, 4 = Other |
| `MARRIAGE` | Nominal | 1 = Married, 2 = Single, 3 = Other |
| `AGE` | Numeric | Age in years |
| `PAY_0` | Ordinal | Repayment status Sep/2005 (-2 to 8) |
| `PAY_2` | Ordinal | Repayment status Aug/2005 |
| `PAY_3` | Ordinal | Repayment status Jul/2005 |
| `BILL_AMT1` | Numeric | Bill statement Sep/2005 (NT$) |
| `PAY_AMT1` | Numeric | Previous payment Sep/2005 (NT$) |
| `default payment next month` | Nominal | Target — 0 = No default, 1 = Default |

## References

- Yeh, I. C., & Lien, C. H. (2009). *The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients.* Expert Systems with Applications, 36(2), 2473–2480.
- [UCI Dataset Page](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
- [Kaggle Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)

## Author

Guilherme — Data Analyst | PUCRS
