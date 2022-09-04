import os
import re
import time
from datetime import datetime, timedelta

import mechanize
import pyodbc
import requests
from bs4 import BeautifulSoup


URL = 'https://memsim.cenace.gob.mx/produccion/participantes/LOGIN/'

# Define the password and the corresponding file paths for the first authentication
certificate_path = os.path.abspath('certificate.cer')
key_path = os.path.abspath('private_key.key')
first_password = '00Beetmann'

# Define the username and password for the second authentication
user = 'BTMNN'
second_password = 'BTMNSIN'


certificate_file = open('certificate.cer', 'rb')
key_file = open('private_key.key', 'rb')



files = {'uploadCerjjfile0': certificate_file, 'uploadKeyfile0': key_file}
#cert = (certificate_path, key_path)
values = {'txtPrivateKey': first_password}

#ce= (certificate_path, key_path)
r = requests.post(URL, files=files, data=values, verify=False)
# site_request = requests.get(...) --> print(str(site_request.content))
#r = requests.(URL, verify=False)
print(r.text)



"""


br = mechanize.Browser()
br.open("https://memsim.cenace.gob.mx/produccion/participantes/LOGIN/")

# follow second link with element text matching regular expression
#response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)

#print(response1.geturl())
#print(response1.info())  # headers
#print(response1.read())  # body


br.form = br.forms()[0]
#br.form.add_file(file_object=open(certificate_path), id='uploadCer_ClientState"')

#br.add_file(open(certificate_path), 'file', nr=0)

print(br.response().read(), "\n---------------------")


#br['uploadCerfile0'] = open(certificate_path)
br['txtPrivateKey'] = '00Beetmann'
#br[]
"""