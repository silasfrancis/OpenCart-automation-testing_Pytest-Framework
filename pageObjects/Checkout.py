from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BillingDetails:
    checkout_btn_xpath = "//a[@class='btn btn-primary']"
    firstname_xpath = "//input[@id='input-payment-firstname']"
    lastname_xpath = "//input[@id='input-payment-lastname']"
    company_xpath = "//input[@id='input-payment-company']"
    address1_xpath = "//input[@id='input-payment-address-1']"
    address2_xpath = "//input[@id='input-payment-address-2']"
    city_xpath = "//input[@id='input-payment-city']"
    postcode_xpath = "//input[@id='input-payment-postcode']"
    country_drp_xpath = "//select[@id='input-payment-country']"
    region_drp_xpath = "//select[@id='input-payment-zone']"
    continue_btn_xpath = "//input[@id='button-payment-address']"

    def __init__(self, driver):
        self.driver = driver

    def clickCheckoutBtn(self):
        self.driver.find_element(By.XPATH, self.checkout_btn_xpath).click()

    def inputFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(fname)

    def inputLastname(self, lname):
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lname)

    def inputCompanyname(self, cname):
        self.driver.find_element(By.XPATH, self.company_xpath).send_keys(cname)

    def inputAddress1(self, address1):
        self.driver.find_element(By.XPATH, self.address1_xpath).send_keys(address1)

    def inputAddress2(self, address2):
        self.driver.find_element(By.XPATH, self.address2_xpath).send_keys(address2)

    def inputCity(self, city):
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)

    def inputPostCode(self, pcode):
        self.driver.find_element(By.XPATH, self.postcode_xpath).send_keys(pcode)

    def SelectCountry(self, country):
        country_drp = Select(self.driver.find_element(By.XPATH, self.country_drp_xpath))
        country_drp.select_by_visible_text(country)

    def SelectRegion(self, region):
        region_drp = Select(self.driver.find_element(By.XPATH, self.region_drp_xpath))
        region_drp.select_by_visible_text(region)

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()


class DeliveryDetails:
    continue_btn_xpath = "//input[@id='button-shipping-address']"

    def __init__(self, driver):
        self.driver = driver

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()


class DeliveryMethod:
    order_comment_xpath = "//textarea[@name='comment']"
    continue_btn_xpath = "//input[@id='button-shipping-method']"

    def __init__(self, driver):
        self.driver = driver

    def InputComment(self, comment):
        self.driver.find_element(By.XPATH, self.order_comment_xpath).send_keys(comment)

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()


class PaymentMethod:
    terms_and_conditions_xpath = "//input[@name='agree']"
    continue_btn_xpath = "//input[@id='button-payment-method']"

    def __init__(self, driver):
        self.driver = driver

    def clickTermsandConditions(self):
        self.driver.find_element(By.XPATH, self.terms_and_conditions_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()

class ConfirmOrder:
    continue_btn_xpath = "//input[@id='button-confirm']"
    order_confirmation_xpath = "//h1[normalize-space()='Your order has been placed!']"
    continue_to_Shopping_xpath = "//a[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def clickContinueConfirm(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()

    def orderConfirmation(self):
        order_confirmation = self.driver.find_element(By.XPATH, self.order_confirmation_xpath)
        return order_confirmation.text()



    def continueToShopping(self):
        self.driver.find_element(By.XPATH, self.continue_to_Shopping_xpath).click()

