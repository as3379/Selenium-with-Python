from selenium import webdriver
import os

class Test():
    def Testmethod(self):
        driver = webdriver.Firefox(
                 executable_path="C:\\Users\\adiwakar\\Documents\\Selenium Browser files\\Library\\geckodriver.exe")
        driver.get("https://google.com")
TT=Test()
TT.Testmethod()
