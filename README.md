# Simple Linear Regression

Predict employee salary from years of experience using ordinary least squares linear regression.

## Overview

Fits the classic model **y = b₀ + b₁x** where *x* is years of experience and *y* is salary. The dataset is split 2:1 into training and test sets, a `LinearRegression` model is trained, and results are visualised for both splits.

Implementations are provided in both Python and R.

## Dataset

`Salary_Data.csv` — 30 observations with two columns:

| Column | Description |
|---|---|
| `YearsExperience` | Years of professional experience |
| `Salary` | Annual salary (USD) |

## 🛠 Tech Stack

| | Tool | Purpose |
|---|---|---|
| 🐍 | Python 3 | Primary implementation |
| 📊 | scikit-learn | `LinearRegression`, `train_test_split` |
| 🔢 | NumPy / pandas | Data handling |
| 📈 | Matplotlib | Visualisation |
| 📉 | R | Alternative implementation |
| 🎨 | ggplot2 | R visualisation |

## Getting Started

### Python

```bash
pip install -r requirements.txt
python simple_linear_regression.py
```

### R

```r
# Install dependencies (first time only)
install.packages(c("caTools", "ggplot2"))

# Run
source("simple_linear_regression.R")
```

## ⚠️ Known Issues

- The dataset is small (30 rows), so model generalisation is limited.
- Plots use `plt.show()` which requires a display; run headless with `matplotlib.use("Agg")` if needed.
