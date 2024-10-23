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
url="https://www.karmamedical.com/en-in/"
page = requests.get(url)
# Get all HTML code"
data =BeautifulSoup(page .text,'html')
#print(data)
#get DIV tag code only
div = data.find_all('div')
print(div)
# convert a scrping data into text 
div1 = data.find('div').text
print(div1)

