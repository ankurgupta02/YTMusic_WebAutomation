import pytest
from pages.login_page import LoginPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen
from pages.elements import Elements

class TestLoginPage:
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_page_objects(self, setup):
        """Initialize driver and LoginPage object before each test."""
        self.driver = setup
        self.driver.get(ReadConfig.get_application_url())
        self.login_page = LoginPage(self.driver)

    def _perform_sign_in(self):
        """Helper method to perform sign-in and sign-out."""
        self.login_page.set_email(self.username)
        self.login_page.click_next_button()
        self.login_page.set_password(self.password)
        self.login_page.click_next_button()
        self.login_page.click_avatar()
        self.login_page.click_sign_out()
        self.login_page.assert_sign_in_button_visible()

    def test_home_page_title(self):
        """Verify the home page title."""
        self.logger.info("Test_001_Login: Verify Home Page Title")
        self.login_page.assert_page_title(Elements.EXPECTED_TITLE)
        self.logger.info("Page Title Test Passed.\n")

    def test_sign_in(self):
        """Verify sign in from default state."""
        self.logger.info("Verify Sign In")
        self.login_page.click_sign_in()
        self._perform_sign_in()
        self.logger.info("Sign In Test Passed.\n")

    def test_sign_in_left_panel_guide_expanded(self):
        """Verify sign in when left panel guide is expanded."""
        self.logger.info("Verify Sign In with Left Panel Guide Expanded")
        if not self.login_page.is_left_panel_guide_text_displayed():
            self.login_page.click_guide_icon()
        self.login_page.click_sign_in_left_guide_expanded()
        self._perform_sign_in()
        self.logger.info("Sign In Test Passed when Left Panel Guide Expanded.\n")

    def test_sign_in_left_panel_guide_collapsed(self):
        """Verify sign in when left panel guide is collapsed."""
        self.logger.info("Verify Sign In with Left Panel Guide Collapsed")
        if self.login_page.is_left_panel_guide_text_displayed():
            self.login_page.click_guide_icon()
        self.login_page.click_sign_in_left_guide_collapsed()
        self._perform_sign_in()
        self.logger.info("Sign In Test Passed when Left Panel Guide Collapsed.\n")