from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 1. Iniciar navegador
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Ir a la página
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(2)

# 3. Aceptar cookies si aparecen (evita errores)
try:
    driver.switch_to.frame("ez-accept-all")
    driver.find_element(By.ID, "ez-accept-all").click()
    driver.switch_to.default_content()
except:
    pass

# 4. Llenar campos de texto
driver.find_element(By.NAME, "firstname").send_keys("Juan Carlos")
driver.find_element(By.NAME, "lastname").send_keys("Chamorro Baldera")

# 5. Seleccionar género (radio button)
driver.find_element(By.ID, "sex-0").click()  # Male

# 6. Seleccionar experiencia (radio button)
driver.find_element(By.ID, "exp-3").click()

# 7. Ingresar fecha
driver.find_element(By.ID, "datepicker").send_keys("04/07/2025")

# 8. Seleccionar profesiones (checkbox)
driver.find_element(By.ID, "profession-0").click()  # Manual Tester
driver.find_element(By.ID, "profession-1").click()  # Automation Tester

# 9. Seleccionar herramienta (checkbox)
driver.find_element(By.ID, "tool-2").click()  # Selenium Webdriver

# 10. Seleccionar continente (dropdown)
continente = Select(driver.find_element(By.ID, "continents"))
continente.select_by_visible_text("South America")

# 11. Seleccionar comandos de Selenium (multi-select)
comandos = Select(driver.find_element(By.ID, "selenium_commands"))
comandos.select_by_visible_text("Browser Commands")
comandos.select_by_visible_text("Navigation Commands")

# 12. Espera para ver el resultado antes de enviar
time.sleep(2)

# 13. Enviar formulario (no funciona porque el botón no hace nada en este sitio)
# driver.find_element(By.ID, "submit").click()

print("Formulario llenado correctamente")

# 14. Cerrar navegador
time.sleep(3)
driver.quit()