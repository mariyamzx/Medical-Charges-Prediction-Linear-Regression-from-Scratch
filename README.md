Predicting Medical Costs with Custom Linear Regression
This project focuses on building a Linear Regression model to predict medical insurance charges based on personal and lifestyle attributes such as age, gender, BMI, number of children, smoking status, and region. It involves complete data preprocessing, exploratory data analysis (EDA), model training, and evaluation — without using scikit-learn's LinearRegression implementation.

📁 Dataset
Source: insurance.csv

Features:

age: Age of the person

sex: Gender (male/female)

bmi: Body Mass Index

children: Number of children

smoker: Smoking status (yes/no)

region: Residential region

charges: Target variable – individual medical costs billed by health insurance

📊 Exploratory Data Analysis (EDA)
Performed visual and statistical analysis to understand feature relationships:

Histograms for continuous feature distribution

Bar plots of categorical features vs charges

Boxplots to detect outliers

Correlation heatmap

Pairplots for selected numerical features

Insights:

Smokers have significantly higher insurance charges

Charges increase with age and BMI

Number of children has little impact

Charges are right-skewed, with some extreme values

🧹 Data Preprocessing
No missing values

Categorical encoding using OneHotEncoder

Optional scaling with StandardScaler

Binning applied to age (if explored)

Considered log-transformation of the target variable for skew correction

🧠 Model Training
Algorithm: Linear Regression implemented from scratch

Built the Linear Regression model manually using NumPy (no use of sklearn.linear_model.LinearRegression)

Calculated weights using the closed-form equation:

𝑤
=
(
𝑋
⊤
𝑋
)
−
1
𝑋
⊤
𝑦
w=(X 
⊤
 X) 
−1
 X 
⊤
 y
Train/Test Split: 80/20

📈 Model Evaluation
Metrics:

R² Score

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

Visualized predictions vs actual values

Compared performance on train and test sets

📌 Additional Analysis
Extracted and interpreted model coefficients manually

Explored feature importance

Checked if there's overfitting or underfitting

Cross-validation for robustness

🛠️ Tech Stack
Python

pandas, numpy

seaborn, matplotlib

Manual implementation of algorithms without scikit-learn's modeling


📚 References
Kaggle Dataset

 Author
Mariyam Muzammil
📎 @mariyamzx
