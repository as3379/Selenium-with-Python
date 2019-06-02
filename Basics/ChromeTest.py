from selenium import webdriver
import os

#class Test():
#    def Testmethod(self):
#         driver = webdriver.Chrome(
#             executable_path="C:\\Users\\adiwakar\Documents\\Selenium Browser files\Library\\chromedriver.exe")
#         driver.get("https://google.com")
# TT=Test()
# TT.Testmethod()
        driverLocation = "C:\\Users\\adiwakar\Documents\\Selenium Browser files\Library\\chromedriver.exe"
        os.environ["webdriver.driver.chrome"]= driverLocation
        driver= webdriver.Chrome(driverLocation)
        driver.get("https://google.com")
TT=Test()
TT.Testmethod()

