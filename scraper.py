import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import schedule
import time
import os

# URL of the target page
URL = "https://boci-pru.com.hk/en/etf/wiseetf/02825"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# File to store the data
DATA_FILE = "data/nav_data.csv"

def scrape_nav():
    try:
        # Fetch the webpage
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the intra-day NAV (this is hypothetical - adjust based on actual HTML)
        # Inspect the page source (right-click > Inspect) to find the exact tag/class
        nav_element = soup.find("span", class_="intra-day-nav")  # Example class name
        if nav_element:
            nav_value = nav_element.text.strip()
        else:
            nav_value = "Not Found"

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Prepare data
        data = {"Timestamp": timestamp, "IntraDayNAV": nav_value}
        print(f"Scraped at {timestamp}: NAV = {nav_value}")

        # Save to CSV
        df = pd.DataFrame([data])
        if not os.path.exists("data"):
            os.makedirs("data")
        if os.path.exists(DATA_FILE):
            df.to_csv(DATA_FILE, mode="a", header=False, index=False)
        else:
            df.to_csv(DATA_FILE, mode="w", header=True, index=False)

    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

def run_scraper():
    # Schedule the scraper to run every 15 minutes
    schedule.every(15).minutes.do(scrape_nav)

    # Initial run
    scrape_nav()

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    run_scraper()
