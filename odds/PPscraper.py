from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver. support import expected_conditions as EC
import time
import pandas as pd

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://app.prizepicks.com/")

wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "close")))
driver.finde_element(By.XPATH, '/html/body/div[2]/div[3]/div/div.div[3]/button').click()
time.sleep(10)