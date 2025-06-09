import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# URL of the webpage to scrape
URL = "https://www.boci-pru.com.hk/en/etf/wiseetf/02825"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Path to the CSV file
CSV_FILE = "data/nav_data.csv"

def scrape_nav():
    try:
        # Send HTTP request
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Raise exception for bad status codes

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the NAV value using the correct CSS selector
        nav_element = soup.select_one("#cms_table_etf_nav_inner_table_desktop tbody tr td:nth-child(4) div.general--fund--table__cell__content div")
        if nav_element:
            nav_value = nav_element.text.strip()
        else:
            nav_value = "Not found"

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Prepare data
        data = {"Timestamp": timestamp, "NAV_per_unit": nav_value}

        # Append to CSV
        df = pd.DataFrame([data])
        if not os.path.exists(CSV_FILE):
            df.to_csv(CSV_FILE, index=False)
        else:
            df.to_csv(CSV_FILE, mode="a", header=False, index=False)

        print(f"Scraped NAV: {nav_value} at {timestamp}")

    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    scrape_nav()
