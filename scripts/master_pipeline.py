import os

# Step 1: Parse XML and Clean Data
os.system("python3 scripts/parse_and_clean.py")

# Step 2: Fetch API Data
os.system("python3 scripts/gleif_api_interaction.py")

# Step 3: Merge Data
os.system("python3 scripts/merge_data.py")

print("Pipeline completed! Final dataset is ready in 'output/merged_data_cleaned.csv'")
