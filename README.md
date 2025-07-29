 Predicting Medical Costs with Custom Linear Regression
This project focuses on building a Linear Regression model from scratch to predict medical insurance charges based on personal and lifestyle attributes such as age, gender, BMI, number of children, smoking status, and region.

It includes complete data preprocessing, exploratory data analysis (EDA), manual model training, and evaluation — all without using scikit-learn's LinearRegression.

📁 Dataset Source
insurance.csv

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

📈 Histograms for continuous feature distribution

📊 Bar plots of categorical features vs. charges

📦 Boxplots to detect outliers

🔥 Correlation heatmap

🔗 Pairplots for selected numerical features

🔍 Key Insights:
Smokers have significantly higher insurance charges

Charges increase with age and BMI

Number of children has little impact

Charges are right-skewed, with some extreme values

🧹 Data Preprocessing
No missing values

Categorical encoding using OneHotEncoder

Optional scaling with StandardScaler

Binning applied to age (if explored)

Log transformation considered for skew correction on target (charges)

🧠 Model Training
Algorithm: Linear Regression implemented manually using NumPy

No use of sklearn.linear_model.LinearRegression

Weights calculated using the closed-form solution:

𝑤
=
(
𝑋
𝑇
𝑋
)
−
1
𝑋
𝑇
𝑦


Train/Test Split: 80/20

📈 Model Evaluation
Metrics:
R² Score

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

📉 Visualized predictions vs. actual values
🔍 Compared performance on training and test sets

📌 Additional Analysis
Extracted and interpreted model coefficients manually

Explored feature importance

Evaluated for overfitting/underfitting

Performed cross-validation for robustness

🛠️ Tech Stack
Python

pandas, numpy

seaborn, matplotlib

Manual algorithm implementation (No scikit-learn for modeling)

📚 References
Kaggle - Medical Cost Personal Datasets

👩‍💻 Author
Mariyam Muzammil
📎 @mariyamzx
