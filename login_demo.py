from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Abrimos el navegador
driver = webdriver.Chrome()

# 2. Accedemos al sitio de login
driver.get("https://the-internet.herokuapp.com/login")

# 3. Esperamos unos segundos
time.sleep(1)

# 4. Ingresamos usuario y contraseña
usuario = driver.find_element(By.ID, "username")
usuario.send_keys("tomsmith")  # usuario válido

contrasena = driver.find_element(By.ID, "password")
contrasena.send_keys("SuperSecretPassword!")  # contraseña válida

# 5. Enviamos el formulario (presionamos Enter)
contrasena.send_keys(Keys.RETURN)

# 6. Esperamos a que cargue y verificamos el resultado
time.sleep(2)

mensaje = driver.find_element(By.ID, "flash")
print("\n Resultado del login:")
print(mensaje.text)

# 7. Cierra el navegador
driver.quit()