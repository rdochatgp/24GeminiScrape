import requests
from parsel import Selector
#from bs4 import BeautifulSoup
#import datetime


#def scrape_value(url, xpath):
#    response = requests.get(url)
#    soup = BeautifulSoup(response.text, 'html.parser')
#    value_element = soup.select_one(xpath)
#    if value_element:
#        return value_element.text.strip()
#    else:
#        return "Value not found"

#def save_to_file(value, timestamp):
#    with open('data.txt', 'a') as f:
#        f.write(f"{timestamp}: {value}\n")

# Replace with your target URL and XPath
url = "http://www.boci-pru.com.hk/en/etf/wiseetf/02825"
#XPATH ="div[@id='cms_table_etf_nav_inner_table_desktop']"
XPATH = "table[@id='cms_table_etf_nav_inner_table_mobile_1']"
respone = requests.get(url)
response.raise_for_status()
selector = Selector(text=response.text)
value = selector.xpath(XPATH),get()

if value:
    value = value.strip()
    print(f"Scraped value: {value}")
else:
    print("No value found")
open("output.txt","w") as f:
f.write(value)
#value = scrape_value(url, xpath)
#timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#save_to_file(value, timestamp)
