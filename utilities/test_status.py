import utilities.customlogger as cl
import logging
from base.selenium_driver import SeleniumWebDriver

class Status(SeleniumWebDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(Status, self).__init__(driver)
        self.result_list = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                self.result_list.append("PASS")
                self.log.info("## Verification successful: " + resultMessage)
            else:
                self.result_list.append("FAILED")
                self.log.error("## Verfitication failed: " + resultMessage)
                self.screenshot(resultMessage)
        except:
            self.result_list.append("FAILED")
            self.log.error("## Verfitication failed: exception occured" )
            self.screenshot(resultMessage)

    def markresult(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def mark_final(self, testName, result, resultMessage):

        self.setResult(result, resultMessage)

        if "FAIL" in self.result_list:
            self.log.error(testName + ": Test Failed")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(testName + ": Test is successful")
            self.result_list.clear()
            assert True == True




