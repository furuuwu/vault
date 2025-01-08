When evaluating model performance on **imbalanced datasets**, traditional metrics like **accuracy** can be misleading. Instead, specialized metrics are used to better capture the model's performance on both the minority and majority classes. Here's a theoretical overview of these metrics, why they're useful, and their formulas:

---

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

### **Summary**
Different metrics highlight different aspects of model performance. For imbalanced datasets, **Precision, Recall, F1, PR-AUC, G-Mean, MCC, and Balanced Accuracy** are commonly recommended, as they provide a clearer picture of how well the model is handling the minority class while balancing the trade-offs with the majority class.


Here are the requested formulas in **LaTeX** syntax, formatted to render correctly in a Jupyter Notebook Markdown cell or an `.md` file. You can paste these directly into a Markdown cell or file to display them properly.

---

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

---

These LaTeX formulas will render beautifully in Jupyter Notebook or Markdown files. Let me know if you'd like help implementing them!
