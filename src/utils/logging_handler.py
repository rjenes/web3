from __future__ import annotations

import inspect
from logging import DEBUG, INFO, Formatter, Logger, StreamHandler, getLogger
from sys import stdout


def get_logger(name: str | None = None) -> Logger:
    """Return a stream logger.

    Args:
        name (str): name for logger, defaults to __name__ of caller.

    Returns:
        Logger: Logger object with StreamHandler.
    """
    name = name or inspect.getmodule(inspect.stack()[1].frame).__name__
    logger = getLogger(name)
    logger.setLevel(DEBUG)

    handler = StreamHandler(stdout)
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s][%(levelname)s] | %(message)s"))

    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)

    return logger
