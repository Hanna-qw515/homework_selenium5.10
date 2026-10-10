import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com")
driver.maximize_window()
time.sleep(1)

links = driver.find_element(By.XPATH,"//a[text()='Form Authentication']")
links.click()
time.sleep(1)

assert "The Internet" in driver.title, f"Неожиданный заголовок: {driver.title}"
print(f"Заголовок страницы: {driver.title}")
driver.back()
time.sleep(1)
driver.quit()
