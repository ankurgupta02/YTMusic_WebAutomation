import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Player_Locators
from utilities.common_helpers import Common_Helpers


class PlayerPage:
    # Page object representing the video player on YouTube Music.

    def __init__(self, driver):
        # Initialize with a Selenium WebDriver instance and get the video element.
        self.driver = driver
        self.common = Common_Helpers(self.driver)
        self.player = self._get_video_element()

    def _get_video_element(self):
        # Retrieve the HTML5 video element from the page using JavaScript and return: video element reference
        return self.driver.execute_script("return document.querySelector('video');")

    def _execute_js(self, command, *args):
        # Execute JavaScript commands on the video element.
        return self.driver.execute_script(f'return arguments[0].{command}', self.player, *args)

    def play(self):
        # Play the video by clicking on the page body (to focus) and invoking play() on the video element.
        self.driver.find_element(By.TAG_NAME, 'body').click()
        self._execute_js("play()")

    def pause(self):
        # Pause the video playback.
        self._execute_js("pause()")

    def get_current_time(self):
        # Get the current playback time of the video in seconds and return: current time in seconds
        return self._execute_js("currentTime")

    def assert_is_playing(self):
        """
        Assert that the video is currently playing.
        Checks that the video is not paused and that the playback time is progressing.
        Raises AssertionError if conditions are not met.
        """
        assert not self._execute_js("paused"), "Video is not playing!"
        start_time = self.get_current_time()
        time.sleep(5)
        end_time = self.get_current_time()
        assert end_time > start_time, (
            "Video is playing but playback time is not progressing; "
            "player controls may be missing or video is stalled."
        )

    def assert_not_playing(self):
        """
        Assert that the video is currently paused.
        Checks that the video is paused and playback time does not advance.
        Raises AssertionError if conditions are not met.
        """
        assert self._execute_js("paused"), "Video is playing!"
        start_time = self.get_current_time()
        time.sleep(5)
        end_time = self.get_current_time()
        assert end_time == start_time, (
            "Video is paused but playback time is progressing; "
            "player controls may be missing or seek-bar is moving."
        )

    def get_current_playing_video_title(self):
        # Get the title of the currently playing video from the player UI and return: video title string
        return self.driver.find_element(By.XPATH, Player_Locators.CURRENT_PLAYING_VIDEO_TITLE).text

    def assert_next_video_title(self, old_title, new_title, video_queue):
        # Assert that the next video is playing by comparing titles.
        assert new_title == video_queue[1] and old_title != new_title, "Next video is not playing."

    def assert_previous_video_title(self, old_title, new_title, video_queue):
        # Assert that the previous video is playing by comparing titles.
        assert new_title == video_queue[0] and old_title == new_title, "Previous video is not playing."

    def click_button(self, button_xpath):
        # Click a button on the player identified by its XPath.
        self.driver.find_element(By.TAG_NAME, 'body').click()
        self.common.wait_for_element_clickable(button_xpath).click()

    def wait_for_ads_to_finish(self, timeout=6):
        """
        Wait for any ads to finish playing before the main video starts.
        Handles both skippable and non-skippable ads. Attempts to click the skip button if available.
        """
        while True:
            is_ad_playing = self.driver.execute_script(
                "return document.querySelector('.ytp-ad-player-overlay') !== null"
            )
            if not is_ad_playing:
                break
            try:
                skip_button = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, Player_Locators.SKIP_BUTTON))
                )
                skip_button.click()
            except TimeoutException:
                # Wait for some time to finish non-skipable ad
                time.sleep(timeout)

    def wait_until_video_ready(self, timeout=10):
        """
        Wait until the video element is ready to play.
        readyState >= 2 means the video has enough data to play the current frame.
        Raises Exception if video is not ready within timeout.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.querySelector('video')?.readyState >= 4")
            )
        except TimeoutException:
            raise Exception("Video did not become ready within the given timeout.")
