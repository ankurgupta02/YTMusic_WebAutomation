import logging
import os

class LogGen:
    _logger = None  # Class-level cache
    @staticmethod
    def loggen():
        if LogGen._logger:
            return LogGen._logger  # Return existing logger if already created

        logger = logging.getLogger("YTMusicLogger")
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers if loggen() is called multiple times
        if not logger.handlers:
            # Construct log path relative to project root
            log_path = os.path.join(os.getcwd(), "logs", "automation.log")
            os.makedirs(os.path.dirname(log_path), exist_ok=True)

            # File handler
            file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Optional: Add console output too
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        LogGen._logger = logger
        return logger