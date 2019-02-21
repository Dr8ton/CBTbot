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
from selenium.webdriver.support.ui import Select

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

SKILLS = [
    'A1 Integrated Out of the Hospital Scenario sp18',
    'A2 Integrated Out of the Hospital Scenario sp18'
    ]

URL = 'https://acadian.csod.com/EPM/POC/ManageChecklist.aspx?tab_page_id=-500200'

browser = webdriver.Chrome()
browser.get(URL)


def main():
    login()

   # find how many skills on page

    for s in SKILLS: 
        try:    
            listOfAllInstancesOfOneSkill = findAllOfOneSkill(s)
        except:
            print "Unable to find: " + s
            continue
        for l in listOfAllInstancesOfOneSkill:

            clickSkill(s)
            for i in range(5):

                subSkill(i)

                validateCompetency()

                alert = browser.switch_to_alert()
                time.sleep(3)

                setOptionAsComplete()
                clickSave()
                clickBack()

#critical critirea
            clickCriticalCriterea()
            validateCompetency()
            alert = browser.switch_to_alert()
            time.sleep(3)
            clickSave()
            clickBack()
            clickMainMenu()

def findAllOfOneSkill(skill): 
    print "Trying to find: " + skill
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, skill)))
    skill = browser.find_elements_by_link_text(skill)
    return skill;

def login():
    userName = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "userNameBox")))
    password = browser.find_element_by_id('passWordBox')
    userName.send_keys('dkittelnemsa')
    password.send_keys('BigGreenWeenie@1')
    browser.find_element_by_id("submit").click()


def clickSave():
    saveBtn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_dlgEditValidation_btnSaveValidation")))
    saveBtn.click()
  # browser.find_element_by_id('ctl00_ContentPlaceHolder1_dlgEditValidation_btnSaveValidation').click()
    return;

def clickBack():
	backBtn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_btnBack")))
	backBtn.click()
	return; 

def setOptionAsComplete():
	select = Select(browser.find_element_by_id("ctl00_ContentPlaceHolder1_dlgEditValidation_ddlRating"))
	select.select_by_visible_text("1 - Complete")
	return; 

def clickCriticalCriterea():
	ccLink = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Critical Criteria")))
	ccLink.click()
	return; 

def validateCompetency():
	validate = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Validate Competency")))
	validate.click()
	return; 

def clickMainMenu(): 
	WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Manage Observation Checklists"))).click()
	return; 

def subSkill(j):
    numAsString = str(j)
    skillStr = "ctl00_ctl00_ContentPlaceHolder1_ChecklistContent_ucCompetencyList_rptCompetencies_ctl0" + numAsString + "_lnkCompetencyName"   
    print skillStr 
    subskill = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, skillStr)))
    subskill.click()
    return;

def subSkill2():
    subskill = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_ContentPlaceHolder1_ChecklistContent_ucCompetencyList_rptCompetencies_ctl01_lnkCompetencyName")))
    subskill.click()
    return;

def clickSkill(skillStr):
    skill = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, skillStr)))
    skill.click()

if __name__== "__main__":
    main()

#course = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Launch")))
#course.click()

#browser = browser.switch_to_alert()

