
import requests
from datetime import datetime
import csv
import os
import json

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

if __name__ == "__main__":
    scrape_signatures()


