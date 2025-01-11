# imbalanced datasets (GPT)

## metrics

When evaluating model performance on **imbalanced datasets**, traditional metrics like **accuracy** can be misleading. Instead, specialized metrics are used to better capture the model's performance on both the minority and majority classes. Here's a theoretical overview of these metrics, why they're useful, and their formulas:

### **1. Precision**

- **Definition**: Measures how many of the predicted positive instances are actually positive.

- **Formula**:
  $$
  \text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Positives (FP)}}
  $$
- **Why it's useful**:
  - High precision means fewer false alarms (i.e., fewer false positives).
  - Particularly important when the cost of false positives is high (e.g., spam filtering).

---

### **2. Recall (Sensitivity, True Positive Rate)**

- **Definition**: Measures how many of the actual positive instances the model correctly identified.
- **Formula**:
  $$
  \text{Recall} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Negatives (FN)}}
  $$
- **Why it's useful**:
  - High recall means the model identifies most positive instances.
  - Important when the cost of missing positives is high (e.g., detecting diseases).

---

### **3. F1 Score**

- **Definition**: The harmonic mean of precision and recall. Balances both metrics.
- **Formula**:
  $$
  F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
  $$
- **Why it's useful**:
  - Provides a single metric to balance precision and recall.
  - Best used when there's a trade-off between precision and recall, and both are important.

---

### **4. Area Under the Curve (AUC) - ROC**

- **Definition**: Measures the area under the Receiver Operating Characteristic (ROC) curve, which plots **True Positive Rate (TPR)** against **False Positive Rate (FPR)** at various thresholds.
- **Formula for TPR and FPR**:
  $$
  \text{TPR} = \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
  $$
  $$
  \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}
  $$
- **Why it's useful**:
  - Indicates how well the model separates classes across all thresholds.
  - AUC closer to 1 indicates better performance.
  - Useful for binary classification problems with imbalanced data.

---

### **5. Precision-Recall AUC (PR-AUC)**

- **Definition**: The area under the Precision-Recall curve, which plots precision against recall at various thresholds.
- **Why it's useful**:
  - Focuses on the positive (minority) class.
  - Provides a better evaluation for imbalanced datasets compared to ROC-AUC.

---

### **6. Geometric Mean (G-Mean)**

- **Definition**: The square root of the product of sensitivity (recall) and specificity.
- **Formula**:
  $$
  \text{G-Mean} = \sqrt{\text{Sensitivity} \cdot \text{Specificity}}
  $$
  Where:
  $$
  \text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}
  $$
- **Why it's useful**:
  - Balances performance on both positive and negative classes.
  - Useful for ensuring the model performs well on the minority class without overly sacrificing performance on the majority class.

---

### **7. Matthews Correlation Coefficient (MCC)**

- **Definition**: Measures the quality of binary classifications, considering true and false positives and negatives.
- **Formula**:
  $$
  \text{MCC} = \frac{(\text{TP} \cdot \text{TN}) - (\text{FP} \cdot \text{FN})}{\sqrt{(\text{TP} + \text{FP})(\text{TP} + \text{FN})(\text{TN} + \text{FP})(\text{TN} + \text{FN})}}
  $$
- **Why it's useful**:
  - Balanced metric even for imbalanced datasets.
  - Values range from -1 (worst) to +1 (perfect correlation).

---

### **8. Balanced Accuracy**

- **Definition**: The average of recall for both classes.
- **Formula**:
  $$
  \text{Balanced Accuracy} = \frac{\text{Sensitivity} + \text{Specificity}}{2}
  $$
- **Why it's useful**:
  - Accounts for imbalanced datasets by equally weighing positive and negative classes.

---

### **9. Brier Score**

- **Definition**: Measures the accuracy of predicted probabilities.
- **Formula**:
  $$
  \text{Brier Score} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{p}_i)^2
  $$
  Where:
  - $ y_i $ is the actual label (0 or 1).
  - $ \hat{p}_i $ is the predicted probability of the positive class.
- **Why it's useful**:
  - Penalizes models for poorly calibrated probabilities.
  - Lower values indicate better-calibrated models.

---

### **Choosing Metrics Based on Use Case**

- **High class imbalance**:
  - Precision, Recall, F1, PR-AUC, and G-Mean are most relevant.
- **Equal importance of both classes**:
  - ROC-AUC, Balanced Accuracy, and MCC are useful.
- **Probability calibration required**:
  - Brier Score.

## metrics - formulas

### Sensitivity (Recall or True Positive Rate)

$$
\text{Sensitivity} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Negatives (FN)}}
$$

---

### Specificity (True Negative Rate)

$$
\text{Specificity} = \frac{\text{True Negatives (TN)}}{\text{True Negatives (TN)} + \text{False Positives (FP)}}
$$

---

### Precision (Positive Predictive Value)

$$
\text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Positives (FP)}}
$$

---

### F1 Score

$$
F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

---

### Geometric Mean (G-Mean)

$$
\text{G-Mean} = \sqrt{\text{Sensitivity} \cdot \text{Specificity}}
$$

---

### Balanced Accuracy

$$
\text{Balanced Accuracy} = \frac{\text{Sensitivity} + \text{Specificity}}{2}
$$

---

### Area Under the Curve (AUC) for ROC

$$
\text{AUC}_{\text{ROC}} = \int_0^1 \text{TPR}(\text{FPR}) \, d(\text{FPR})
$$

Where:

- **TPR** = True Positive Rate
- **FPR** = False Positive Rate

---

### Brier Score

$$
\text{Brier Score} = \frac{1}{N} \sum_{i=1}^N \left( y_i - \hat{y}_i \right)^2
$$

Where:

- $ y_i $ = True label ($0$ or $1$)
- $\hat{y}_i $ = Predicted probability for the positive class

---

### Matthews Correlation Coefficient (MCC)

$$
\text{MCC} = \frac{\text{TP} \cdot \text{TN} - \text{FP} \cdot \text{FN}}{\sqrt{(\text{TP} + \text{FP})(\text{TP} + \text{FN})(\text{TN} + \text{FP})(\text{TN} + \text{FN})}}
$$

---

### Log Loss (Binary Crossentropy)

$$
\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

## metrics - comparison

Accuracy is often a poor metric for evaluating models on imbalanced datasets because it does not account for the distribution of class labels. Here’s the reasoning behind this and alternative metrics to avoid in such scenarios:

### **Why Accuracy is a Poor Metric**

Accuracy measures the proportion of correctly classified instances:

\[
\text{Accuracy} = \frac{\text{True Positives (TP)} + \text{True Negatives (TN)}}{\text{Total Samples}}
\]

In imbalanced datasets, the majority class dominates the dataset. As a result:

- A model that predicts only the majority class can still achieve a high accuracy, even if it completely ignores the minority class.
- For example, if 95% of the samples belong to Class A and only 5% belong to Class B:
  - A model that predicts Class A for all samples will have an accuracy of 95%, but it provides no meaningful insights into detecting Class B.

---

### **Other Metrics That Are Problematic for Imbalanced Datasets**

1. **Precision Alone**
   - Precision measures the proportion of true positives among predicted positives:
     $$
     \text{Precision} = \frac{\text{TP}}{\text{TP + FP}}
     $$
   - Problem: Precision focuses only on the positive predictions and ignores false negatives, making it insufficient when the minority class is under-represented.

2. **Recall Alone**
   - Recall (or Sensitivity) measures the proportion of true positives out of the actual positives:
     \[
     \text{Recall} = \frac{\text{TP}}{\text{TP + FN}}
     \]
   - Problem: While recall captures the ability to identify positive instances, it does not penalize a high number of false positives, which can be common in imbalanced datasets.

3. **Specificity Alone**
   - Specificity measures the proportion of true negatives among all actual negatives:
     \[
     \text{Specificity} = \frac{\text{TN}}{\text{TN + FP}}
     \]
   - Problem: Like accuracy, specificity can be high for imbalanced datasets if the majority class dominates the negatives.

---

### **Better Metrics for Imbalanced Datasets**

1. **F1 Score**
   - The harmonic mean of precision and recall:
     \[
     \text{F1 Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
     \]
   - Why it’s better: The F1 score balances precision and recall, which is particularly useful when there is a class imbalance.

2. **Area Under the Receiver Operating Characteristic (ROC-AUC) Curve**
   - Measures the model’s ability to discriminate between classes across different thresholds.
   - Why it’s better: It considers the trade-off between true positive rate (recall) and false positive rate, providing a more nuanced evaluation.

3. **Area Under the Precision-Recall (PR-AUC) Curve**
   - Focuses on precision and recall across thresholds.
   - Why it’s better: It is particularly effective when the dataset is highly imbalanced, as it gives more weight to the minority class.

4. **Cohen's Kappa**
   - Measures the agreement between predicted and actual labels, adjusted for chance:
     \[
     \text{Kappa} = \frac{\text{Accuracy} - \text{Expected Accuracy}}{1 - \text{Expected Accuracy}}
     \]
   - Why it’s better: It accounts for imbalances in the dataset.

5. **Balanced Accuracy**
   - An average of recall for each class:
     \[
     \text{Balanced Accuracy} = \frac{\text{Sensitivity} + \text{Specificity}}{2}
     \]
   - Why it’s better: It gives equal importance to both classes, regardless of their representation.

6. **G-Mean (Geometric Mean)**
   - The square root of the product of sensitivity and specificity:
     \[
     \text{G-Mean} = \sqrt{\text{Sensitivity} \cdot \text{Specificity}}
     \]
   - Why it’s better: It balances performance on both classes.
