# GLEIF_project
Overview

This project automates the processing, enrichment, and visualization of Legal Entity Identifier (LEI) data
Project Structure

GLEIF_LEI_Project/
│── scripts/
│   ├── parse_and_clean.py        # Parses XML data and cleans it
│   ├── gleif_api_interaction.py  # Fetches LEI details from the GLEIF API
│   ├── merge_data.py             # Merges local and API data
│── output/                       # Stores generated CSV files
│── master_pipeline.py            # Automates the entire pipeline
│── app.py                        # Streamlit dashboard for LEI data
│── README.md                     # Project documentation

Workflow & Explanation
1. Parsing and Cleaning XML Data (parse_and_clean.py)

    Reads an XML file containing raw LEI data.
    Extracts key details: LEI, Legal Name, Country, and Status.
    Removes duplicates and fills missing values.
    Saves the cleaned dataset as output/cleaned_data.csv.

2. Fetching Additional Data from GLEIF API (gleif_api_interaction.py)

    Queries the GLEIF API to fetch additional details for each LEI.
    Retrieves fields like City, Status, Last Update, and Next Renewal.
    Saves the API-enriched dataset as output/api_enriched_data.csv.

3. Merging Local and API Data (merge_data.py)

    Combines cleaned_data.csv (local XML data) with api_enriched_data.csv (GLEIF API data).
    Merges based on the LEI column.
    Renames and cleans columns for clarity.
    Saves the final dataset as output/merged_data_cleaned.csv.

4. Automating the Full Pipeline (master_pipeline.py)

    Executes all three scripts sequentially.
    Ensures that the final dataset is prepared automatically.

5. Web-Based LEI Data Explorer (app.py)

    Loads the merged_data_cleaned.csv file.
    Allows users to search for an LEI and view its details.
    Displays a sample dataset in an interactive UI.
    Marks entries where API data is missing.

