# 📈 Sales Prediction Using Machine Learning

# 🏆 Oasis Infobyte Internship Task

This project was completed as part of the **Oasis Infobyte Data Science Internship Program (OIBSIP)**.

### Task Details

| Field | Details |
|--------|---------|
| Internship Program | Oasis Infobyte Data Science Internship (OIBSIP) |
| Task Number | Task 5 |
| Task Name | Sales Prediction Using Python |
| Domain | Machine Learning Regression |
| Model Type | Supervised Learning |
| Algorithm | Linear Regression |
| Deployment | Streamlit Dashboard |

---

## 📌 Project Overview

This project focuses on predicting product sales based on advertising expenditures across different marketing channels such as **TV**, **Radio**, and **Newspaper**.

The objective is to analyze the relationship between advertising budgets and sales performance, identify the most influential advertising channel, and build a machine learning model capable of forecasting future sales.

The project includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Selection
- Linear Regression Model Building
- Model Evaluation
- Interactive Streamlit Dashboard

---

## 🚀 Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Correlation analysis using heatmaps
- Advertising channel impact analysis
- Linear Regression model training
- Sales prediction based on user inputs
- Model evaluation using MAE, RMSE, and R² Score
- Interactive Streamlit dashboard for real-time predictions
- Modern visualizations using Plotly

---

## 📂 Dataset Information

The dataset contains advertising budgets spent on different media channels and corresponding sales figures.

| Feature | Description |
|----------|-------------|
| TV | Advertising budget spent on TV |
| Radio | Advertising budget spent on Radio |
| Newspaper | Advertising budget spent on Newspaper |
| Sales | Product sales (Target Variable) |

### 🎯 Target Variable

```text
Sales
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit
- Pickle

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Missing Value Analysis
- Duplicate Record Check
- Correlation Heatmap
- Sales Distribution Analysis
- TV vs Sales Relationship
- Radio vs Sales Relationship
- Newspaper vs Sales Relationship

### 🔍 Key Findings

✅ TV advertising has the strongest impact on sales.

✅ Radio advertising also contributes significantly.

✅ Newspaper advertising has relatively weak influence.

✅ Strong positive correlation exists between TV advertising and sales.

---

## 🤖 Machine Learning Model

### Algorithm Used

```text
Linear Regression
```

### Why Linear Regression?

Linear Regression is suitable because the target variable (**Sales**) is continuous and the dataset exhibits a strong linear relationship between advertising expenditure and sales.

---

## 📈 Model Evaluation Metrics

The model was evaluated using:

| Metric | Purpose |
|----------|----------|
| MAE (Mean Absolute Error) | Average prediction error |
| RMSE (Root Mean Squared Error) | Measures prediction accuracy |
| R² Score | Explains model performance |

### Performance Summary

The Linear Regression model achieved a high R² Score, indicating that the advertising budgets explain a significant portion of the variation in sales.

---

## 💡 Example Prediction

| TV Budget | Radio Budget | Newspaper Budget | Predicted Sales |
|------------|-------------|------------------|----------------|
| 230 | 37 | 69 | 22.5 |
| 150 | 20 | 15 | 14.3 |
| 80 | 10 | 5 | 8.9 |

> *Values may vary depending on model training and test split.*

---

## 📊 Dashboard Features

The Streamlit Dashboard includes:

- Interactive Budget Sliders
- Real-Time Sales Prediction
- KPI Cards
- Correlation Heatmap
- Scatter Plots
- Business Insights Section
- Modern Dark Theme Interface

---

## 📁 Project Structure

```text
SalesPredictionProject/
│
├── Advertising.csv
├── Sales_Prediction.ipynb
├── sales_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
python -m streamlit run app.py
```

---

## 🎯 Business Impact

This project helps businesses:

- Predict future sales based on advertising budgets.
- Identify the most effective marketing channel.
- Optimize advertising spending.
- Improve marketing decision-making through data-driven insights.

---

## 👩‍💻 Author

**Diya Kapadia**  
Computer Science Student  
Machine Learning & Data Science Enthusiast

---

## ⭐ Acknowledgements

This project was developed as part of the **Oasis Infobyte Data Science Internship Program (OIBSIP)** and demonstrates the practical application of Machine Learning, Data Analysis, and Data Visualization techniques for business decision-making.
