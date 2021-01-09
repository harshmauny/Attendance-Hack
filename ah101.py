import os
import time
import random
import winsound
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

code = sys.argv[1]

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--disable-gpu')
opt.add_argument("--disable-blink-features")
opt.add_argument("--disable-blink-features=AutomationControlled")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 2 
  })
opt.add_experimental_option("excludeSwitches", ['enable-automation'])

link = "https://meet.google.com/" + code

path = os.getcwd() + '\chromedriver.exe'
def s2r(path):
    return fr"{path}"
chrome_path = s2r(path)

## FIELDS TO EDIT ##

YOUR_EMAIL_ADDRESS = "devarsh@gmail.com" # Replace with your EMAIL ADRESS
YOUR_PASSWORD = "YOUR PASSWORD" # Replace with your PASSWORD

####################

driver = webdriver.Chrome(options=opt, executable_path=chrome_path)
driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')

driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(YOUR_EMAIL_ADDRESS)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

time.sleep(5)
driver.find_element_by_name('password').send_keys(YOUR_PASSWORD)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

time.sleep(5)
driver.get(link)
time.sleep(15)

# TURNING OFF CAMERA AND MIC

ActionChains(driver).key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
time.sleep(5)

# CLICKS "JOIN NOW" OR "ASK TO JOIN"
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]').click()
time.sleep(25)

driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]').click()

# CLICKS TURN ON "CAPTIONS"
try:
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[10]/div[3]/div[2]/div').click()
    time.sleep(10)
except:
    print("Restart the Script.")
    driver.quit()
    sys.exit()

def letsRunAgain():
    try:
        captionbox = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[5]')
        inside = captionbox.find_element_by_class_name('iTTPOb')
        text = inside.find_elements_by_class_name('CNusmb')
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for x in text:
            string = x.text.lower()
            print(string)
            for pun in string:
                if(pun in punctuations):
                    string = string.replace(pun, "")
            parts = string.split()
            for strx in parts:
                if(strx == "attendance" or strx == "present" or strx == "enrollment"):
                    print("\n\n## ATTENDANCE ALERT##\n\n")
                    frequency = 2500
                    duration = 5000 #1000ms = 1sec
                    winsound.Beep(frequency,duration)
    except:
        print("No Text")

while(True):
    time.sleep(2)
    letsRunAgain()

sys.stdout.flush()