from io import StringIO
from typing import List

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

feature_cols: List[str] = [
    "Age",
    "REM sleep percentage",
    "Deep sleep percentage",
    "Light sleep percentage",
    "Awakenings",
    "Alcohol consumption",
    "Smoking status",
    "Exercise frequency",
]

response_col: str = "Sleep efficiency"


class Model:
    def __init__(self, csv_str):
        self.data = pd.read_csv(StringIO(csv_str))
        # Assign numerical values to categorical data
        self.data["Gender"] = self.data["Gender"].map({"Male": 1, "Female": 0})
        self.data["Smoking status"] = self.data["Smoking status"].map(
            {"Yes": 1, "No": 0}
        )

        # Remove rows with missing values
        self.data.dropna(inplace=True)
        self.X = self.data[feature_cols]
        self.y = self.data[response_col]
        self.fit()

    def fit(self):
        self.regressor = LinearRegression()
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.3, random_state=42
        )

        self.regressor.fit(X_train, y_train)

    def predict(self, x):
        """Predicts one set of input"""
        return self.regressor.predict(
            pd.DataFrame(
                x,
                index=[0],
            )
        ).tolist()[0]
