from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chromedriver ="/Users/Lenovo/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

inputs = browser.find_element_by_xpath('//input[@name="username"]')
inputs.click()
inputs.send_keys('Email')

ayush = browser.find_element_by_xpath('//input[@name="password"]')
ayush.click()
ayush.send_keys('password')

a = browser.find_element_by_xpath('//button[@type="submit"]')
a.click()

sleep(5)
b = browser.find_element_by_xpath('//button[text()="Not Now"]')
b.click()
body_elem = browser.find_element_by_tag_name('body')






yashu = browser.find_element_by_xpath('//a[text()="See All"]')
yashu.click()
sleep(2)
cs = browser.find_elements_by_xpath('//button[text()="Follow"]')
for c in cs:
	c.click()
	sleep(2)




