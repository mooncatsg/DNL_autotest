# -*- coding: utf-8 -*-

import os
import sys
import time
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def log(msg):
   print (time.strftime("%H:%M:%S") + ": " + msg)

# appium_URL = 'http://appium.testdroid.com/wd/hub'
#
# desired_caps = {}
# desired_caps['testdroid_username'] = 'vukongminh@gmail.com'
# desired_caps['testdroid_password'] = 'xxxxxxxx'
# desired_caps['testdroid_target'] = 'chrome'
# desired_caps['testdroid_project'] = 'Appium Chrome'
# desired_caps['testdroid_testrun'] = 'TestRun 1'
# desired_caps['testdroid_device'] = 'Asus Google Nexus 7 (2013) ME571KL'
# desired_caps['platformName'] = 'android'
# desired_caps['deviceName'] = 'AndroidDevice'
# desired_caps['browserName'] = 'chrome'
#
# log ("WebDriver request initiated. Waiting for response, this may take a while.")
# driver = webdriver.Remote(appium_URL, desired_caps)

# create a new Firefox session
# capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
opts = Options()
# opts.set_capability("deviceName", "iPhone")
#
# presets = [
#     {
#         "key": "480x800",
#         "name": "Google Nexus one",
#         "width": 480,
#         "height": 800
#     }
# ]
#
# profile = webdriver.FirefoxProfile()
# profile.set_preference('devtools.responsiveUI.presets', json.dumps(presets))
# driver = webdriver.Firefox(options = opts)
# driver = webdriver.Firefox(firefox_profile = profile)
mobile_emulation = {
    "deviceMetrics": { "width": 500, "height": 780, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
# mobile_emulation = { "deviceName": "Nexus 6" }
chrome_options = Options()
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("disable-infobars")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
prefs = { "credentials_enable_service": False,
          "profile": {
             "password_manager_enabled": False
          }
}
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options = chrome_options)
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# driver.set_window_position(20,20)
# driver.set_window_position(0, 0)
# driver.set_window_size(360, 640)

# navigate to the application home page
driver.get("https://dev.dev.cargolink.vn/login")

# get the search textbox
login_field = driver.find_element_by_xpath("//input[@type='tel']")
pass_field = driver.find_element_by_xpath("//input[@type='password']")
role_radio = driver.find_element_by_xpath("//div[@role='radio'][1]")
login_field.clear()
pass_field.clear()

# enter search keyword and submit
login_field.send_keys("983974528")
pass_field.send_keys("Admin123")
role_radio.click()

current_url = driver.current_url
pass_field.send_keys(Keys.ENTER)

WebDriverWait(driver, 5).until(EC.url_changes(current_url))
# create_order_btn = driver.find_element_by_xpath("//button[@type='button'][2]")
create_order_btn = driver.find_element_by_xpath("//*[@id='shippers']/div/header/div/div/a/button")

current_url = driver.current_url
create_order_btn.click()
WebDriverWait(driver, 5).until(EC.url_changes(current_url))

log("Tạo yêu cầu vận chuyển")

# name_cargo_field = driver.find_element_by_xpath("//*[@id='new-request-steps']/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div[1]/div[1]/label/div/div[1]/div/input")
name_cargo_field = driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[1]//input")

name_cargo_field.send_keys(u"Gạo")

# type_of_cargo = driver.find_element_by_xpath('//*[@id="new-request-steps"]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/label/div')
type_of_cargo = driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[2]")
log(type_of_cargo.get_attribute('innerHTML'))
type_of_cargo.click()

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='q-virtual-scroll__content']//div[@class='q-item__label'][contains(text(), 'nông')]"))).click()

amount_field = driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[3]//input")
amount_field.send_keys(5)

unit_of_cargo = driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[4]")
unit_of_cargo.click()

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='q-virtual-scroll__content']//div[@class='q-item__label'][contains(text(), 'Bao')]"))).click()

amount_field = driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[5]//input")
amount_field.send_keys(5)

driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[6]//input").send_keys(2)
driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[7]//input").send_keys(2)
driver.find_element_by_xpath("(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[8]//input").send_keys(2)

driver.find_element_by_xpath('//*[@id="new-request-steps"]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div[6]/div/div/div/div[2]').click()

driver.find_element_by_xpath('//*[@id="new-request-steps"]/div/div[2]/div/div/div/div/div/div[1]/div[2]/button').click()

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="new-request-steps"]//div[contains(text(), "Địa điểm bốc hàng")]')))

load_location = driver.find_element_by_xpath('//*[@id="origin"]')
load_location.send_keys(u'Hà Nội')

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "pac-container")]')))
driver.find_element_by_xpath('//div[contains(@class, "pac-container")]//span[contains(text(), "Hanoi")][1]').click()
# /html/body/div[3]/div[1]/span[2]/span


# close the browser window
log("Finish")
# driver.quit()
