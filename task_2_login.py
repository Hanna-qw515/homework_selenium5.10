import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
username_field = driver.find_element(By.ID,"username")
username_field.send_keys("tomsmith")
password_field = driver.find_element(By.ID,"password")
password_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
time.sleep(2)
flash_message = driver.find_element(By.ID,"flash")
flash_text = flash_message.text
assert "You logged into a secure area!" in flash_text
print("✅ Позитивный тест пройден!")
driver.quit()