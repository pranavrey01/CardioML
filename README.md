### Model Comparison and Selection

Three Machine Learning Algorithms: Logistic Regression, Random Forest and XGBoost were assessed. They were compared in terms of accuracy, precision, recall, F1-score and ROC-AUC.

| Metric | Logistic Regression | Random Forest | XGBoost |
|---|---:|---:|---:|
| Accuracy | 84.2% | **87.0%** | 85.3% |
| Precision | 84.8% | **86.8%** | 84.4% |
| Recall | 87.3% | **90.2%** | 90.2% |
| F1-score | 0.860 | **0.885** | 0.872 |
| ROC-AUC | 0.909 | **0.927** | 0.917 |

**Best Overall Model: Random Forest**

In the first model comparison, the highest accuracy, precision, F1 and ROC-AUC values were obtained by the Random Forest model. In addition, it also matched XGBoost's recall of 90.2%, which was the best of the three models in this experiment.

After the priority of identifying positive cases, tuning of thresholds was done on a validation set. The final Random Forest model had 76.5% precision, 82.6% accuracy and 99.0% recall on the test set used earlier with a threshold of 0.30. This shows that there is a trade-off between finding more positive cases and having more false positives.

These findings are preliminary and may only apply to this data and method of assessment. Conclusions on real world or clinical performance needs to be further validated with independent data.
