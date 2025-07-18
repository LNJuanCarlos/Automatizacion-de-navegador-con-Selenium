from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Crear el navegador
driver = webdriver.Chrome()  # Asegúrate de que chromedriver esté en el mismo folder o en el PATH

# 2. Ir a Google
driver.get("https://www.google.com")

# 3. Aceptar cookies si aparecen (opcional)
try:
    driver.find_element(By.ID, "L2AGLb").click()  # Botón "Aceptar todo" de cookies
except:
    pass

# 4. Buscar algo
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("Python automatización")
buscador.send_keys(Keys.RETURN)

# 5. Esperar un poco para que cargue
time.sleep(2)

# 6. Obtener los títulos de resultados
resultados = driver.find_elements(By.CSS_SELECTOR, "h3")

print("\nResultados:")
for r in resultados:
    if r.text.strip() != "":
        print("➡️", r.text)

# 7. Cerrar el navegador
driver.quit()
