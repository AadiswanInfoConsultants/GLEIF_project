import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('output/merged_data_cleaned.csv')

# Rename columns for better readability
df.rename(columns={
    'LEI': 'LEI Code',
    'Legal Name (Local)': 'Legal Name (Local Dataset)',
    'Country (Local)': 'Country (Local Dataset)',
    'Status (Local)': 'Status (Local Dataset)',
    'Legal Name (API)': 'Legal Name (API Dataset)',
    'Country (API)': 'Country (API Dataset)',
    'City': 'City (API Dataset)',
    'Status (API)': 'Status (API Dataset)',
    'Last Update': 'Last API Update',
    'Next Renewal': 'Next Renewal Date'
}, inplace=True)

# Add a column to indicate missing API data
df['API Data Missing'] = df['Legal Name (API Dataset)'].apply(lambda x: x == "Not Available")

# Streamlit app title
st.title("GLEIF LEI Dataset Explorer")

# User input for LEI search
lei_input = st.text_input("Enter an LEI:")
if lei_input:
    result = df[df['LEI Code'] == lei_input]
    if not result.empty:
        st.write("Search Results:")
        st.dataframe(result)
    else:
        st.write("No matching LEI found.")

# Display a sample of the dataset
st.write("Sample of the Dataset:")
st.dataframe(df.head(10))

