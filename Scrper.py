from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Create a Service object using ChromeDriverManager
service = Service(ChromeDriverManager().install())


# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
driver.get("https://www.motionelements.com/search/video?s=")
driver.implicitly_wait(10)

a_elements = driver.find_elements(By.XPATH,"//a[@class='product-click']")
urls = [a_element.get_attribute('href') for a_element in a_elements]

# Create a DataFrame from the list of URLs
df = pd.DataFrame({'URL': urls})

# Save the DataFrame to a CSV file
df.to_csv('urls.csv', index=False)

# Close the WebDriver
driver.quit()