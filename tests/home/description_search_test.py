from pages.home.description_search_page import Description_search
from utilities.test_status import Status
from ddt import ddt, data, unpack

import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SearchByDescTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sdt = Description_search(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_search(self):
        self.sdt.search("Djole")
        result = self.sdt.succesful_search()
        self.ts.mark_final("Test search by description text", result, "Test is successful")

    @pytest.mark.run(order = 1)
    def test_search(self):
        self.sdt.search("postman")
        result = self.sdt.succesful_search()
        self.ts.mark_final("Test search by description text", result, "Test is successful")









