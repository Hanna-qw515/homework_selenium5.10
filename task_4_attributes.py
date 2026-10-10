
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
password_field = driver.find_element(By.ID, "password")
field_type = password_field.get_attribute("type")
print(field_type)
assert field_type == "password", "Критический БАГ: пароль вводится открытым текстом!"
print(f"Тип поля пароля: {field_type}")
login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
#field_class = login_button.get_attribute("class")
#print(field_class)
print(login_button.get_attribute("class"))
driver.quit()