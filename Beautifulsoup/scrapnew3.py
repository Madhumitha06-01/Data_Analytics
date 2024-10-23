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

url = "https://friendsdiaper.in/products/premium-adult-diaper-dry-pants"
page = requests.get(url)

# Check if the request was successful
if page.status_code == 200:
    # Get all HTML code
    fullcode = BeautifulSoup(page.text, 'html.parser')  # Use 'html.parser'
    # Get description data
    Details = fullcode.find('div', class_='contable')
    
    if Details:
        print(Details.text)  # Print the description text
    else:
        print("Description not found.")
else:
    print(f"Failed to retrieve page: {page.status_code}")
if page.status_code == 200:

    #description
    fullcode = BeautifulSoup(page.text, 'html.parser')  # Use 'html.parser'
    description = fullcode.find('div',class_='main-prod-tab-list-desc')
    if description:
        print(description.text)  # Print the description text
    else:
        print("Description not found.")
# Clean up
driver.quit()
