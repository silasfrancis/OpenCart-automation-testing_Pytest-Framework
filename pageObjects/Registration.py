from selenium.webdriver.common.by import By

class Registration:
    my_account_drp_homepage_xpath = "//i[@class='fa fa-user']"
    register_xpath = "//a[normalize-space()='Register']"
    firstname_xpath = "//input[@id='input-firstname']"
    lastname_xpath = "//input[@id='input-lastname']"
    email_xpath = "//input[@id='input-email']"
    telephone_xpath = "//input[@id='input-telephone']"
    password_xpath = "//input[@id='input-password']"
    confirm_password_xpath = "//input[@id='input-confirm']"
    privacy_policy_xpath = "//input[@name='agree']"
    continue_registration_xpath = "//input[@value='Continue']"
    account_create_notif_xpath = "//*[@id='content']/h1"
    click_continue_xpath = "//a[normalize-space()='Continue']"
    # my_account_drp_xpath = "//a[@title='My Account']"
    # logout_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"
    logout_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"
    continue_logout_xpath = "//a[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.my_account_drp_homepage_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.register_xpath).click()

    def setFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lname)

    def InputEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def inputPhoneNo(self, phoneNo):
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(phoneNo)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def confirmPassword(self, password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password)

    def clickPPcheckbox(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_xpath).click()

    def contineRegistration(self):
        self.driver.find_element(By.XPATH, self.continue_registration_xpath).click()

    def confirmRegistation(self):
        reg_confirm = self.driver.find_element(By.XPATH, self.account_create_notif_xpath)
        return reg_confirm

    def continueReg(self):
        self.driver.find_element(By.XPATH, self.click_continue_xpath).click()

    def logOut(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        self.driver.find_element(By.XPATH, self.continue_logout_xpath).click()


