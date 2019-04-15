#!/bin/python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import getpass
import time
import sys
import subprocess

login_id = sys.argv[1]
password = getpass.getpass("Password: ")

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

def rub_login(id,password):
	driver.get("https://login.rz.ruhr-uni-bochum.de/cgi-bin/start?nocheck=1")
	driver.find_element_by_name("loginid").send_keys(id)
	driver.find_element_by_name("password").send_keys(password)
	driver.find_element_by_name("action").click()
	if "gelungen" in driver.page_source:
		print("[✓] Login succeeded")
	else:
		print("[x] Login failed. Restart script")
		driver.quit()
		exit()

	ping_response = subprocess.call(["/bin/ping", "-c1", "-w100", "1.1.1.1"], stdout=subprocess.PIPE)
	while(ping_response == 0):
		print("[✓] Still connected")
		time.sleep(60)
		ping_response = subprocess.call(["/bin/ping", "-c1", "-w100", "1.1.1.1"], stdout=subprocess.PIPE)

	rub_login(id,password)

if __name__ == "__main__":

	rub_login(login_id,password)
