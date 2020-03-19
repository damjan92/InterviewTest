from selenium.webdriver.common.by import By
from traceback import print_stack
import utilities.customlogger as cl
import time
import os
import logging

class SeleniumWebDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return  By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        else:
            self.log.warning("Locator type: " + locatorType + "is not supported")
        return False

    def getElement(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            self.log.info("Element is found")
        return element

    def getElements(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
        except:
            self.log.info("Element is found")
        return element



    def elementClick(self, locator, locatorType = 'id'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
        except:
            self.log.info("#CLICK# Element is not found")
            print_stack()

    def sendKeys(self, data, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except:
            self.log.info("Can not send: " + data + " data")
            print_stack()

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element is presented")
                return True
            else:
                self.log.warning("#IsElementPresent# Element is not present")
                return False
        except:
            self.log.warning("## Element is not present")
            print_stack()


