import xml.etree.ElementTree as ET
import pandas as pd
import os

# Paths
data_path = '/home/shubham/Downloads/GLEIF_Project/data/data.xml'
raw_output = '/home/shubham/Downloads/GLEIF_Project/output/raw_data.csv'
cleaned_output = '/home/shubham/Downloads/GLEIF_Project/output/cleaned_data.csv'

# Ensure output directory exists
os.makedirs('/home/shubham/Downloads/GLEIF_Project/output', exist_ok=True)

# Parse XML
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {'ns': 'http://www.gleif.org/data/schema/leidata/2016'}

    records = []
    for record in root.findall('.//ns:LEIRecord', namespace):
        lei = record.find('ns:LEI', namespace).text
        entity = record.find('ns:Entity', namespace)

        legal_name = entity.find('ns:LegalName', namespace).text
        country = entity.find('ns:LegalAddress/ns:Country', namespace).text
        status = entity.find('ns:EntityStatus', namespace).text

        records.append({
            'LEI': lei,
            'Legal Name': legal_name,
            'Country': country,
            'Status': status
        })
    return records

# Save to CSV
def save_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

# Main execution
if __name__ == "__main__":
    if os.path.exists(data_path):
        records = parse_xml(data_path)
        if records:
            save_to_csv(records, raw_output)
            df = pd.read_csv(raw_output)

            # Data cleaning
            df.drop_duplicates(inplace=True)
            df.fillna('Unknown', inplace=True)
            df.to_csv(cleaned_output, index=False)
            print(f"Cleaned data saved to {cleaned_output}")
        else:
            print("No records found in the XML.")
    else:
        print(f"{data_path} does not exist.")

