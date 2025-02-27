"""
Ir a la url https://the-internet.herokuapp.com/login y logarse con los datos que se indica en la propia url
"""

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/login")

    tbx__username = driver.find_element(By.ID, "username")
    tbx__username.send_keys("tomsmith")

    tbx__password = driver.find_element(By.ID, "password")
    tbx__password.send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button").click()

    boton_logout = driver.find_element(By.CSS_SELECTOR, "#content > div > a > iasdf")

    if not boton_logout.is_displayed():
        driver.save_screenshot("evidencia_error.png")
        raise AssertionError("Error")

    driver.save_screenshot("screenshot.png")

except AssertionError as e:
    print(e)

except NoSuchElementException as e:
    print(e)

finally:
    driver.quit()
