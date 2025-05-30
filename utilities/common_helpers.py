from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class Common_Helpers:
    # A helper class containing common Selenium WebDriver utility methods to interact with web elements and perform
    # common actions.

    def __init__(self, driver):
        # Initialize the helper with a Selenium WebDriver instance.
        self.driver = driver

    def wait_for_element_visible(self, locator, element="Element", timeout=10):
        """
        Wait until the element specified by the XPath locator is visible on the page.
        :param locator: XPath string to locate the element
        :param element: Friendly name of the element for error messages (default: "Element")
        :param timeout: Maximum time to wait in seconds (default: 10)
        :raises AssertionError: If the element is not visible within the timeout
        :return: The visisble WebElement
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            assert False, f"Either {element} didn't load on page or missing on the page."

    def wait_for_element_clickable(self, locator, element="Element", timeout=10):
        """
        Wait until the element specified by the XPath locator is clickable on the page.
        :param locator: XPath string to locate the element
        :param element: Friendly name of the element for error messages (default: "Element")
        :param timeout: Maximum time to wait in seconds (default: 10)
        :raises AssertionError: If the element is not clickable within the timeout
        :return: The clickable WebElement
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
        except TimeoutException:
            assert False, f"Either {element} was not clickable or is missing on the page."

    def get_a_random_video(self, items):
        # Return a random index (1-based) from the list of items.
        return random.randint(1, len(items))

    def move_and_click_to_element(self, element):
        # Move the mouse cursor to the specified element and perform a click action.
        act = ActionChains(self.driver)
        act.move_to_element(element).click().perform()