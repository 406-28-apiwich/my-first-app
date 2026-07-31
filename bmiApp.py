import streamlit as st

st.markdown("# :red[💪BMI CALCULATOR]")
st.write("Type in your Weight & Height")

weight = st.number_input("Weight 🏋️ (KG):")
height_cm = st.number_input("Height 📏 (CM):")

if st.button("Calculate BMI 📈"):
 height_m = height_cm / 100
 bmi = weight / (height_m ** 2)
 
 st.write("---")
 st.header(f"YOUR BMI IS: **{bmi:.2f}**")

 if bmi < 18.5:
   st.warning("⚠️ Thin")
 elif 18.5 <= bmi < 23.0:
   st.success("⭐ Healthy")
 elif 23.0 <= bmi < 25.0:
   st.success("ℹ️ Fat")
 else:
   st.error("🚨 Very fat")

 st.divider()
 st.write("นายอภิวิชญ์ ญาณวดี เลขที่ 28 ม.4/6")
