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

def finish_web_scraping(msg = "", driver_created=True, logout_tabs = 0, error = False):
	
	#if logout_tabs != 0:
	#close_session(logout_tab = logout_tabs)
	if driver_created:
		driver.quit()
	else:
		print("This version of ChromeDriver is not supported.")
		print("Try to install the version that matches your Google Chrome browser at: https://sites.google.com/chromium.org/driver/")
	if error:
		with open("status.txt", "a") as f:
			f.write("Error: " + msg + "\n")

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


def create_driver():
	"""Create webdriver"""

	global driver
	driver = webdriver.Chrome(options=chrome_options, executable_path=google_driver_path)


def connect_to_website():
	"""Establish connection to the website"""

	driver.get("https://memsim.cenace.gob.mx/produccion/participantes/LOGIN/")


def enter_certificate():
	"""Enter certificate for the first login"""
	
	certificate_elem = driver.find_element_by_id("uploadCerfile0")
	certificate_elem.clear()
	certificate_elem.send_keys(certificate_path)


def enter_private_key():
	"""Enter private key for the first login"""
	
	key_elem = driver.find_element_by_id("uploadKeyfile0")
	key_elem.clear()
	key_elem.send_keys(key_path)


def enter_first_pass():
	"""Enter password for the first login"""
	
	password_1_elem = driver.find_element_by_id("txtPrivateKey")
	password_1_elem.clear()
	password_1_elem.send_keys(first_password)


def first_submit():
	"""Click submit button for the first login"""

	driver.find_element_by_id("btnEnviar").click()


def enter_username():
	"""Enter username for the second login"""

	user_elem = driver.find_element_by_id("txtUsuario")
	user_elem.clear()
	user_elem.send_keys(user)


def enter_second_pass():
	"""Enter password for the second login"""
			
	password_2_elem = driver.find_element_by_id("txtPassword")
	password_2_elem.clear()
	password_2_elem.send_keys(second_password)


def second_submit():
	"""Click submit button for the second login"""
	
	driver.find_element_by_id("Button1").click()


def click_LFP():
	"""Click on the text 'Liquidación, Facturación y Pago'"""
	
	driver.find_element_by_link_text("Liquidación, Facturación y Pago").click()


def click_G():
	"""Click on the text 'Garantías'"""
	
	driver.find_element_by_link_text("Garantías").click()


def click_RM():
	"""Click on the text 'REA y Monto Garantizado de Pago'"""
	
	driver.find_element_by_link_text("REA y Monto Garantizado de Pago").click()


def switch_tab():
	"""Switch to the new tab"""

	driver.switch_to.window(driver.window_handles[1])


def get_table_values():
	"""Get table values"""

	global values, values_2, values_3
	table = driver.find_element_by_id("tablaResultado_wrapper").find_element_by_tag_name("table")
	values = table.find_element_by_tag_name("tbody").find_element_by_tag_name("tr").find_elements_by_tag_name("td")
	table_2 = driver.find_element_by_id("tablaResultado2_wrapper").find_element_by_tag_name("table")
	values_2 = table_2.find_element_by_tag_name("tbody").find_element_by_tag_name("tr").find_elements_by_tag_name("td")
	table_3 = driver.find_element_by_id("tablaResultado3_wrapper").find_element_by_tag_name("table")
	values_3 = table_3.find_element_by_tag_name("tbody").find_element_by_tag_name("tr").find_elements_by_tag_name("td")


def get_FV():
	"""Get FV value"""

	global FV_value
	FV_value = driver.find_element_by_id("panelresultados").find_elements_by_tag_name("div")[3].find_element_by_tag_name("p").get_attribute("innerHTML")
	FV_value = FV_value.replace("Factor Volatilidad:", "").strip()


def get_MGP():
	"""Get MGP value"""
	
	global MGP_value
	MGP_value = str(values[1].get_attribute("innerHTML"))
	MGP_value = MGP_value.strip().replace(",", "").replace("$", "")

def get_PC():
	"""Get PC value"""
	
	global PC_value
	PC_value = str(values[2].get_attribute("innerHTML"))
	PC_value = PC_value.strip().replace(",", "").replace("$", "")


def get_PPE():
	"""Get PPE value"""

	global PPE_value
	PPE_value = str(values[3].get_attribute("innerHTML"))
	PPE_value = PPE_value.strip().replace(",", "").replace("$", "")


def get_REA():
	"""Get REA value"""

	global REA_value
	REA_value = str(values[4].get_attribute("innerHTML"))
	REA_value = REA_value.strip().replace(",", "").replace("$", "")


def get_OOPM():
	"""Get OOPM value"""

	global OOPM_value
	OOPM_value = str(values_2[2].get_attribute("innerHTML"))
	OOPM_value = OOPM_value.replace(",", "").replace("$", "").strip()


def get_OPC():
	"""Get OPC value"""

	global OPC_value
	OPC_value = str(values_2[3].get_attribute("innerHTML"))
	OPC_value = OPC_value.replace(",", "").replace("$", "").strip()


def get_CPMCP():
	"""Get CPMCP value"""

	global CPMCP_value
	CPMCP_value = str(values_3[2].get_attribute("innerHTML"))
	CPMCP_value = CPMCP_value.replace(",", "").replace("$", "").strip()


def get_CPMTDO():
	"""Get CPMTDO value"""

	global CPMTDO_value
	CPMTDO_value = str(values_3[3].get_attribute("innerHTML"))
	CPMTDO_value = CPMTDO_value.replace(",", "").replace("$", "").strip()


def get_TMP():
	"""Get TMP value"""

	global TMP_value
	TMP_value = str(values_3[9].get_attribute("innerHTML"))
	TMP_value = TMP_value.replace(",", "").replace("$", "").strip()


def update_db():
	"""Update database if new REA values found"""

	now = datetime.now()
	cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER="+db_server+";DATABASE="+db_name+";UID="+db_user+";PWD="+db_password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT TOP 1 [REA] FROM [dbo].[REA_CENACE] ORDER BY [Fecha] DESC")
	current_rea = str(cursor.fetchone()[0])
	if REA_value != current_rea:
		cursor.execute(
			"""INSERT INTO [dbo].[REA_CENACE] 
			([Fecha], [Pasivo conocido], [Pasivo potencial], [REA], [Factor Volatilidad], [OOPM], [OPC], [CPMCP], [CPMTDO], [TMP], [MGP]) 
			VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
			now, PC_value, PPE_value, REA_value, FV_value, OOPM_value, OPC_value, CPMCP_value, CPMTDO_value, TMP_value, MGP_value)
		cnxn.commit()
		with open("status.txt", "a") as f:
			f.write("REA updated\n --> ")
			f.write("FV: " + FV_value + ", ")
			f.write("PC: " + PC_value + ", ")
			f.write("PPE: " + PPE_value + ", ")
			f.write("REA: " + REA_value + ", ")
			f.write("OOPM: " + OOPM_value + ", ")
			f.write("OPC: " + OPC_value + ", ")
			f.write("CPMCP: " + CPMCP_value + ", ")
			f.write("CPMTDO: " + CPMTDO_value + ", ")
			f.write("TMP: " + TMP_value + ", ")
			f.write("MGP: " + MGP_value + "\n")
		print("REA updated")


def make_action(func, driver_created=True):

	for _ in range(5):
		try:
			func()
			return True
		except: pass
	finish_web_scraping("Could not correctly execute the '" + func.__name__ + "' function", driver_created=driver_created, error=True)

	return False


while True:

	tab = 1

	# Database values
	db_server = "tcp:beetmann-energy.database.windows.net"
	db_name = "mercados"
	db_user = "adm"
	db_password = "MercadosBD20"

	# Define path for the driver
	google_driver_path = os.path.abspath("drivers/chromedriver.exe")

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
	chrome_options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

	# Create the webdriver for Chrome
	if not make_action(create_driver, driver_created=False): continue
	driver.implicitly_wait(30)

	# Establish connection to the website
	print("\nEstablishing connection to the website...")
	if not make_action(connect_to_website):
		time.sleep(60)
		continue
	print("Connection established.\n")
	time.sleep(5) # Wait for the page to load
	
	# Make first login
	print("Performing first authentication...")
	if not make_action(enter_certificate): continue
	if not make_action(enter_private_key): continue
	if not make_action(enter_first_pass): continue
	if not make_action(first_submit): continue
	print("First authentication completed.\n")
	time.sleep(10) # Wait for the next page to load

	# Make second login
	print("Performing second authentication...")
	if not make_action(enter_username): continue
	if not make_action(enter_second_pass): continue
	if not make_action(second_submit): continue
	print("Second authentication completed.\n")
	time.sleep(5) # Wait for the next page to load

	# Access the REA page
	print("Accessing the REA values page...")
	if not make_action(click_LFP): continue
	if not make_action(click_G): continue
	if not make_action(click_RM): continue
	if not make_action(switch_tab): continue
	tab = 2
	print("REA values page accessed.\n")
	time.sleep(5) # Wait for the next page to load

	# Get REA values
	print("Obtaining REA values...")
	if not make_action(get_table_values): continue
	if not make_action(get_FV): continue
	if not make_action(get_MGP): continue
	if not make_action(get_PC): continue
	if not make_action(get_PPE): continue
	if not make_action(get_REA): continue
	if not make_action(get_OOPM): continue
	if not make_action(get_OPC): continue
	if not make_action(get_CPMCP): continue
	if not make_action(get_CPMTDO): continue
	if not make_action(get_TMP): continue
	print("REA values obtained.\n")

	# Update database
	if not make_action(update_db): continue
	
	# Finish process
	finish_web_scraping()
	with open("status.txt", "a") as f:
		f.write("Success\n")
	print("Process completed successfully.")
	
	# Wait 1 hour
	time.sleep(3600)


__author__ = "Hedguhar Domínguez González"
__email__ = "hedguhar.dominguez@beetmann.com"