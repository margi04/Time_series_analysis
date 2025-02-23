import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI
st.title("📊 Time Series Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df)  # Displays all columns

    # Let user select date column
    date_col = st.selectbox("📅 Select Date Column", df.columns)

    # Convert date column to datetime format
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # Let user select categorical column to filter rows
    category_col = st.selectbox("🔍 Select a Column to Filter Rows", df.columns)

    # Get unique values from the selected column
    unique_values = df[category_col].unique().tolist()

    # Let user choose specific rows based on unique values
    selected_rows = st.multiselect("📝 Select Rows for Time Series Analysis", unique_values)

    # Button to show time series plot
    if st.button("📈 Show Time Series Analysis"):
        if not selected_rows:
            st.warning("⚠️ Please select at least one row!")
        else:
            fig, ax = plt.subplots(figsize=(10, 5))
            for value in selected_rows:
                filtered_data = df[df[category_col] == value]
                ax.plot(filtered_data[date_col], filtered_data.iloc[:, 1], label=value)
            ax.set_xlabel("Date")
            ax.set_ylabel("Values")
            ax.set_title("📈 Time Series Analysis")
            ax.legend()
            st.pyplot(fig)
