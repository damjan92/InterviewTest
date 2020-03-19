from base.selenium_driver import SeleniumWebDriver
import utilities.customlogger as cl
import time
import logging

class Description_search(SeleniumWebDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators

    search_box = "//input[@placeholder='Search...']"                                #xpath
    filter_button = "//button[@class='btn btn-outline-secondary input-button']"     #xpath

    succes_search = "box-title"                                                    #class


    def input_text(self, text):
        self.sendKeys(text, self.search_box, locatorType="xpath")

    def search_click(self):
        self.elementClick(self.filter_button, locatorType="xpath")

    def clear_fields(self):
        sbox = self.getElement(locator= self.search_box)
        sbox.clear()

    def search(self, text):
        time.sleep(2)
        #self.clear_fields()
        self.input_text(text)
        time.sleep(2)
        self.search_box

    def succesful_search(self):
        result = self.isElementPresent(self.succes_search, locatorType="class")
        return  result




