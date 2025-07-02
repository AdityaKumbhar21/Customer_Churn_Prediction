# 📉 Customer Churn Prediction


## Important Links
- [LIVE PROJECT LINK](https://customer-churn-prediction-ui.vercel.app/)
- Video Demo: [Click Here](https://drive.google.com/file/d/1UPpWe2N63nd7HFPZiYD0FUQ0tLajAC6t/view?usp=sharing)
- UI Code: [Click Here](https://github.com/AdityaKumbhar21/Customer_Churn_Prediction_UI)
- Blog Link: [Click Here](https://medium.com/@adityakumbhar915/predicting-customer-churn-a-deep-dive-into-preventing-customer-loss-808fde23177e)
- PPT Link: [Click Here](https://www.canva.com/design/DAGqxrdv3eY/kfacleE_9h_KqdHxgHdu4A/view?utm_content=DAGqxrdv3eY&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=ha3f93a78ab)


- [✨ Project Overview](#-project-overview)
- [❓ Problem Statement](#-problem-statement)
- [📊 Dataset](#-dataset)
- [🚀 Methodology & Pipeline](#-methodology--pipeline)
  - [1. Data Preprocessing](#1-data-preprocessing)
  - [2. Feature Engineering](#2-feature-engineering)
  - [3. Feature Selection](#3-feature-selection)
  - [4. Exploratory Data Analysis (EDA)](#4-exploratory-data-analysis-eda)
  - [5. Handling Class Imbalance](#5-handling-class-imbalance)
  - [6. Model Training & Evaluation](#6-model-training--evaluation)
  - [7. Hyperparameter Optimization (HPO)](#7-hyperparameter-optimization-hpo)
  - [8. Model Selection](#8-model-selection)
- [🎯 Key Findings & Model Performance](#-key-findings--model-performance)
- [🌐 Deployment](#-deployment)
- [🛠️ Technologies Used](#%EF%B8%8F-technologies-used)

---

## ✨ Project Overview

This project focuses on building a robust machine learning model to predict customer churn for a telecommunications company. By proactively identifying customers at high risk of churning, businesses can implement targeted retention strategies, reduce customer acquisition costs, and increase overall customer lifetime value. This repository contains the complete end-to-end data science workflow, from raw data to a deployed web application.

---

## ❓ Problem Statement

Customer churn is a significant challenge for businesses, directly impacting revenue and growth. The core problem addressed here is the **lack of foresight** into which customers are likely to discontinue their service. Without this insight, companies can only react to churn, often when it's too late. Our goal is to develop a predictive solution that enables **proactive intervention**, allowing the company to engage with at-risk customers *before* they leave, thereby mitigating potential revenue loss and improving customer satisfaction.

---

## 📊 Dataset

The dataset used for this project is the **Telco Customer Churn Dataset**, publicly available on Kaggle. It comprises:

* **7,043 rows** and **21 features**.
* **Customer demographics:** Gender, Senior Citizen, Partner, Dependents.
* **Account information:** Tenure, Contract Type, Payment Method, Monthly Charges, Total Charges.
* **Services information:** Phone Service, Multiple Lines, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies.
* **Target Variable:** `Churn` (Yes/No), indicating whether the customer left the company within the last month.

---

## 🚀 Methodology & Pipeline

Our project followed a structured data science pipeline to ensure data quality, effective modeling, and actionable insights.

### 1. Data Preprocessing

This crucial phase transformed raw data into a clean, model-ready format:
* **Handling Missing Values:** Identified and processed empty strings in `TotalCharges` by converting them to `NaN` and then imputing with `0` (assuming new customers had no initial charges).
* **Data Type Conversion:** Ensured `TotalCharges` was numeric (float), and other numerical features (`tenure`, `MonthlyCharges`) were correctly typed.
* **Feature Encoding:** Applied **One-Hot Encoding** (with `drop='first'`) to all categorical features to convert them into a numerical representation suitable for machine learning algorithms.
* **Feature Scaling:** Applied **Standard Scaling** to numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`) to normalize their ranges and prevent features with larger values from dominating the model.

### 2. Feature Engineering

A new feature, `tenure_group`, was engineered by binning the continuous `tenure` variable into meaningful categorical groups (e.g., '0-12', '12-24' months). This helped capture non-linear relationships and allowed the model to identify patterns across different stages of customer loyalty.

### 3. Feature Selection

To enhance model performance, prevent overfitting, and improve interpretability, we performed feature selection.
* We utilized **`SelectKBest`** from Scikit-learn.
* The **`f_classif` (ANOVA F-value)** statistical test was employed to assess the relationship between each feature and the target variable, selecting the top 'K' features with the strongest statistical association to churn.

### 4. Exploratory Data Analysis (EDA)

Comprehensive EDA was conducted to understand the dataset's characteristics and uncover key insights:
* **Churn Rate Distribution:** Identified an approximate 27% churn rate, highlighting a class imbalance.
* **Key Churn Drivers:** Visual analysis revealed higher churn rates among customers with:
    * Month-to-month contracts.
    * Fiber optic internet service.
    * Electronic check payment methods.
    * Shorter tenures.

### 5. Handling Class Imbalance

Given the significant class imbalance (73% 'No Churn' vs. 27% 'Churn'), which can bias models towards the majority class, we employed the **Synthetic Minority Over-sampling Technique (SMOTE)**. SMOTE generates synthetic samples for the minority class (churners) in the training data, effectively balancing the class distribution and ensuring the model learns adequately from both classes.

### 6. Model Training & Evaluation

A range of machine learning models were initially trained to establish baseline performance:
* **K-Nearest Neighbors (KNN)**
* **Random Forest**
* **Support Vector Machines (SVM)**
* **AdaBoost**
* **XGBoost Classifier**

We focused on the following metrics for evaluation, especially for the minority (churn) class, due to imbalance:
* **Precision:** Of all predicted churners, how many were correct?
* **Recall:** Of all actual churners, how many were correctly identified?
* **F1-Score:** The harmonic mean of Precision and Recall, providing a balanced measure.
* **Confusion Matrix:** Detail of True Positives, False Positives, True Negatives, and False Negatives.
* **Accuracy:** Overall correctness (though less reliable for imbalanced datasets).

### 7. Hyperparameter Optimization (HPO)

Based on their initial performance and robustness, **XGBoost Classifier and Support Vector Machines (SVM) were selected for in-depth Hyperparameter Optimization.** We used `RandomizedSearchCV` with `StratifiedKFold` cross-validation to efficiently search for optimal hyperparameters that maximized the F1-Score and Recall for the churn class.

### 8. Model Selection

After rigorous HPO, the **Support Vector Machine (SVM) model** emerged as the top performer for our churn prediction task.

Here's a comparison of the top models after HPO:

| Model                      | Accuracy | Precision (Churn) | Recall (Churn) | F1-Score (Churn) | False Positives (FP) | False Negatives (FN) | True Positives (TP) | True Negatives (TN) |
| :------------------------- | :------- | :---------------- | :------------- | :--------------- | :------------------- | :------------------- | :------------------ | :------------------ |
| **SVM (After HPO)** | **0.78** | **0.51** | **0.73** | **0.60** | 223                  | 88                   | 233                 | 858                 |
| XGBoost (After HPO)        | 0.78     | 0.51              | 0.65           | 0.57             | 198                  | 112                  | 209                 | 883                 |
| KNN                        | 0.79     | 0.54              | 0.64           | 0.58             | 178                  | 115                  | 206                 | 903                 |
| Random Forest              | 0.79     | 0.53              | 0.61           | 0.57             | 176                  | 124                  | 197                 | 905                 |
| AdaBoost                   | 0.78     | 0.51              | 0.63           | 0.56             | 195                  | 119                  | 202                 | 886                 |

**Reason for Choosing SVM:**
The SVM model achieved the highest **F1-Score (0.60)** and, critically, the highest **Recall (0.73)** for the churn class among all tested models. While its precision (0.51) was similar to XGBoost, its superior recall means it's better at identifying a larger proportion of actual churners. This ability to capture more at-risk customers is paramount for proactive retention strategies, making SVM the ideal choice for this project.

---

## 🎯 Key Findings & Model Performance

Our chosen SVM model successfully identified **233 customers** who were predicted to churn and actually did (True Positives). This capability provides critical foresight for the business.

By focusing retention efforts (e.g., special offers, personalized support) on these 233 high-risk individuals *before* they leave, companies can significantly improve their customer retention rates. This proactive approach directly translates to:
* **Reduced Customer Acquisition Costs:** It's often far cheaper to retain an existing customer than to acquire a new one.
* **Increased Customer Lifetime Value (CLTV):** Retaining customers for longer periods directly boosts their overall value to the company.
* **Improved Customer Satisfaction:** Proactive engagement can also improve satisfaction among customers who might have otherwise left.

---

## 🌐 Deployment

To make our predictive model accessible and usable, we've deployed it as a full-stack web application:

* **FastAPI Backend:** A robust and modern Python API built with **FastAPI** serves the model. It exposes a dedicated prediction endpoint: `/predict`.
    * **Pydantic Validation:** Leveraged **Pydantic** to ensure strict input data validation at the `/predict` endpoint, enhancing API reliability and preventing malformed requests.
    * **Internal Transformation:** The backend intelligently transforms raw input, such as converting `tenure` (numerical) to `tenure_group` (categorical), before passing data to the loaded ML pipeline.
* **ReactJS Frontend:** A dynamic and intuitive user interface built with **ReactJS** allows users to input customer details and receive real-time churn predictions.

The entire data preprocessing and model inference pipeline is encapsulated using `imblearn.pipeline.Pipeline` and saved with `joblib`, ensuring consistency and ease of deployment.

---

## 🛠️ Technologies Used

* **Python**
* **pandas**
* **numpy**
* **scikit-learn**
* **imblearn** (for SMOTE, ImbPipeline)
* **XGBoost**
* **FastAPI**
* **Pydantic**
* **joblib** (for model serialization)
* **ReactJS** (for Frontend)
* **Matplotlib** (for EDA visualizations)
* **Seaborn** (for EDA visualizations)

---

## 📁 Project Structure
