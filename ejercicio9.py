"""
    https://the-internet.herokuapp.com/hovers
    clickar en el enlace que sale al poner el cursor/ratón encima de la imagen (la llamamos avatar en el código)
 """

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/hovers")

avatar = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > img")

hover = ActionChains(driver).move_to_element(avatar)
hover.perform()

link = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > div > a")

link.click()

time.sleep(5)
