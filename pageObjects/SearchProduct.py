from selenium.webdriver.common.by import By

class SearchProduct:
    search_product_xpath = "//input[@placeholder='Search']"
    search_btn_xpath = "//button[@class='btn btn-default btn-lg']"

    def __init__(self, driver):
        self.driver = driver

    def inputProduct(self, product_name):
        self.driver.find_element(By.XPATH, self.search_product_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_product_xpath).send_keys(product_name)

    def searchProduct(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()
