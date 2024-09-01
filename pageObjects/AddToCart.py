import time
from selenium.webdriver.common.by import By

class AddToCart:
    add_to_cart_btn = "//button[@class='btn btn-default btn-lg']"
    shopping_cart_xpath = "//a[@title='Shopping Cart']//i[@class='fa fa-shopping-cart']"
    product1_name_xpath = "//body[1]/div[2]/div[1]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]"
    product2_name_xpath = "//body[1]/div[2]/div[1]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]"

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_btn).click()

    def clickShoppingCart(self):
        self.driver.find_element(By.XPATH, self.shopping_cart_xpath).click()
        time.sleep(5)
        self.driver.refresh()

    def confirmProduct1_InCart(self):
        self.driver.find_element(By.XPATH, self.shopping_cart_xpath).click()
        self.driver.refresh()
        time.sleep(5)
        target_locator = self.driver.find_element(By.XPATH, self.product1_name_xpath)
        return target_locator

    def confirmProduct2_InCart(self, product):
        self.driver.find_element(By.XPATH, self.shopping_cart_xpath).click()
        time.sleep(5)
        self.driver.refresh()
        target_locator = self.driver.find_element(By.XPATH, self.product2_name_xpath)
        return target_locator




