import pytest

from pageObjects.Login import Login
from pageObjects.SearchProduct import SearchProduct
from pageObjects.AddToCart import AddToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_SearchAndAddToCart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchandaddtocart(self, setup):
        self.logger.info("*************** Logging In ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.login = Login(self.driver)
        self.login.clickMyAccount()
        self.login.clickLogin()
        self.login.inputEmail(self.username)
        self.login.inputPassword(self.password)
        self.login.clickLoginButton()
        self.logger.info("*************** Login Successful ***************")

        self.search = SearchProduct(self.driver)
        self.add = AddToCart(self.driver)
        self.logger.info("*************** Starting Test_003_SearchAndAddToCart ***************")

        self.logger.info("*************** Searching for Product: iPhone ***************")
        self.search.inputProduct("iPhone")
        self.search.searchProduct()
        self.logger.info("*************** Adding Product to Shopping Cart ***************")
        self.add.add_product_to_cart()
        if self.add.confirmProduct1_InCart().text() == "iPhone":
            assert True
        else: assert False

        self.logger.info("*************** Searching for Product: iMac ***************")
        self.search.inputProduct("iMac")
        self.search.searchProduct()
        self.logger.info("*************** Adding Product to Shopping Cart ***************")
        self.add.add_product_to_cart()
        if self.add.confirmProduct2_InCart.text() == "iMac":
            assert True
        else: assert False

        self.logger.info("*************** Test_003_SearchAndAddToCart Successful ***************")
        self.driver.close()



