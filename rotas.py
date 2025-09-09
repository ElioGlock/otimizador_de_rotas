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

def open_routes():
    routes = driver.find_element(By.ID,"hArJGc")
    routes.click()
    
def put_places(enderecos):
    start_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/input")
    time.sleep(1)
    start_place.send_keys("R. Antônio Cardoso Franco, 268 - Casa Branca, Santo André - SP, 09015-530")
    finish_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/input")
    finish_place.send_keys(enderecos)
    finish_place.send_keys(Keys.ENTER)


 
if __name__ == "__main__":
    
    enderecos = "Av. Pedro Álvares Cabral, s/n - Vila Mariana, São Paulo - SP, 04094-050"
    # R. Giácomo Versolato - Nova Petrópolis, São Bernardo do Campo - SP, 09770-440
    open_routes()
    time.sleep(2)
    put_places(enderecos)

time.sleep(600)
