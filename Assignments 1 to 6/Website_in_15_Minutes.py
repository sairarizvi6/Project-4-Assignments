import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())  # Better than st.write() for DataFrames

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.dataframe(filtered_df)  # Better display for DataFrames

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns, key="x_axis")  # Unique key
    y_column = st.selectbox("Select y-axis column", columns, key="y_axis")  # Unique key

    if st.button("Generate Plot"):
        st.line_chart(data=filtered_df, x=x_column, y=y_column)  # Simpler syntax
else:
    st.info("Waiting for file upload...")  # Better than st.write()