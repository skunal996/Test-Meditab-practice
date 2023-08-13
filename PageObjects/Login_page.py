from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Enter_clinic_cl = (By.XPATH, "/html/body/mtab-login/div[1]/div[2]/div/div/form/div[2]/div[1]/div["
                                 "2]/mtab-input-text/span/input")
    Enter_username_cl = (By.XPATH, "/html/body/mtab-login/div[1]/div[2]/div/div/form/div[2]/div[2]/div["
                                   "2]/mtab-input-text/span/input")
    Enter_password_cl = (By.XPATH, "/html/body/mtab-login/div[1]/div[2]/div/div/form/div[2]/div[3]/div["
                                   "2]/mtab-input-text/span/input")
    Click_login_button_cl = (By.XPATH, "/html/body/mtab-login/div[1]/div[2]/div/div/form/div[2]/div[6]/button")
    Capture_error_message_cl = (By.XPATH, "/html/body/mtab-login/div[1]/div[2]/div/div/form/div[2]/span")

    def __init__(self, login):
        self.driver = login
        self.wait = WebDriverWait(self.driver, 10)

    def url(self):
        self.driver.get("https://iemodemoindia.meditab.com")
        self.wait.until((expected_conditions.visibility_of_element_located(self.Enter_clinic_cl)))

    def enter_clinic(self, clinic_name):
        self.wait.until((expected_conditions.visibility_of_element_located(self.Click_login_button_cl)))
        self.driver.find_element(*LoginPage.Enter_clinic_cl).send_keys(clinic_name)

    def enter_username(self, user_name):
        self.wait.until((expected_conditions.visibility_of_element_located(self.Click_login_button_cl)))
        self.driver.find_element(*LoginPage.Enter_username_cl).send_keys(user_name)

    def enter_password(self, password):
        self.wait.until((expected_conditions.visibility_of_element_located(self.Click_login_button_cl)))
        self.driver.find_element(*LoginPage.Enter_password_cl).send_keys(password)

    def click_login_button(self):
        self.wait.until((expected_conditions.visibility_of_element_located(self.Click_login_button_cl)))
        self.driver.find_element(*LoginPage.Click_login_button_cl).click()

    def capture_error_message(self):
        self.wait.until((expected_conditions.visibility_of_element_located(self.Capture_error_message_cl)))
        try:
            message = self.driver.find_element(*LoginPage.Capture_error_message_cl).text
            print(message)
            return message
        except NoSuchElementException:
            return False
