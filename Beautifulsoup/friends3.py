from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

# Set the path to the Chromedriver
DRIVER_PATH = r'chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe'

# Create a Service object
service = Service(executable_path=DRIVER_PATH)

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")  # Ensure the browser window is maximized

# Initialize Chrome with the specified options and Service object
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to the website
     driver.get("https://friendsdiaper.in/")
    # Wait for the element to be clickable and click on the navbar item
    element = WebDriverWait(driver, 30).until(        
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[8]/div/div/div[2]/a'))
    )     
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(3)
    element.click()
    
    # Initialize an empty list to store the results
    results = []
    total_products = 5  # Total products to scrape

    for i in range(1, total_products + 1):  # Loop through products
        print(f"Processing product {i}...")  
        try:
            # Close ad if it appears
            try:
                deny_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID, "deny"))  # Adjust the ID as needed 
                )
                deny_button.click()
                print("Closed ad pop-up.")
            except Exception:
                print("No ad found or couldn't close it.")

            # Build XPath for the product item dynamically
            product_xpath = f"/html/body/div[11]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div[{i}]//a"
            product_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, product_xpath))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", product_element)
            time.sleep(3)  # Allow time for scrolling
            
            # Click on the product item
            product_element.click()

            # Wait for product details to load
            WebDriverWait(driver, 30).until(                
                EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/main/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[1]"))
            )

            # Extract Item Name
            try:
                item_name = driver.find_element(By.XPATH, "/html/body/div[11]/main/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[1]").text
            except:
                item_name = driver.find_element(By.XPATH, '/html/body/main/section[3]/section/div/div/div/div[2]/div[1]/div/gp-product/product-form/form/div/div[2]/div[1]/div/div/h1').text

            # Extract Product Summary
            try:
                mrp = driver.find_element(By.XPATH, '/html/body/div[11]/main/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[2]/span[1]/span[2]').text
            except:
                mrp = "MRP not found"
                print("MRP error")

            # Extract Image URL
            try:
                image_url = driver.find_element(By.XPATH, '//*[@id="xzoom-default"]').get_attribute('src')
            except:
                image_url = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/figure/div/a/img').get_attribute('src')
            # Check if the request was successful
            page = requests.get(url)

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
# 
            # Store product details
            product_result = {
                "Product_Name": item_name,
                "MRP": mrp,
                "Product_Image": image_url,
                "DESCRIPTION":description,
                "SPECIFICATION":Details
            }
            results.append(product_result)
            print(f"Product {i} processed successfully.")
            time.sleep(2)
            
            # Navigate back to the listing page
            driver.back()

            # Wait for the listing page to reload
            nextpage = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[8]/div[1]/div[1]/div[2]/a[1]/div[1]"))
            )
            nextpage.click()
            print("Navigated back to the listing page.")
        
        except Exception as e:
            print(f"An error occurred while processing product {i}: {e}")

    # Create a DataFrame from the results
    df_data = pd.DataFrame(results)

    # Save DataFrame to an Excel file
    df_data.to_excel('friend3_scraping_result.xlsx', index=False)

finally:
    # Clean up
    driver.quit()
    print("WebDriver closed.")