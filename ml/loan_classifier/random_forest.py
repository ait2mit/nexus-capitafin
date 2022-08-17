import joblib
import pandas as pd
import os

# print("ls",ls ../../)
class RandomForestClassifier:
    def __init__(self):
        curr_wd = os.getcwd()
        path_to_artifacts = curr_wd + "/ml-model-dev/loan-model/final-model-artifacts/"
        self.values_fill_missing = joblib.load(path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest_model.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        input_data.fillna(self.values_fill_missing)

        print("input coming:", input_data)

        # convert categoricals
        # cat_var = [c for c in input_data.columns if input_data[c].dtype=='object']
        cat_var = [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "Property_Area",
        ]
        for column in cat_var:

            print("columns", column)
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])

        return input_data

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def postprocessing(self, input_data):
        label = "N"
        if input_data[1] > 0.5:
            label = "Y"
        return {"probability": input_data[1], "label": label, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction
