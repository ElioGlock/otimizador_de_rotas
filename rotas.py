from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com/maps")
driver.maximize_window()

routes = driver.find_element(By.ID,"hArJGc")
routes.click()


 
enderecos = "Praça Ismene Mendes, s/n - Centro, Uberlândia - MG, 38400-186"

time.sleep(600)
