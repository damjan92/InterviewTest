from pages.home.width_page import Width_page
from utilities.test_status import Status
from ddt import ddt, data, unpack
from utilities.read_data import getCSVdata



import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestTheWidth(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.wp = Width_page(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)

    def test_width(self):
        self.wp.check()
        result = self.wp.check()
        self.ts.mark_final("Testing the width", result, "Test is successful")