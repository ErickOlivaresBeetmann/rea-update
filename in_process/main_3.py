# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script to obtain and update the values corresponding to the REA."""

import os
import time
from datetime import datetime, timedelta

import pyodbc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# variables: fecha, hora, pasivoconovcido,, pasivopotencia, rea

def finish_web_scraping(msg = None, logout_tabs = 0, error = True):
	if msg:
		print(msg)
	if logout_tabs != 0:
		close_session(logout_tab = logout_tabs)
	driver.quit()
	time.sleep(2)
	if error:
		exit()


def close_session(logout_tab):
	if logout_tab == 1:
		error = True
		attempts = 5
		while error and attempts > 0:
			try:
				driver.find_element_by_id("btnCerrarSesion").click()
				print("Session closed.")
				error = False
			except Exception:
				attempts -= 1
				if attempts == 0:
					print("The session could not be closed.")
	elif logout_tab == 2:
		error = True
		attempts = 5
		while error and attempts > 0:
			try:
				driver.find_element_by_link_text("Cerrar Sesión").click()
				print("Session closed.")
				error = False
			except Exception:
				attempts -= 1
				if attempts == 0:
					print("The session could not be closed.")


#now = datetime.now() - timedelta(.208333)
#print(now.strftime("%Y%m%d"))


# Define path for the driver
google_driver_path = os.path.abspath("drivers/chromedriver2.exe")

# Define the password and the corresponding file paths for the first authentication
certificate_path = os.path.abspath("files/certificate.cer")
key_path = os.path.abspath("files/private_key.key")
first_password = "00Beetmann"

# Define the username and password for the second authentication
user = "BTMNN"
second_password = "BTMNSIN"

# Define driver options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors-spki-list")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
try:
	driver = webdriver.Chrome(options=chrome_options, executable_path=google_driver_path)
except Exception:
	print("This version of ChromeDriver is not supported.")
	print("Try to install the version that matches your Google Chrome browser at: https://sites.google.com/chromium.org/driver/")
driver.implicitly_wait(30)

#---------------------------------------------------------------------------------#

print("\nEstablishing connection to the website...")

# Establish connection to the website
error = True
try_again = "y"
while try_again == "y" and error:
	try:
		driver.get("https://memsim.cenace.gob.mx/produccion/participantes/LOGIN/")
		error = False
	except:
		print("The website could not be accessed.")
		option = input("Try again? (y/n): ")
		if option != "y":
			exit()

print("Connection established.\n")

# Wait for the page to load
time.sleep(5)

#---------------------------------------------------------------------------------#

print("Performing first authentication...")

# Enter certificate for the first login
error = True
attempts = 5
while error:
	try:
		certificate_elem = driver.find_element_by_id("uploadCerfile0")
		certificate_elem.clear()
		certificate_elem.send_keys(certificate_path)
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not upload certificate.")
		attempts -= 1

# Enter private key for the first login
error = True
attempts = 5
while error:
	try:
		key_elem = driver.find_element_by_id("uploadKeyfile0")
		key_elem.clear()
		key_elem.send_keys(key_path)
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not upload private key.")
		attempts -= 1

# Enter password for the first login
error = True
attempts = 5
while error:
	try:
		password_1_elem = driver.find_element_by_id("txtPrivateKey")
		password_1_elem.clear()
		password_1_elem.send_keys(first_password)
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not enter first password.")
		attempts -= 1

# Click submit button for the first login
error = True
attempts = 5
while error:
	try:
		driver.find_element_by_id("btnEnviar").click()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not click submit button.")
		attempts -= 1

print("First authentication completed.\n")

# Wait for the next page to load
time.sleep(10)

#---------------------------------------------------------------------------------#

print("Performing second authentication...")

# Enter username the second login
error = True
attempts = 5
while error:
	try:
		user_elem = driver.find_element_by_id("txtUsuario")
		user_elem.clear()
		user_elem.send_keys(user)
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not enter username.")
		attempts -= 1

# Enter password for the second login
error = True
attempts = 5
while error:
	try:
		password_2_elem = driver.find_element_by_id("txtPassword")
		password_2_elem.clear()
		password_2_elem.send_keys(second_password)
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not enter second password.")
		attempts -= 1

# Click submit button for the second login
error = True
attempts = 5
while error:
	try:
		driver.find_element_by_id("Button1").click()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not click submit button.")
		attempts -= 1

print("Second authentication completed.\n")

# Wait for the next page to load
time.sleep(5)

#---------------------------------------------------------------------------------#

print("Accessing the REA values page...")

# Click on the text "Liquidación, Facturación y Pago"
error = True
attempts = 5
while error:
	try:
		driver.find_element_by_link_text("Liquidación, Facturación y Pago").click()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not click text \"Liquidación, Facturación y Pago\".", logout_tabs = 1)
		attempts -= 1

# Click on the text "Garantías"
error = True
attempts = 5
while error:
	try:
		driver.find_element_by_link_text("Garantías").click()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not click text \"Garantías\".", logout_tabs = 1)
		attempts -= 1

# Click on the text "REA y Monto Garantizado de Pago"
error = True
attempts = 5
while error:
	try:
		driver.find_element_by_link_text("REA y Monto Garantizado de Pago").click()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not click text \"REA y Monto Garantizado de Pago\".", logout_tabs = 1)
		attempts -= 1

print("REA values page accessed.\n")

# Switch to the new tab and wait for it to load
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
#---------------------------------------------------------------------------------#

print("Obtaining REA values...")

table = driver.find_element_by_id("tablaResultado_wrapper").find_element_by_tag_name("table")
values = table.find_element_by_tag_name("tbody").find_element_by_tag_name("tr").find_elements_by_tag_name("td")
table_2 = driver.find_element_by_id("tablaResultado2_wrapper").find_element_by_tag_name("table")
values_2 = table_2.find_element_by_tag_name("tbody").find_element_by_tag_name("tr").find_elements_by_tag_name("td")
table_3 = driver.find_element_by_id("tablaResultado3_wrapper").find_element_by_tag_name("table")
values_3 = table_3.find_element_by_tag_name("tbody").find_element_by_tag_name("tr").find_elements_by_tag_name("td")

# Get Factor Volatilidad value
print("FV")

error = True
attempts = 5
while error:
	try:
		FV_value = driver.find_element_by_id("panelresultados").find_elements_by_tag_name("div")[3].find_element_by_tag_name("p").get_attribute("innerHTML")
		FV_value = FV_value.replace("Factor Volatilidad:", "").strip()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get Factor Volatilidad value.", logout_tabs = 2)
		attempts -= 1

# Get OOPM value
error = True
attempts = 5
while error:
	try:
		OOPM_value = str(values_2[2].get_attribute("innerHTML"))
		OOPM_value = OOPM_value.replace(",", "").replace("$", "").strip()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get OOPM value.", logout_tabs = 2)
		attempts -= 1

# Get OPC value
error = True
attempts = 5
while error:
	try:
		OPC_value = str(values_2[3].get_attribute("innerHTML"))
		OPC_value = OPC_value.replace(",", "").replace("$", "").strip()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get OPC value.", logout_tabs = 2)
		attempts -= 1

# Get CPMCP value
error = True
attempts = 5
while error:
	try:
		CPMCP_value = str(values_3[2].get_attribute("innerHTML"))
		CPMCP_value = CPMCP_value.replace(",", "").replace("$", "").strip()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get CPMCP value.", logout_tabs = 2)
		attempts -= 1

# Get CPMTDO value
error = True
attempts = 5
while error:
	try:
		CPMTDO_value = str(values_3[3].get_attribute("innerHTML"))
		CPMTDO_value = CPMTDO_value.replace(",", "").replace("$", "").strip()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get CPMTDO value.", logout_tabs = 2)
		attempts -= 1

# Get TMP value
error = True
attempts = 5
while error:
	try:
		TMP_value = str(values_3[9].get_attribute("innerHTML"))
		TMP_value = TMP_value.replace(",", "").replace("$", "").strip()
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get TMP value.", logout_tabs = 2)
		attempts -= 1

# Get REA value
error = True
attempts = 5
while error:
	try:
		rea_value = str(values[4].get_attribute("innerHTML"))
		rea_value = rea_value.strip().replace(",", "").replace("$", "")
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get REA value.", logout_tabs = 2)
		attempts -= 1

# Get Pasivo Potencial value
error = True
attempts = 5
while error:
	try:
		pasivo_potencial_value = str(values[3].get_attribute("innerHTML"))
		pasivo_potencial_value = pasivo_potencial_value.strip().replace(",", "").replace("$", "")
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get Pasivo Potencial value.", logout_tabs = 2)
		attempts -= 1

# Get Pasivo Potencial value
error = True
attempts = 5
while error:
	try:
		pasivo_conocido_value = str(values[2].get_attribute("innerHTML"))
		pasivo_conocido_value = pasivo_conocido_value.strip().replace(",", "").replace("$", "")
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get Pasivo Potencial value.", logout_tabs = 2)
		attempts -= 1

"""
# Get REA value
error = True
attempts = 5
while error:
	try:
		rea_value = str(driver.find_element_by_id("rea").get_attribute("innerHTML"))
		rea_value = rea_value.replace(",", "").replace("$", "")
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get REA value.", logout_tabs = 2)
		attempts -= 1

# Get Pasivo Potencial value
error = True
attempts = 5
while error:
	try:
		pasivo_potencial_value = str(driver.find_element_by_id("pasivoPotencial").get_attribute("innerHTML"))
		pasivo_potencial_value = pasivo_potencial_value.replace(",", "").replace("$", "")
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get Pasivo Potencial value.", logout_tabs = 2)
		attempts -= 1

# Get Pasivo Potencial value
error = True
attempts = 5
while error:
	try:
		pasivo_conocido_value = str(driver.find_element_by_id("pasivoConocido").get_attribute("innerHTML"))
		pasivo_conocido_value = pasivo_conocido_value.replace(",", "").replace("$", "")
		error = False
	except Exception:
		if attempts == 0:
			finish_web_scraping("Could not get Pasivo Potencial value.", logout_tabs = 2)
		attempts -= 1
"""

print("REA values obtained.\n")

#---------------------------------------------------------------------------------#

"""
Espacio para el código correspondiente para actualizar la base de datos
"""

print("REA:", rea_value)
print("Pasivo potencial:", pasivo_potencial_value)
print("Pasivo conocido:", pasivo_conocido_value)
print("Factor volatilidad:", FV_value)
print("OOPM:", OOPM_value)
print("OPC:", OPC_value)
print("CPMCP:", CPMCP_value)
print("CPMTDO:", CPMTDO_value)
print("TMP:", TMP_value)

finish_web_scraping(logout_tabs = 2, error = False)

update = input("\nUpdate? (y/n): ")

if update.lower() == "y":

	now = datetime.now()

	direccion_servidor = "tcp:beetmann-energy.database.windows.net"
	nombre_bd = "mercados"
	nombre_usuario = "adm"
	password = "MercadosBD20"

	cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER="+direccion_servidor+";DATABASE="+nombre_bd+";UID="+nombre_usuario+";PWD="+password) # Crear conexión con SQL Server
	cursor = cnxn.cursor()

	cursor.execute("""
	INSERT INTO [dbo].[REA_CENACE] 
	([Fecha],[Pasivo conocido],[Pasivo potencial],[REA])
	values(?,?,?,?)""", now, pasivo_conocido_value, pasivo_potencial_value, rea_value)
	cnxn.commit()

	print("Process completed successfully.")

__author__ = "Hedguhar Domínguez González"
__email__ = "hedguhar.dominguez@beetmann.com"


"""
factor de volatilidad
*oopm y opc
cpmcp
cpmtdo
tmp
"""