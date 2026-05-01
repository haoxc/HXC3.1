---
aliases:
tags:
description:
type:
ref-url:
  - https://indersciencesubmissions.com/reviewerpeer/index.php?action=paperevalform&intSubmissionId=298740&intReveiwerAssignId=653915&intRevisionNumber=1&logStatus=0
create-date: 2026-04-29
---
1. Paper Summary
This paper proposes a comprehensive framework for financial risk prediction by integrating machine learning (ML) classifiers with novel metaheuristic optimization algorithms. The study treats risk assessment as a three-class supervised classification task (No Risk, Low Risk, and High Risk). It employs Extra Trees (ETC)and CatBoost (CATC) as base models, optimized via the Catch Fish Optimization Algorithm (CFOA) and the Dollmaker Optimization Algorithm (DOA). Through an analysis of 11 financial and device-level features, the study identifies the CACF (CatBoost + CFOA) hybrid model as the top performer, achieving an Accuracy of 0.9676 and an AUC of 0.9757. Additionally, a Copula-based sensitivity analysis identifies credit_score as the primary risk driver.

2. Overall Evaluation

Recommendation: Major Revision 

Reasoning: The research topic is highly relevant to contemporary financial risk management, particularly in the context of real-time monitoring and edge computing. The methodology is rigorous, covering data cleaning, hyperparameter optimization, and model interpretability. However, certain ambiguities regarding data processing and the quantification of real-time performance need to be addressed to strengthen the paper’s contribution.

---

3. Detailed Comments

A. Strengths

1. Methodological Innovation: The application of relatively new human-inspired optimizers (CFOA and DOA) to financial risk classification is a novel contribution. The resulting hybrid architectures demonstrate superior performance over standalone models.
2. Robust Validation: The use of Isolation Forest for outlier detection and 5-fold cross-validation ensures that the results are statistically reliable and less prone to overfitting.
3. Interpretability: By employing Copula Theory for sensitivity analysis, the authors move beyond "black-box" modeling, providing actionable insights into which factors (e.g., credit score) most significantly impact risk levels.
4. High-Risk Sensitivity: The proposed framework shows a significant improvement in the Recall of the "High Risk" category, which is critical for financial institutions to avoid costly systemic failures.

B. Areas for Improvement & Suggestions
1. Clarification of Data Consistency (Data Preprocessing):
    - On Page 4, the text states the dataset was downsized from 3,243 to 520 clean samples after Isolation Forest filtering. However, the end of Page 5 mentions that "no data were removed" after applying the same algorithm.
    - Suggestion: The authors must clarify this discrepancy. If 80%+ of the data was indeed removed, the authors should justify the representativeness of the remaining 520 samples and discuss potential small-sample bias.
2. Justification of Optimization Algorithms:
    - While CFOA and DOA are used, there is a lack of comparison against standard baseline optimizers such as Grid Search, Random Search, or Bayesian Optimization.
    - Suggestion: Briefly discuss why these specific metaheuristics were chosen and provide a comparison of their convergence speed or search efficiency relative to traditional methods.
3. Quantification of "Real-Time" Performance:
    - The paper emphasizes the system's suitability for "time-critical" and "real-time" financial situations, specifically mentioning edge devices like the Jetson Nano.
    - Suggestion: Include quantitative data on Inference Latency (e.g., milliseconds per transaction) for the various models to substantiate the claim that these complex hybrid models are feasible for real-time edge deployment.
4. Technical Presentation & Minor Errors:
    - Some figures (e.g., Figure 3 and Figure 5) require higher resolution for better legibility.
    - There are minor typographical errors (e.g., "performability" on Page 11).
    - Suggestion: Perform a final proofread for linguistic consistency and ensure all figures are exported at 300 DPI or higher.

---

4. Conclusion

This study provides a valuable application of business intelligence and data mining techniques to the financial sector. Addressing the concerns regarding data consistency and real-time quantification will significantly enhance the paper's impact and suitability for publication in the International Journal of Business Intelligence and Data Mining.

---