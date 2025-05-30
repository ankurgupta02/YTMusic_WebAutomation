import os
from pathlib import Path
import pytest
import undetected_chromedriver as webdriver
from selenium.webdriver.chrome.options import Options
from utilities.custom_logger import LogGen

@pytest.fixture
def setup():
    # Pytest fixture to initialize and yield a Chrome WebDriver instance.

    # Set Chrome options
    options = Options()
    options.add_argument("--guest")  # Run browser in guest mode
    options.add_argument("--disable-sync")  # Disable Chrome sync

    # Initialize Chrome WebDriver with options
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()  # Maximize browser window
    driver.implicitly_wait(5)  # Wait up to 5 seconds for elements to appear

    yield driver  # Provide the driver instance to the test
    driver.close()  # Close the browser window


# ------------------- Pytest Hooks -------------------

# Initialize global logger instance
logger = LogGen.loggen()

# Global reference for pytest-html plugin
pytest_html = None


def pytest_configure(config):
    """
    Hook to configure pytest before running any tests.
    Retrieves a reference to the pytest-html plugin for later use in attaching screenshots.
    """
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


def pytest_sessionstart(session):
    """
    Hook that runs before any tests are executed.
    Cleans up the screenshots folder to avoid stale images from previous runs.
    """
    clean_screenshots_folder()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that is triggered after each test phase (setup/call/teardown).
    If a test fails in the call phase:
    - Captures a screenshot.
    - Attaches it to the HTML report.
    - Logs the failure with assertion error details.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("setup")

    if driver:
        screenshot_path = capture_screenshot(item.name, driver)
        attach_screenshot_to_html(report, screenshot_path)

    # Log assertion failure details
    log_assertion_failure(item.name, call.excinfo)


def pytest_html_report_title(report):
    # Customize the title of the pytest-html report.
    report.title = "YTMusic_WebAutomation Report"


# ------------------- Helper Functions -------------------

def clean_screenshots_folder():
    # Deletes all .png screenshots in the screenshots directory.
    screenshots_dir = get_screenshots_dir()

    if os.path.exists(screenshots_dir):
        for file in os.listdir(screenshots_dir):
            if file.endswith(".png"):
                os.remove(os.path.join(screenshots_dir, file))
    else:
        os.makedirs(screenshots_dir)  # Create the directory if it doesn't exist


def get_screenshots_dir():
    # Returns the absolute path to the screenshots directory.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.abspath(os.path.join(current_dir, "..")), "screenshots")


def capture_screenshot(test_name, driver):
    """
    Captures a screenshot of the browser and saves it to the screenshots folder.
    Args:
        test_name (str): Name of the failed test (used as filename).
        driver (WebDriver): Selenium WebDriver instance.
    Returns:
        str: Full path to the saved screenshot.
    """
    screenshots_dir = get_screenshots_dir()
    file_name = f"{test_name}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    try:
        driver.save_screenshot(file_path)
        logger.info(f"📸 Screenshot captured: {file_path}")
    except Exception as e:
        logger.error(f"Failed to capture screenshot: {e}")

    return file_path


def attach_screenshot_to_html(report, screenshot_path):
    """
    Attaches a clickable screenshot URL to the pytest-html report.
    Args:
        report: Pytest report object.
        screenshot_path (str): Absolute file path to the screenshot.
    """
    if pytest_html and screenshot_path:
        try:
            file_uri = Path(screenshot_path).absolute().as_uri()
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.url(file_uri, name="Screenshot"))
            report.extra = extra
        except Exception as e:
            logger.error(f"Failed to attach screenshot to report: {e}")


def log_assertion_failure(test_name, excinfo):
    """
    Logs detailed information about assertion failures.
    Args:
        test_name (str): The name of the failed test.
        excinfo: Exception info from pytest.
    """
    if excinfo:
        error_type = excinfo.type.__name__
        error_msg = str(excinfo.value)
        logger.error(f"❌ Test Failed: {test_name}")
        logger.error(f"📛 Error Type: {error_type}")
        logger.error(f"📝 Error Message: {error_msg}\n")
