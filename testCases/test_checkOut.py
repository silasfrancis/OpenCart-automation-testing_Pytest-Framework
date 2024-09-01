import pytest

from pageObjects.Login import Login
from pageObjects.SearchProduct import SearchProduct
from pageObjects.AddToCart import AddToCart
from pageObjects.Checkout import BillingDetails, DeliveryDetails, DeliveryMethod, PaymentMethod, ConfirmOrder
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_CheckOut:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_checkout(self, setup):
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

        self.logger.info("*************** Searching for Product: iMac ***************")
        self.search.inputProduct("iMac")
        self.search.searchProduct()
        self.logger.info("*************** Adding Product to Shopping Cart ***************")
        self.add.add_product_to_cart()

        self.logger.info("********************* Entering Shopping Cart ************************")
        self.add.clickShoppingCart()

        self.logger.info("********************* Checking Out ************************")
        self.bill = BillingDetails(self.driver)
        self.bill.clickCheckoutBtn()

        self.logger.info("********************* Entering Billing Details ************************")
        self.bill.inputFirstname("Francis")
        self.bill.inputLastname("Silas")
        self.bill.inputCompanyname("Tester")
        self.bill.inputAddress1("No 2 Nigeria")
        self.bill.inputAddress2("No 3 Nigeria")
        self.bill.inputCity("Uyo")
        self.bill.inputPostCode("520113")
        self.bill.SelectCountry("Nigeria")
        self.bill.SelectRegion("Akwa Ibom")
        self.bill.clickContinue()

        self.logger.info("********************* Entering Delivery Details ************************")
        self.deliv = DeliveryDetails(self.driver)
        self.delivm = DeliveryMethod(self.driver)
        self.deliv.clickContinue()
        self.delivm.InputComment("This is a test")
        self.delivm.clickContinue()

        self.logger.info("********************* Setting Payment Method ************************")
        self.payment = PaymentMethod(self.driver)
        self.payment.clickTermsandConditions()
        self.payment.clickContinue()

        self.logger.info("********************* Confirming Order ************************")
        self.orderconfirm = ConfirmOrder(self.driver)
        self.orderconfirm.clickContinueConfirm()
        if self.orderconfirm.orderConfirmation().text() == "Your order has been placed!":
            assert True
        else: assert False
        self.orderconfirm.continueToShopping()
        self.logger.info("********************* Product CheckOut Successful ************************")
        self.logger.info("********************* Test_004_CheckOut Successful ************************")
        self.driver.close()
