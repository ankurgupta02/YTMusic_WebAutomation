import configparser
import os

# Get absolute path to config.ini relative to this file
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini'))
config = configparser.ConfigParser()
config.read(config_path)


class ReadConfig:
    # Utility class to read configuration values from config.ini.
    @staticmethod
    def get_application_url():
        # Retrieves the base application URL from the config file and return: Base URL as a string
        return config.get('common_info', 'base_url')

    @staticmethod
    def get_username():
        # Retrieves the username from the config file and return: Username as a string
        return config.get('credentials', 'username')

    @staticmethod
    def get_password():
        # Retrieves the password from the config file and return: Password as a string
        return config.get('credentials', 'password')

    @staticmethod
    def get_video_url():
        # Constructs the full video URL using base URL and video ID from the config file and return: Full video URL as a string
        video_id = config.get('video_info', 'video_id')
        return ReadConfig.get_application_url() + "watch?v=" + video_id
