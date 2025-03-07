"""
    https://the-internet.herokuapp.com/drag_and_drop
    Solucionar DRAG & DROP con Python, Selenium buscando la solución en internet
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configura el controlador del navegador (asegúrate de tener el controlador adecuado instalado)
driver = webdriver.Chrome()

# Abre la URL
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

# Encuentra los elementos de los cuadrados A y B
square_a = driver.find_element_by_id("column-a")
square_b = driver.find_element_by_id("column-b")

# Crea una instancia de ActionChains
actions = ActionChains(driver)

# Realiza la acción de arrastrar y soltar
actions.drag_and_drop(square_a, square_b).perform()

# Espera unos segundos para ver el resultado
time.sleep(10)

# Cierra el navegador
driver.quit()