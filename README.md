# 🧠 Predicting Medical Costs with Custom Linear Regression

This project focuses on building a **Linear Regression model from scratch** to predict **medical insurance charges** based on personal and lifestyle attributes such as **age**, **gender**, **BMI**, **number of children**, **smoking status**, and **region**.

It includes complete **data preprocessing**, **exploratory data analysis (EDA)**, **manual model training**, and **evaluation** — all **without using scikit-learn's LinearRegression**.

---

## 📁 Dataset Source

`insurance.csv`

### Features:
- `age`: Age of the person  
- `sex`: Gender (male/female)  
- `bmi`: Body Mass Index  
- `children`: Number of children  
- `smoker`: Smoking status (yes/no)  
- `region`: Residential region  
- `charges`: Target variable – individual medical costs billed by health insurance  

---

## 📊 Exploratory Data Analysis (EDA)

Performed **visual and statistical analysis** to understand feature relationships:

- 📈 Histograms for continuous feature distribution  
- 📊 Bar plots of categorical features vs. `charges`  
- 📦 Boxplots to detect outliers  
- 🔥 Correlation heatmap  
- 🔗 Pairplots for selected numerical features  

### 🔍 Key Insights:
- Smokers have **significantly higher** insurance charges  
- Charges **increase with age** and **BMI**  
- Number of children has **little impact**  
- Charges are **right-skewed**, with some extreme values  

---

## 🧹 Data Preprocessing

- No missing values  
- Categorical encoding using `OneHotEncoder`  
- Optional scaling with `StandardScaler`  
- **Binning** applied to `age` (if explored)  
- **Log transformation** considered for skew correction on target (`charges`)  

---

## 🧠 Model Training

- **Algorithm**: Linear Regression implemented **manually** using **NumPy**  
- No use of `sklearn.linear_model.LinearRegression`  
- Weights calculated using the **closed-form solution**:  
 
  **w = (Xᵀ X)⁻¹ Xᵀ y**
  

- **Train/Test Split**: 80/20  

---

## 📈 Model Evaluation

### Metrics:
- R² Score  
- Root Mean Squared Error (RMSE)  
- Mean Absolute Error (MAE)  

📉 Visualized **predictions vs. actual values**  
🔍 Compared performance on **training and test sets**  

---

## 📌 Additional Analysis

- Extracted and interpreted **model coefficients** manually  
- Explored **feature importance**  
- Evaluated for **overfitting/underfitting**  
- Performed **cross-validation** for robustness  

---

## 🚀 Streamlit Web App

A **Streamlit app** is included to interactively predict insurance costs based on user inputs.

### ▶️ How to Run

```bash
streamlit run app/main.py
Enter input values (age, gender, BMI, children, smoker status, region) and receive predicted charges instantly.

📦 Installation
Install all dependencies:


pip install -r requirements.txt
requirements.txt includes:

numpy==2.3.2
pandas==2.3.1
streamlit==1.47.1
scikit-learn==1.7.1
seaborn==0.13.2
matplotlib==3.10.3
🗂️ Project Structure

insurance/
├── app/
│   ├── LinearReg.py         # Custom linear regression class
│   └── main.py              # Streamlit app entry point
├── .streamlit/
│   └──config.toml
├── insurance.csv            # Dataset
├── insurance_pipeline.pkl   # Saved preprocessed pipeline
├── notebook(2).ipynb
├── requirements.txt
└── README.md


🛠️ Tech Stack
Python

numpy, pandas

seaborn, matplotlib

streamlit

Manual model implementation (no sklearn for modeling)

📚 References
Kaggle - Medical Cost Personal Datasets

👩‍💻 Author
Mariyam Muzammil
📎 @mariyamzx