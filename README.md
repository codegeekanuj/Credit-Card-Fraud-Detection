# Credit Card Fraud Detection

**Author:** Anuj Tripathi  
**Project type:** Machine learning — imbalanced classification & anomaly detection

Detect fraudulent credit card transactions using the [ULB MLG creditcard fraud dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud). The data covers two days of European cardholder activity (September 2013): **492 frauds** out of **284,807** transactions (~**0.17%** positive class).

![Project visuals](images/basket.jpg)

## What this repo contains

| Path | Description |
|------|-------------|
| `notebooks/01_exploratory_analysis.ipynb` | EDA, preprocessing, baseline classifiers |
| `notebooks/02_crisp_dm_pipeline.ipynb` | Full CRISP-DM workflow (SMOTE, tuning, evaluation) |
| `PyOD/fraud_credit.py` | PyOD outlier-detection comparison on Amount vs Class |
| `PyOD/CreditCardFraud.ipynb` | Notebook version of PyOD experiments |
| `data/` | Place `creditcard.csv` here (not committed — see below) |
| `images/` | Plots and figures used in reports |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Dataset

1. Download from [Kaggle — Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud).
2. Extract and save as **`data/creditcard.csv`**.

Notebooks and scripts load the file via `src/paths.py` so paths stay consistent from any working directory.

## Approach (summary)

- **Exploratory analysis:** class imbalance, amount/time patterns, correlation structure.
- **Supervised models:** logistic regression, SVM, k-NN, trees, random forest, SGD — with **SMOTE** and stratified validation; metrics emphasize **recall**, **F1**, and **MCC** for fraud.
- **Unsupervised / anomaly view:** PyOD (Isolation Forest, LOF, KNN variants, etc.) on scaled features.

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgements

Public dataset by Dal Pozzolo et al. (ULB). Initial notebook structure was adapted from open-source fraud-detection examples and reworked for this portfolio project.
