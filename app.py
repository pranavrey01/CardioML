
import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CardioML",
    page_icon="❤️",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent

# Load the saved model and threshold
model = joblib.load(BASE_DIR / "cardioml_model.joblib")

with open(BASE_DIR / "model_config.json", "r") as file:
    config = json.load(file)

threshold = config["threshold"]

# App heading
st.title("❤️ CardioML")
st.subheader("Heart Disease Classification Demo")
st.write(
    "Enter the sample's measurements to generate an "
    "experimental model prediction."
)

st.warning(
    "Educational project only. This model is not validated "
    "for clinical diagnosis or medical decision-making."
)

# Input form
with st.form("patient_form"):
    st.subheader("Patient measurements")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age (years)", min_value=1, max_value=120, value=50
        )
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox(
            "Chest pain type",
            [
                "typical angina",
                "atypical angina",
                "non-anginal",
                "asymptomatic"
            ]
        )
        trestbps = st.number_input(
            "Resting blood pressure",
            min_value=50.0, max_value=300.0, value=120.0
        )
        chol = st.number_input(
            "Cholesterol",
            min_value=50.0, max_value=700.0, value=200.0
        )
        fbs = st.selectbox("Fasting blood sugar > 120 mg/dl", [False, True])
        restecg = st.selectbox(
            "Resting ECG",
            ["normal", "st-t abnormality", "lv hypertrophy"]
        )

    with col2:
        thalch = st.number_input(
            "Maximum heart rate achieved",
            min_value=40.0, max_value=250.0, value=150.0
        )
        exang = st.selectbox("Exercise-induced angina", [False, True])
        oldpeak = st.number_input(
            "ST depression (oldpeak)",
            min_value=-5.0, max_value=10.0, value=0.0
        )
        slope = st.selectbox(
            "ST segment slope",
            ["upsloping", "flat", "downsloping"]
        )
        ca = st.selectbox(
            "Major vessels (ca)",
            ["Unknown", "0", "1", "2", "3"]
        )
        thal = st.selectbox(
            "Thalassemia (thal)",
            ["Unknown", "normal", "fixed defect", "reversible defect"]
        )

    submitted = st.form_submit_button("Run prediction")

# Predict only when the form is submitted
if submitted:
    # Construct one row with the exact feature names used in training
    patient = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalch": thalch,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": float(ca) if ca != "Unknown" else float("nan"),
        "thal": thal if thal != "Unknown" else None
    }])

    # The pipeline handles missing values and encoding
    probability = model.predict_proba(patient)[0, 1]
    prediction = int(probability >= threshold)

    st.divider()
    st.subheader("Model output")

    st.metric("Estimated model probability", f"{probability:.1%}")
    st.caption(f"Classification threshold: {threshold:.2f}")

    if prediction == 1:
        st.error("Positive classification")
    else:
        st.success("Negative classification")

    st.caption(
        "This is an experimental dataset classification, "
        "not a diagnosis or a validated clinical risk estimate."
    )
