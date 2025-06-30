
import requests
from datetime import datetime
import csv
import os
import pandas as pd


def scrape_signatures():
    api_url = "https://eci.ec.europa.eu/045/public/api/report/progression"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        signatures = data.get("signatureCount", "N/A")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        csv_file_path = "signatures.csv"

        file_exists = os.path.isfile(csv_file_path)
        with open(csv_file_path, "a", newline="") as csvfile:
            fieldnames = ["Timestamp", "Signatures"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()
            writer.writerow({"Timestamp": timestamp, "Signatures": signatures})
        print(f"Scraped at {timestamp}: {signatures} signatures.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def updateExcel():
    excel_path = r"C:\Users\Geno\OneDrive\Documents\Signatures over time.xlsx"
    csv_path = r"C:\Users\Geno\Documents\GitHub\Stop-Destroying-Games-Signatures\scrapeSignatures\signatures.csv"

    df_csv = pd.read_csv(csv_path)

    with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_csv.to_excel(writer, sheet_name='Signature data', index=False)


if __name__ == "__main__":
    scrape_signatures()


