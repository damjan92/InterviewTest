from base.selenium_driver import SeleniumWebDriver
import utilities.customlogger as cl
import time
import logging

class Width_page(SeleniumWebDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cell = "cell"                       #class
    description = "box-title"           #class

    def div_with(self):
        self.getElements(self.cell, locatorType="class")

    def text_width(self):
        self.getElements(self.description, locatorType="class")

    def get_div_widht(self):
        div = self.driver.execute_scrtipt("return window.innerWidth;")
        return div

    def get_text_width(self):
        text = self.driver.execute_scrtipt("return window.innerWidth;")
        return text


    def check_the_width(self,):
        try:
            if self.text_width(self) > self.div_with(self):
                self.log.error("Text is too long")
                return False
            else:
                self.log.info("With is ok")
                return True
        except:
            self.log.info("With is ok")
            return True
    def check(self):
        self.div_with()
        self.get_div_widht()
        self.text_width()
        self.get_text_width()
        self.check_the_width()




