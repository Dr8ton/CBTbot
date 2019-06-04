#http://selenium-python.readthedocs.io/
#https://seleniumhq.github.io/selenium/docs/api/py/api.html
#https://automatetheboringstuff.com/chapter18/


from selenium import webdriver

import pyautogui
import time


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


browser = webdriver.Chrome()
browser.get('https://central.acadian.com/Intranet/LogIn.aspx?ReturnUrl=%2fIntranet%2fTools%2fSoftware%2fAcadianUniversitySso.aspx')

userName = browser.find_element_by_id('txtUsername')

password = browser.find_element_by_id('txtPassword')

userName.send_keys('NEEDS SECRET KEY FILE')

password.send_keys('NEEDS SECRET KEY FILE')

browser.find_element_by_id("btnLogin").click()

course = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Launch")))
course.click()

browser = browser.switch_to_alert()

#install flash player

#click to allow flash player again. 




while  True:
	if list(pyautogui.locateAllOnScreen('check2.png', grayscale=True)):
		print 'check 2 found'
		pyautogui.click(520, 121, button='left')
	elif list(pyautogui.locateAllOnScreen('check1.png', grayscale=True)):
		print 'check 1 found'
		pyautogui.click(520, 121, button='left')
	elif list(pyautogui.locateAllOnScreen('check3.png', grayscale=True)):
		print 'check 3 found'
		pyautogui.click(520, 121, button='left')
	elif list(pyautogui.locateAllOnScreen('check4.png', grayscale=True)):
		print 'check 4 found'
		pyautogui.click(520, 121, button='left')
	elif list(pyautogui.locateAllOnScreen('check5.png', grayscale=True)):
		print 'check 5 found'
		pyautogui.click(881, 118, button='left')
	elif list(pyautogui.locateAllOnScreen('check6.png', grayscale=True)):
		print 'check 6 found'
		pyautogui.click(881, 118, button='left')
	else: 
		print 'check not found'


	#time.sleep(3)
	#pyautogui.click(521, 166, button='left')
	#print('click')
