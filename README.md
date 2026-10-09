### Model Comparison and Selection

Three machine learning algorithms were evaluated: Logistic Regression, Random Forest, and XGBoost. Their performance was compared using accuracy, precision, recall, F1-score, and ROC-AUC.

| Metric | Logistic Regression | Random Forest | XGBoost |
|---|---:|---:|---:|
| Accuracy | 84.2% | **87.0%** | 85.3% |
| Precision | 84.8% | **86.8%** | 84.4% |
| Recall | 87.3% | **90.2%** | 90.2% |
| F1-score | 0.860 | **0.885** | 0.872 |
| ROC-AUC | 0.909 | **0.927** | 0.917 |

**Best Overall Model: Random Forest**

Random Forest achieved the highest accuracy, precision, F1-score, and ROC-AUC in the initial model comparison. It also matched XGBoost's recall of 90.2%, making it the strongest overall candidate among the three models for this experiment.

Because identifying positive cases was a priority, threshold tuning was subsequently performed on a validation set. At a threshold of 0.30, the final Random Forest model achieved 99.0% recall on the previously used test set, with 76.5% precision and 82.6% accuracy. This demonstrates the trade-off between detecting more positive cases and generating more false positives.

These results are preliminary and specific to this dataset and evaluation procedure. Further validation on independent data is required before drawing conclusions about real-world or clinical performance.
