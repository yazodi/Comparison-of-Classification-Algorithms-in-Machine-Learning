import streamlit as st
import joblib
import numpy as np

# Modeli yükle
model = joblib.load("KNN_classifier.pkl")

st.title("🛍️ Satın Alma Tahmin Uygulaması")
st.markdown("Bu uygulama, bir kişinin yaşına ve maaşına göre ürün satın alıp almayacağını tahmin eder.")

# Girdi alanları
age = st.slider("Yaş", 18, 70, 30)
salary = st.number_input("Tahmini Maaş (USD)", min_value=1000, max_value=200000, value=50000, step=1000)

# Tahmin
if st.button("Tahmin Et"):
    input_data = np.array([[age, salary]])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("Bu kişi büyük olasılıkla satin alır.")
    else:
        st.warning("Bu kişi büyük olasılıkla satin almaz.")
