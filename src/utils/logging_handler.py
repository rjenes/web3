import logging

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")


class LoggingHandler(object):
    """Handle the logging of the project."""

    def __init__(self, class_name: str):
        """Construct a LoggingHandler instance.

        Args:
            class_name: name of the class to be indicated in the logs.
        """
        self._logger: logging.Logger = logging.getLogger(class_name)
        self._logger.setLevel(logging.DEBUG)
        lsh = logging.StreamHandler()
        lsh.setLevel(logging.DEBUG)
        lsh.setFormatter(FORMATTER)
        if not self._logger.hasHandlers():
            # avoid keep adding handlers and therefore duplicate messages
            self._logger.addHandler(lsh)

    def get_logger(self) -> logging.Logger:
        """Get the _logger instance variable.

        Returns:
            logging.Logger: the logger object.
        """
        return self._logger
