from selenium.webdriver.common.by import By

class Login:
    my_account_drp_homepage_xpath = "//i[@class='fa fa-user']"
    login_xpath = "//a[normalize-space()='Login']"
    input_email_xpath = "//input[@id='input-email']"
    input_password_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.my_account_drp_homepage_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def inputEmail(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def inputPassword(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

