from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver. support import expected_conditions as EC
import time
import pandas as pd

#PATH = ''
driver = webdriver.Chrome()

driver.get("https://app.prizepicks.com/")

time.sleep(10)

wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='name'][normalize-space()='NFL']")))
#driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div.div[3]/button').click()
#time.sleep(10)

ppPlayers = []

#Click on NFL Tab
driver.find_element(By.XPATH, "//div[@class='name'][normalize-space()='NFL']").click()
time.sleep(5)

#Waiting until stat_container is visible
stat_container = WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "stat-container")))

#Finds all of the stat elements in the stat_container
categories = driver.find_element(By.CSS_SELECTOR, "stat-container").text.split('\n')

for category in categories:
    driver.find_element(By.XPATH, f"//div[text()='{category}']").click()
    projectionsPP = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".projection")))


