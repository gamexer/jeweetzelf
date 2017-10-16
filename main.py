from os import getcwd
from time import sleep
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://chirojezuseik.be/")
while True:
    sleep(100)