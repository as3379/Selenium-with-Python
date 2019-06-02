from selenium import webdriver
import os

class Test():
   def Testmethod(self):
#
        driverLocation = "C:\\Users\\adiwakar\Documents\\Selenium Browser files\Library\\IEDriverServer.exe"
        os.environ["webdriver.driver.ie"]= driverLocation
        driver= webdriver.Ie(driverLocation)
        driver.get("https://google.com")
TT=Test()
TT.Testmethod()

