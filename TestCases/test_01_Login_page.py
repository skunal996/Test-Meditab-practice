import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.Logger import LogGenerator
from Utilities.ReadConfig import ReadConfig
from PageObjects.Login_page import LoginPage

class Test_Meditab:
    clinic_n = ReadConfig.get_clinic()
    user_n = ReadConfig.get_user()
    password_n = ReadConfig.get_passwd()

    log = LogGenerator.loggen()

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("Meditab - https://iemodemoindia.meditab.com")
    @allure.title("Checking credential error message")
    @allure.story("This is a test case for testing of alert message while entering wrong credentials")
    def test_login_01(self, open_browser):
        self.log.info("Testcase 'Initiated' for Meditab login page")

        self.log.info("Opening the browser")
        self.driver = open_browser
        self.lp = LoginPage(self.driver)

        self.log.info("Fetching the URL")
        self.lp.url()

        self.log.info("Entering the clinic")
        self.lp.enter_clinic(self.clinic_n)
        self.log.info("Entering the username")
        self.lp.enter_username(self.user_n)
        self.log.info("Entering the password")
        self.lp.enter_password(self.password_n)
        self.log.info("Clicking the login button")
        self.lp.click_login_button()

        self.log.info("Checking for confirmation message")
        if self.lp.capture_error_message():
            self.log.info("'Alert': " + str(self.lp.capture_error_message()))
            allure.attach(self.driver.get_screenshot_as_png(), name="Meditab_credential_error",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\Meditab_login_fail.PNG")
            self.log.info("Closing the browser")
            self.log.info("\nTestcase 'verified successfully' for invalid credentials alert\n")
            assert True
        else:
            assert False
