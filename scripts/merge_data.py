import pandas as pd

# Paths to input files
local_data_path = "output/cleaned_data.csv"
api_data_path = "output/api_enriched_data.csv"
merged_output_path = "output/merged_data_cleaned.csv"

# Load datasets
local_data = pd.read_csv(local_data_path)
api_data = pd.read_csv(api_data_path)

# Merge on the "LEI" column
merged_data = pd.merge(local_data, api_data, on="LEI", how="left")

# Drop duplicate or unnecessary columns
merged_data = merged_data.rename(columns={
    "Legal Name_x": "Legal Name (Local)",
    "Country_x": "Country (Local)",
    "Status_x": "Status (Local)",
    "Legal Name_y": "Legal Name (API)",
    "Country_y": "Country (API)",
    "Status_y": "Status (API)"
})

#fill missing values with placeholders
merged_data.fillna("Not Available", inplace=True)
# Save the cleaned merged dataset
merged_data.to_csv(merged_output_path, index=False)
print(f"Cleaned merged data saved to {merged_output_path}")

