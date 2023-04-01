from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://myaccount.nytimes.com/auth/login'
email = 'j364254@gmail.com'  # Replace with your actual email address
password = 'Totoro0415!'  # Replace with your actual password

# Configure Firefox WebDriver
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

# Get the login page
driver.get(url)

# Wait for the login form to load
time.sleep(2)

# Enter email and password
email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
email_input.send_keys(email)

password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
password_input.send_keys(password)

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Get webpage content
driver.get('https://www.nytimes.com/2023/03/31/nyregion/alvin-bragg-trump-investigation.html')

# Find the section with the specified name and class
section = driver.find_element(By.XPATH, '//section[@name="articleBody" and contains(@class, "meteredContent")]')

# Retrieve all paragraphs inside the section
paragraphs = section.find_elements(By.TAG_NAME, 'p')

# Extract text data from each paragraph and save it to a list
text_data = []
for paragraph in paragraphs:
    if paragraph.text.strip():
        text_data.append(paragraph.text)

print("Text data:", text_data)

# Close the WebDriver
driver.quit()
