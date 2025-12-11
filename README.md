Student At-Risk Prediction

This repository provides all the necessary components to run a machine-learning system that predicts whether a student is at academic risk. The project includes preprocessing objects, a trained prediction model, column definitions, and a ready-to-use HTML interface.

Repository Contents

1. preprocessors.pkl
Contains the preprocessing pipeline used during model training. This may include encoding of categorical variables, scaling of numerical values, and column transformations. It ensures that new input data is processed in the exact same way as the training data.

2. risk_models.pkl
The saved machine-learning model responsible for predicting whether a student is at risk. This file may contain a single model or a dictionary of models, depending on how the system was trained.

3. x_risk_columns.pkl
Stores the exact list and ordering of input features expected by the model. Consistent column structure is required for accurate predictions.

4. index.html
A simple front-end interface that collects student information and sends it for prediction. It includes fields such as gender, age, department, attendance, exam scores, study habits, extracurricular activities, internet access, family background, stress levels, and sleep patterns.

How the System Works

User Inputs Data
Through the HTML interface or another data source, user-submitted information is collected using predefined fields.

Preprocessing
The data is passed through the preprocessing pipeline to match the structure and format used during training.

Model Prediction
The transformed data is sent to the trained model, which outputs a label indicating whether the student is at academic risk.
Some models may also provide probability scores.

Result Display
The prediction is returned and can be displayed in the web interface, console, or an API response.

Feature Overview

The model expects the following types of inputs:

Demographic: Gender, Age, Department

Academic performance: Attendance, Midterm score, Final score, Assignments, Quizzes, Participation, Projects, Total marks

Lifestyle & behavior: Study hours, Sleep hours, Stress levels

Background factors: Extracurricular activities, Internet access, Parent education, Family income

These features collectively help assess whether a student may be at risk academically.

Deployment Notes

Ensure that all three files — preprocessing pipeline, model, and column list — remain synchronized.

Inputs must match the expected column names and types for accurate predictions.

The HTML interface can be integrated with any backend (Flask, FastAPI, Node, etc.) that loads the model and returns predictions.

Avoid modifying the model or preprocessor files unless retraining the system.

Security Considerations

Pickle files can execute code when loaded; only use files from trusted sources.

Do not expose model files publicly if they contain sensitive training data or internal configurations.

Sanitize and validate user inputs before feeding them into the model.

Purpose

This project helps institutions or educators:

Identify students who may need academic support

Analyze patterns behind performance issues

Provide early interventions to improve outcomes

License

Add a license of your choice (MIT recommended).
