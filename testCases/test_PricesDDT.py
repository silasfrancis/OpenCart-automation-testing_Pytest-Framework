from pageObjects.SearchProduct import SearchProduct
from utilities import ExcelUtils
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class Test_005DDT_Prices:
    baseURL = ReadConfig.getApplicationURL()
    prices_path = ".//TestData/Prices.xlsx"

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.search = SearchProduct(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Login Data')

        for r in range(2, self.rows+1):
            self.productName = ExcelUtils.readData(self.path, 'Prices', r, 1)
            self.prices = ExcelUtils.readData(self.path, 'Prices', r, 2)

            self.txt_search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            if self.txt_search.is_displayed():
                self.search.inputProduct(self.productName)
                self.search.searchProduct()

            self.act_productname = self.driver.find_element(By.XPATH, "//div[@class='product-thumb']//div[2]//div//h4")
            if self.act_productname.text() == self.productName:
                assert True
            else:
                assert False

            self.act_price = self.driver.find_element(By.XPATH, "//div[@class='product-thumb']//div[2]//div//p[2]")
            if self.act_price.text() == self.prices:
                assert True
            else:
                assert False
            self.driver.close()







