# Hotel Booking Cancellation Prediction

## Project Overview

This project aims to predict whether a hotel booking will be canceled by a customer based on historical booking data.  
The main objective is to provide actionable insights to hotel management to reduce cancellations and optimize occupancy.

**Author:** Jesus Alejandro Murillo Perez  
---

## Dataset

The dataset contains historical booking information, including:

- Customer details
- Booking dates
- Room type reserved and assigned
- Number of adults, children, and other relevant features
- Target variable: `is_canceled` (1 if the booking was canceled, 0 otherwise)

*Note: A sample CSV with the same structure is provided for demonstration purposes.*
---

## Features and Preprocessing

- Categorical variables are encoded using **OneHotEncoder**, except `country` which is encoded using **TargetEncoder** due to high cardinality.  
- Numeric variables are scaled using **StandardScaler** for consistency across models.  
- Date features are decomposed into `year`, `month`, and `day`.  
- A derived feature `room_assigned_correctly` indicates whether the assigned room matches the reserved room.  
- Features that represent future information (`reservation_status`) are removed to prevent data leakage.

---

## Models

Two models were trained and evaluated:

1. **Logistic Regression**
   - Final hyperparameters: `C=10`, `penalty='l2'`, `solver='newton-cg'`
   - Achieved very high metrics (F1, Accuracy, Precision, Recall, ROC AUC > 0.93)
   - Selected as the final model

2. **Random Forest**
   - Used for comparison purposes
   - Slightly lower metrics but required fewer features

---

## Evaluation

The models were evaluated using:

- **F1 Score**
- **Accuracy**
- **Precision**
- **Recall**
- **ROC AUC**

Visualizations include:

- **ROC Curve**
- **Precision-Recall Curve**
- **Confusion Matrix**

**Insights:** The Logistic Regression model captures nearly all cancellations, allowing hotel staff to proactively target high-risk customers.

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hotel_booking_cancellation.git
