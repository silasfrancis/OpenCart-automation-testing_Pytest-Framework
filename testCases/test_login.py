import pytest
from selenium.webdriver.common.by import By
from pageObjects.Login import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*************** Starting Login Test ***************")
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

        target_locator = self.driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']")
        target_item = "My Account"
        found = False

        while not found:
            if target_locator.text == target_item:
                found = True
                self.logger.info("****************** Login Successful ******************")
                self.logger.info("****************** Test_002_Login Successful ******************")
                self.driver.close()
            else:
                self.logger.info("**************** Login Failed ********************")
                self.driver.close()


