import time
import unittest
from selenium import webdriver
from Config.config import TestData
from Pages.Appliances import Appliances
from Pages.Base import Base
from Pages.Cart import Cart
from Pages.Fashion import Fashion
from Pages.Home_Link import Home_Link
from Pages.Home_Page import Home_Page
from Pages.Login import Login


class cart_item_verify(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=TestData.Chrome_Executable_Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.Base_Url)

    def test_add_items_and_verify(self):
        login = Login(self.driver)
        home = Home_Page(self.driver)
        fashion = Fashion(self.driver)
        home_link = Home_Link(self.driver)
        appliances = Appliances(self.driver)
        base = Base(self.driver)
        login.login_into_app()
        time.sleep(4)
        home.hover_fashion_and_select_element()
        fashion_product_name = fashion.select_fashion_product_and_add_to_cart()
        home.back_to_old_window()
        base.backward()
        time.sleep(4)
        home.hover_appliances_and_select_element()
        appliances_product_name = appliances.select_appliances_product_and_add_to_cart()
        home.click_on_cart()
        cart = Cart(self.driver)
        name1 = cart.verify_product_name()
        print(name1)
        for j in name1:
            name2 = j
            print(name2)
            if name2.__contains__(fashion_product_name) or name2.__contains__(appliances_product_name):
                print("cart item are matched")
            else:
                print("cart items are not matched")












