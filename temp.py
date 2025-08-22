import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App Title
st.title("📊 Data Analysis Web App")
st.subheader("Analyze your dataset with Python & Streamlit")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Buttons for head & tail
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Head"):
            st.write(data.head())
    with col2:
        if st.button("Show Tail"):
            st.write(data.tail())

    # Datatypes
    if st.checkbox("Show Data Types"):
        st.write(data.dtypes)

    # Shape
    shape_option = st.radio("Show Dataset Shape:", ('Rows', 'Columns'))
    if shape_option == 'Rows':
        st.write(f"Number of Rows: {data.shape[0]}")
    else:
        st.write(f"Number of Columns: {data.shape[1]}")

    # Null values
    if st.button("Check Missing Values"):
        if data.isnull().values.any():
            st.warning("⚠️ Dataset contains missing values")
            if st.checkbox("Show Missing Values Heatmap"):
                
                sns.heatmap(data.isnull())
                st.pyplot()   # pass figure here
        else:
            st.success("🎉 No missing values found!")

    # Duplicates
    if data.duplicated().any():
        st.warning("⚠️ Dataset has duplicate rows")
        remove = st.selectbox("Do you want to remove duplicates?", ["No", "Yes"])
        if remove == "Yes":
            data = data.drop_duplicates()
            st.success("✅ Duplicates removed")
    else:
        st.info("No duplicate rows found")

    # Summary
    if st.checkbox("Show Summary Statistics"):
        st.write(data.describe(include='all'))

# About Section
if st.button("ℹ️ About App"):
    st.info("This app helps you analyze datasets quickly using Streamlit!")

if st.button("👩‍💻 Created By"):
    st.success("Sanjana Kapuganti")
