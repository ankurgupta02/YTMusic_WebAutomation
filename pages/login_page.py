from pages.locators import Login_Locator
from utilities.common_helpers import Common_Helpers

class LoginPage:
    #Page object for the YouTube Music Login page.

    def __init__(self, driver):
        self.driver = driver
        self.common = Common_Helpers(self.driver)

    def click_sign_in(self):
        """Click the Sign-In button."""
        self.common.wait_for_element_clickable(Login_Locator.SIGN_IN_BUTTON).click()

    def set_email(self, username):
        """Enter the email/username."""
        email_field = self.common.wait_for_element_visible(Login_Locator.EMAIL_ID)
        email_field.clear()
        email_field.send_keys(username)

    def set_password(self, password):
        """Enter the password."""
        password_field = self.common.wait_for_element_visible(Login_Locator.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_next_button(self):
        """Click the Next button."""
        self.common.wait_for_element_clickable(Login_Locator.NEXT_BUTTON).click()

    def assert_sign_in_button_visible(self):
        """Assert that the Sign-In button is visible on the page."""
        is_visible = self.common.wait_for_element_visible(Login_Locator.SIGN_IN_BUTTON).is_displayed()
        assert is_visible, "Sign-In button is not visible on the page."

    def assert_page_title(self, expected_title):
        """Assert that the current page title matches the expected title."""
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Page title mismatch: Expected '{expected_title}', got '{actual_title}'."

    def click_avatar(self):
        """Click the user avatar button."""
        self.common.wait_for_element_clickable(Login_Locator.AVATAR_BUTTON).click()

    def click_sign_out(self):
        """Click the Sign-Out button."""
        self.common.wait_for_element_clickable(Login_Locator.SIGN_OUT_BUTTON).click()

    def is_left_panel_guide_text_displayed(self):
        """Check if the left panel guide text is displayed."""
        return self.common.wait_for_element_visible(Login_Locator.SIGN_IN_TEXT_LEFT_GUIDE).is_displayed()

    def click_guide_icon(self):
        """Click the guide icon on the left panel."""
        self.common.wait_for_element_clickable(Login_Locator.LEFT_GUIDE_BUTTON).click()

    def click_sign_in_left_guide_expanded(self):
        """Click the Sign-In button when the left guide panel is expanded."""
        self.common.wait_for_element_clickable(Login_Locator.SIGN_IN_BUTTON_WHEN_LEFTGUIDE_EXPANDED).click()

    def click_sign_in_left_guide_collapsed(self):
        """Click the Sign-In button when the left guide panel is collapsed."""
        self.common.wait_for_element_clickable(Login_Locator.SIGN_IN_BUTTON_WHEN_LEFTGUIDE_COLLAPSED).click()