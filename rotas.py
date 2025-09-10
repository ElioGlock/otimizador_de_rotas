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
    
def set_places():
    start_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/input")
    time.sleep(1)
    start_place.send_keys(startpoint)
    finish_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/input")
    finish_place.send_keys(enderecos[0])
    finish_place.send_keys(Keys.ENTER)
    
def new_places():
    for c in [1,2,3]:
        new = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/button/div[2]")
        new.click()
        if c ==1:
            f = 3
        if c ==2:
           f = 4
        if c ==3:
            f = 5
        new_input = driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[{f}]/div[2]/div[1]/div/input")
        new_input.send_keys(enderecos[c])
        new_input.send_keys(Keys.ENTER)
        time.sleep(2)

 
if __name__ == "__main__":
    startpoint = "R. Antônio Cardoso Franco, 268 - Casa Branca, Santo André - SP, 09015-530"
    enderecos = ["Av. Pedro Álvares Cabral, s/n - Vila Mariana, São Paulo - SP, 04094-050",
                 "R. Manuel França dos Santos, 174 - Vila Sapopemba, São Paulo - SP, 03975-130",
                 "Praça Charles Miller, s/n - Pacaembu, São Paulo - SP, 01234-010",
                 "Av. Sen. Teotônio Vilela, 261 - Jardim Malia I, São Paulo - SP, 04801-000"]
                 
    open_routes()
    time.sleep(2)
    set_places()
    time.sleep(1)
    new_places()
 
time.sleep(600)