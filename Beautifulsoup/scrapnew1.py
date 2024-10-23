from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import requests
# Set the path to the Chromedriver
DRIVER_PATH = r'chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe'

# Create a Service object
service = Service(executable_path=DRIVER_PATH)

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")  # Ensure the browser window is maximized

# Initialize Chrome with the specified options and Service object
driver = webdriver.Chrome(service=service, options=options)
url="https://www.romsons.in/collections/hospital-care/products/intra-cath"
page = requests.get(url)

# Check if the request was successful
if page.status_code == 200:
# Get all HTML code"    
    data =BeautifulSoup(page.text,'html')
     #print(data)
    # Find the table
    table = data.find('table')  # You may need to specify an ID or class

    # Extract data frim table 
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all(['td', 'th'])  # Include both data and header cells
        cols = [col.get_text(strip=True) for col in cols]  # Get text and strip whitespace
        data.append(cols)

    # Print the extracted data
    for row in data:
        print(row)
else:
    print(f"Failed to retrieve the data")


