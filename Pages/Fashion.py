import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.Base import Base


class Fashion(Base):

    def __init__(self, driver):
        super().__init__(driver)

    Fashion  = "//div[text()='Fashion']"
    footwear = "//a[@class='_6WOcW9 _2-k99T']"
    Fashion_product_details = "//a[@class='IRpwTa']"
    fashion_add_to_cart = "//button[text()='ADD TO CART']"
    size = "//a[normalize-space()='S']"
    women_hover = "//span[text()='Women']"
    wishlist = "//div[@class='_36FSn5']"
    saree = "//a[@title='Sarees']"
    saree_product_details = "//a[@class='IRpwTa']"
    My_account = "//div[text()='My Account']"
    wishlist_my = "//a[@href='/wishlist?link=home_wishlist']"
    wishlist_items = "//div[@class='_3hscEA']"


    def fashion_test(self):

        fashion = self.driver.find_element(By.XPATH, self.Fashion)
        action = ActionChains(self.driver)
        Hover = action.move_to_element(fashion).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.footwear).click()
        product_details = self.driver.find_elements(By.XPATH, self.Fashion_product_details)
        for i in product_details:
            print(i.text)
            i.click()
            break
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.XPATH, self.size).click()
        self.driver.find_element(By.XPATH, self.fashion_add_to_cart).click()

    def select_fashion_product_and_add_to_cart(self):

        product_details = self.driver.find_elements(By.XPATH, self.Fashion_product_details)
        product_name = self.check_on_product_and_give_product_name(product_details)
        print("Fashion product name which is added in your cart", product_name)
        self.window_handle()
        self.click_on_element(self.size)
        self.click_on_element(self.fashion_add_to_cart)



    def wishlist_check_fashion(self):
        fashion = self.driver.find_element(By.XPATH, self.Fashion)
        self.hover_on_element(fashion)
        self.click_on_element(self.footwear)
        product_details = self.driver.find_elements(By.XPATH, self.Fashion_product_details)
        product_name1 = self.check_on_product_and_give_product_name(product_details)
        print("product name", product_name1)
        self.window_handle()
        self.click_on_element(self.wishlist)
        women = self.driver.find_element(By.XPATH, self.women_hover)
        self.hover_on_element(women)
        self.click_on_element(self.saree)
        time.sleep(4)
        saree_details = self.driver.find_elements(By.XPATH, self.saree_product_details)
        product_name2 = self.check_on_product_and_give_product_name(saree_details)
        print("product name", product_name2)
        self.window_handle()
        self.click_on_element(self.wishlist)
        my_account = self.driver.find_element(By.XPATH, self.My_account)
        self.hover_on_element(my_account)
        self.click_on_element(self.wishlist_my)
        items_wishlist = self.driver.find_elements(By.XPATH, self.wishlist_items)
        name = []
        for i in items_wishlist:
            name.append(i.text)
        for j in name:
            name2 = j
            print("name2", name2)
            if name2.__contains__(product_name1) or name2.__contains__(product_name2):
                print("wishlist items get matched")
            else:
                print("wishlist items are not matched")

















