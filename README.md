# 📈 Simple Linear Regression — Salary Prediction

A beginner-friendly machine learning project that predicts employee salary based on years of experience using Simple Linear Regression, implemented in both Python and R.

## 📖 Description

This project demonstrates the most fundamental supervised learning algorithm — **Simple Linear Regression** — applied to a real-world salary dataset. Given an employee's years of experience, the model learns the linear relationship and predicts their expected salary.

**Mathematical Model:**

```
y = b₀ + b₁x
```

Where:
- `y` = predicted salary
- `b₀` = intercept (base salary)
- `b₁` = coefficient (salary increase per year of experience)
- `x` = years of experience

## 🔬 Methodology

1. **Data Exploration** — Scatter plot visualization to confirm a linear relationship between experience and salary
2. **Data Splitting** — Dataset split into training (2/3) and test (1/3) sets
3. **Model Training** — Fit a linear regression model on the training data
4. **Prediction** — Predict salaries on the unseen test set
5. **Visualization** — Plot regression line against both training and test data to evaluate fit

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python 3 | Primary implementation |
| 📊 R | Alternative implementation |
| 🔢 NumPy | Numerical computing |
| 🐼 pandas | Data loading and manipulation |
| 📉 matplotlib | Plotting (Python) |
| 📈 ggplot2 | Plotting (R) |
| 🤖 scikit-learn | ML model and train/test split |
| 📦 caTools | Train/test split (R) |

## 📋 Dependencies

### Python

```
numpy
pandas
matplotlib
scikit-learn
```

### R

```
caTools
ggplot2
```

## 🚀 How to Run

### Python

```bash
# Install dependencies
pip install numpy pandas matplotlib scikit-learn

# Run the script
python simple_linear_regression.py
```

### R

```r
# Install packages (first time only)
install.packages("caTools")
install.packages("ggplot2")

# Run the script
Rscript simple_linear_regression.R
```

## 📁 Dataset

`Salary_Data.csv` contains 30 observations with two columns:

| Column | Description |
|--------|-------------|
| `YearsExperience` | Number of years of professional experience |
| `Salary` | Annual salary in USD |

## ⚠️ Known Issues

- The dataset is small (30 samples), so the model may not generalize well to broader populations
- No feature scaling is applied (commented out in code) — not strictly necessary for single-feature linear regression, but may matter in extended use cases
- Plots display sequentially in Python (`plt.show()` blocks); close each window to see the next
- The R script must be run from the directory containing `Salary_Data.csv` (same applies to Python)

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
