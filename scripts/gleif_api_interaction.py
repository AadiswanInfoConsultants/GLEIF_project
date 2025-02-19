import requests
import pandas as pd

# Base API URL
base_url = "https://api.gleif.org/api/v1/"

# Fetch details for a specific LEI
def fetch_lei_details(lei):
    endpoint = f"lei-records/{lei}"
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Save API Data to CSV
def save_api_data_to_csv(lei_list, output_path):
    records = []
    for lei in lei_list:
        details = fetch_lei_details(lei)
        if details:
            entity = details['data']['attributes']
            legal_name = entity['entity']['legalName']['name']
            country = entity['entity']['legalAddress']['country']
            city = entity['entity']['legalAddress']['city']
            status = entity['entity']['status']
            last_update = entity['registration']['lastUpdateDate']
            next_renewal = entity['registration']['nextRenewalDate']
            
            # Append to records
            records.append({
                'LEI': lei,
                'Legal Name': legal_name,
                'Country': country,
                'City': city,
                'Status': status,
                'Last Update': last_update,
                'Next Renewal': next_renewal
            })
    # Save to CSV
    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False)
    print(f"API data saved to {output_path}")

# Main execution
if __name__ == "__main__":
    # Example LEIs
    lei_list = ["549300YWX7WFTLHG5M31"]  # Replace or add more LEIs
    output_csv = "output/api_enriched_data.csv"
    save_api_data_to_csv(lei_list, output_csv)

