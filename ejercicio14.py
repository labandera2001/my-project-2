"""
    https://the-internet.herokuapp.com/tables
    blablabla
"""

import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/tables")

#table1 > tbody > tr:nth-child(3) > td:nth-child(4)