import requests
from bs4 import BeautifulSoup
import datetime

def scrape_value(url, xpath):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    value_element = soup.select_one(xpath)
    if value_element:
        return value_element.text.strip()
    else:
        return "Value not found"

def save_to_file(value, timestamp):
    with open('data.txt', 'a') as f:
        f.write(f"{timestamp}: {value}\n")

# Replace with your target URL and XPath
url = "http://www.boci-pru.com.hk/en/etf/wiseetf/02825"
xpath = "table#cms_table_etf_nav_inner_table_mobile_1"

value = scrape_value(url, xpath)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
save_to_file(value, timestamp)
