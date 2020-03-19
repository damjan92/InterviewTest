from pages.home.search_page import Description_search
from utilities.test_status import Status
from ddt import ddt, data, unpack
from utilities.read_data import getCSVdata



import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class SearchByDescTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sdt = Description_search(self.driver)
        self.ts = Status(self.driver)

    # @pytest.mark.run(order=2)
    # def test_search(self):
    #     self.sdt.search("Djole")
    #     result = self.sdt.succesful_search()
    #     self.ts.mark_final("Test search by description text", result, "Test is successful")

    @pytest.mark.run(order = 1)
    @data(*getCSVdata("C:\\Users\\damja\\Desktop\\Python\\VivifyTest\\test_data.csv"))
    @unpack
    def test_search(self,description):
        self.sdt.search(description)
        result = self.sdt.succesful_search()
        self.ts.mark_final("Test search by description text", result, "Test is successful")




# Run test
# py.test -s -v tests\home\search_test.py --browser firefox




