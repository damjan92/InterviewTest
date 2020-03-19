from selenium import webdriver
import  os
import utilities.customlogger as cl
import logging
class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstantce(self):

        baseUrl = "https://gallery-app.vivifyideas.com/"
        if self.browser == "ieexplorer":
            pass
            #driver = webdriver.Ie()
        elif self.browser == "chrome":
            #setting chrome
            driverLocation = "C:\\Users\\damja\\Desktop\\Python\\VivifyTest\\libs\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            self.log.info("Running on Chrome")

        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="..\\libs\\geckodriver.exe")
            self.log.info("Running on Firefox")
        else:
            driver = webdriver.Firefox(executable_path="..\\libs\\geckodriver.exe")
            self.log.info("Running on Firefox")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
