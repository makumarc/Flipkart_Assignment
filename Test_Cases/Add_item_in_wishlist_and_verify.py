import unittest
from selenium import webdriver
from Config.config import TestData
from Pages.Fashion import Fashion
from Pages.Home_Page import Home_Page
from Pages.Login import Login


class wishlist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=TestData.Chrome_Executable_Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.Base_Url)


    def  test_verify_wishlist_items(self):
        login = Login(self.driver)
        login.login_into_app()
        F = Fashion(self.driver)
        F.wishlist_check_fashion()

