# Simple Linear Regression

# Importing the libraries
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    # Importing the dataset (resolve path relative to this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Salary_Data.csv")
    dataset = pd.read_csv(csv_path)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=1 / 3, random_state=0
    )

    # Feature Scaling (not needed for simple linear regression)
    # from sklearn.preprocessing import StandardScaler
    # sc_X = StandardScaler()
    # X_train = sc_X.fit_transform(X_train)
    # X_test = sc_X.transform(X_test)

    # Fitting Simple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)

    # Visualising the Training set results
    plt.scatter(X_train, y_train, color="red")
    plt.plot(X_train, regressor.predict(X_train), color="blue")
    plt.title("Salary vs Experience (Training set)")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.show()

    # Visualising the Test set results
    plt.scatter(X_test, y_test, color="red")
    plt.plot(X_train, regressor.predict(X_train), color="blue")
    plt.title("Salary vs Experience (Test set)")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.show()


if __name__ == "__main__":
    main()
