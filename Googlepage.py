

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

ipl=driver.find_element(By.XPATH,'//*[@id="APjFqb" and @name="q"]')
ipl.send_keys("TamizhagaVetriKazhagam")
ipl.submit()

time.sleep(10)


driver.quit()