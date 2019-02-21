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
    # 'A1 Auto-injector Sp 18',
    # 'A1 Bleeding Control/Shock Management Sp 18',
    # 'A1 BVM VENTILATION OF AN APNEIC ADULT PATIENT Sp 18',
    # 'A1 CARDIAC ARREST MANAGEMENT / AED Sp 18',
    # 'A1 Childbirth Sp 18',
    # 'A1 Glucometer Sp 18',
    # 'A1 Intranasal Medication administration Sp 18',
    # 'A1 JOINT IMMOBILIZATION Sp 18',
    # 'A1 LONG BONE IMMOBILIZATION Sp 18',
    # 'A1 OXYGEN ADMINISTRATION BY NON-REBREATHER MASK Sp 18',
    # 'A1 Patient Assessment/Management - Trauma Sp 18',
    # 'A1 Spinal Immobilization (Supine Patient) Sp 18',
    # 'A1 Supraglottic Airway Device Sp 18',
    # 'A2 Auto-injector Sp 18',
    # 'A2 Bleeding Control/Shock Management Sp 18',
    # 'A2 BVM VENTILATION OF AN APNEIC ADULT PATIENT Sp 18',
    # 'A2 CARDIAC ARREST MANAGEMENT / AED Sp 18',
    # 'A2 Childbirth Sp 18',
    # 'A2 Glucometer Sp 18',
    # 'A2 Intranasal Medication administration Sp 18',
    # 'A2 JOINT IMMOBILIZATION Sp 18',
    # 'A2 LONG BONE IMMOBILIZATION Sp 18',
     'A2 Metered Dose Inhaler and Nebulizer Sp 18',
    # 'A2 OXYGEN ADMINISTRATION BY NON-REBREATHER MASK Sp 18',
    # 'A2 Patient Assessment/Management - Medical Sp 18',
    # 'A2 Patient Assessment/Management - Trauma Sp 18',
    # 'A2 Spinal Immobilization (Supine Patient) Sp 18',
    # 'A2 Supraglottic Airway Device Sp 18',
    'A1 Airway Adjuncts Sp 18',
    'A2 Airway Adjuncts Sp 18',
     'A1 Metered Dose Inhaler and Nebulizer Sp 18',
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

            subSkill()

            validateCompetency()

            alert = browser.switch_to_alert()
            time.sleep(3)

            setOptionAsComplete()
            clickSave()
            clickBack()

# SECONDARY SKILLS 
            subSkill2()

            validateCompetency()

            alert = browser.switch_to_alert()
            time.sleep(3)

            setOptionAsComplete()
            clickSave()
            clickBack()

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

def subSkill():
    subskill = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_ContentPlaceHolder1_ChecklistContent_ucCompetencyList_rptCompetencies_ctl00_lnkCompetencyName")))
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

