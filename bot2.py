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
time.sleep(15)

handles = browser.window_handles

browser.switch_to_window(handles[1])
time.sleep(5)

frame = browser.find_element_by_id('lesson')
browser.switch_to.frame(frame)

#browser.find_element_by_id('Stage_whiteness_opening_screen_beginbutton').click()
#beginBtn = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "Stage_whiteness_opening_screen_beginbutton_Text2")))
#beginBtn.click()
while True:
    	timeLeft = browser.find_element_by_id("Stage_timeremaining")
    	time.sleep(3)
    	if timeLeft.text == "-0:00":
    		print "time is up"
    		nextBtn = browser.find_element_by_id('Stage_nextbutton_nextpulse_next22')
    		nextBtn.click()
    	else:
    		print "time still remains"
	


