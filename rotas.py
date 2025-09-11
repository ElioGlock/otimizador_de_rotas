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
    time.sleep(2)
    
def set_place():
    start_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/input")
    time.sleep(1)
    start_place.send_keys(startpoint)
    time.sleep(1)
    
def new_places():
    for c in list(range(len(ordem_enderecos))):
        if c == 0:
            second_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/input")
            second_place.clear()
            second_place.send_keys(ordem_enderecos[0])
            second_place.send_keys(Keys.ENTER)
        if c != 0:
            new = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/button/div[2]")
            new.click()
            if c == 0:
                pass
            f = c + 2
            new_input = driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[{f}]/div[2]/div[1]/div/input")
            new_input.send_keys(ordem_enderecos[c])
            new_input.send_keys(Keys.ENTER)
            time.sleep(2)
    time.sleep(1)
        
def return_time():
    xpath = '//div[@id="section-directions-trip-0"]//div[contains(text(),"min")]'
    wait = WebDriverWait(driver,timeout=3)
    time_element = wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
    print(time_element.text)
    return time_element.text

def return_distance():
    xpath = '//div[@id="section-directions-trip-0"]//div[contains(text(),"km")]'
    wait = WebDriverWait(driver,timeout=3)
    time_element = wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
    time_element_filter = float(time_element.text.replace("km","").replace(",","."))
    print(time_element_filter)
    return time_element_filter

def remake_order():
    dictionary ={}
    for c in list(range(len(enderecos))):
        second_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/input")
        second_place.clear()
        second_place.send_keys(enderecos[c])
        second_place.send_keys(Keys.ENTER)
        time.sleep(1)
        distance = return_distance()
        dictionary[enderecos[c]] = distance
        sorted_list_dictionary = sorted(dictionary.items(), key=lambda item: item[1])
        sorted_dict_dictionary = dict(sorted_list_dictionary)
        ordem_enderecos = list(sorted_dict_dictionary.keys())
        
        time.sleep(2)
    return  ordem_enderecos
   
        


if __name__ == "__main__":
    startpoint = "R. Antônio Cardoso Franco, 268 - Casa Branca, Santo André - SP, 09015-530"
    
    enderecos = ["Av. Pedro Álvares Cabral, s/n - Vila Mariana, São Paulo - SP, 04094-050",
                 "R. Manuel França dos Santos, 174 - Vila Sapopemba, São Paulo - SP, 03975-130",
                 "Praça Charles Miller, s/n - Pacaembu, São Paulo - SP, 01234-010",
                 "Av. Sen. Teotônio Vilela, 261 - Jardim Malia I, São Paulo - SP, 04801-000"]
                 
    open_routes()
    set_place()
    ordem_enderecos = remake_order()
    new_places()
    
 
time.sleep(600)



        