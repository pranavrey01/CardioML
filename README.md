### Cross-Source Generalization Evaluation

A source-based evaluation was carried out to determine if model performance varies depending on data source. AAll Cleveland records were held out for evaluation. The models were trained on records from Hungary, VA Long Beach, and Switzerland.
| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 73.4% | 68.6% | 77.0% | 0.725 | 0.832 |
| Random Forest | 73.4% | 67.3% | **81.3%** | 0.736 | 0.840 |
| XGBoost | **78.3%** | **76.6%** | 75.5% | **0.761** | **0.863** |

*Results*: In this cross-source experiment, XGBoost had the best accuracy, precision, F1 score and ROC-AUC values. Random Forest had the best performance in terms of the highest recall which means it was able to classify more cases as positive cases at the default classification threshold.

These results are contrary to the initial random-split comparison, where Random Forest was the best overall. This illustrates the effect that source of evaluation data has on model ranking.

*Limitations*: The test of generalization is limited to one held-out source. The results are of no clinical validity and do not guarantee results on other populations. Additional assessment with independent data, source-specific analysis and threshold selection on validation data from the training side is required.
