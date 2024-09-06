from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from time import sleep
import sys

def login_wait(driver):
    # Navigate to the favorites page
    driver.get("https://nhentai.net/favorites/")
    while True:
        try:
            # Check if the user is logged in by looking for an element that is only visible when logged in
            logged_in_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gallery-favorite")))
            break
        except:
            # If the element is not found, wait for 5 seconds and try again
            sleep(5)

    # Now the user is logged in, you can proceed with the rest of the code
    print("User is logged in!")

def save_doujinshi(driver):
    did = 1
    page = "https://nhentai.net/favorites/?page={}"
    all_dids = []

    while True:
        try:
            driver.get(page.format(did))
            
            # Wait for the page to load and the data-id elements to be present
            WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gallery-favorite")))

            # Extract the data-id elements
            data_id_elements = driver.find_elements(By.CSS_SELECTOR, "div.gallery-favorite")

            # Extract the data-id values
            data_ids = [element.get_attribute("data-id") for element in data_id_elements]
            print(f"Data IDs: {data_ids}\n")
            all_dids.extend(data_ids)
        except:
            print(f"\n\nGran Total: {len(all_dids)}")
            with open("all_dids.txt", "w") as f:
                f.write("\n".join(all_dids))
            # Close the browser
            driver.quit()
            break
        did += 1

def save_all_dids():
    # Specify the path to the geckodriver
    geckodriver_path = "/snap/bin/geckodriver"

    # Create a Service instance
    service = Service(geckodriver_path)

    # Create a WebDriver instance
    driver = webdriver.Firefox(service=service)
    
    # User Interactive Login
    login_wait(driver)

    # download all doujinshis
    save_doujinshi(driver)