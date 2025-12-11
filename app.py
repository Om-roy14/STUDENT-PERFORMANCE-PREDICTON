from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load pre-trained model and preprocessor (from your notebook)
with open("risk_models.pkl", "rb") as f:
    risk_model = pickle.load(f)

with open("preprocessors.pkl", "rb") as f:
    preprocessor = pickle.load(f)

# Load column names from training
x_risk_columns = pickle.load(open("x_risk_columns.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Extract form data
    input_data = [[
        request.form["Gender"],
        int(request.form["Age"]),
        request.form["Department"],
        float(request.form["attendance"]),
        float(request.form["midterm"]),
        float(request.form["final"]),
        float(request.form["assignments"]),
        float(request.form["quizzes"]),
        float(request.form["participation"]),
        float(request.form["projects"]),
        float(request.form["total"]),
        float(request.form["study_hours"]),
        request.form["extracurricular_activities"],
        request.form["internet_access"],
        request.form["parent_education"],
        request.form["family_income"],
        int(request.form["stress_level"]),
        float(request.form["sleep_hours"]),
    ]]

    # Convert to DataFrame with correct columns
    df_input = pd.DataFrame(input_data, columns=x_risk_columns)

    # Preprocess
    processed = preprocessor.transform(df_input)

    # Predict
    prediction = risk_model.predict(processed)[0]
    result = "At Risk" if prediction else "Not At Risk"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
