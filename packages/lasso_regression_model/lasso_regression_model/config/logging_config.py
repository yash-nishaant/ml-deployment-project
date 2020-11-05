import logging
import sys

# Multiple calls to logging.getLogger('exampleLogger') return a reference within the same module object
# This is true across all modules as long as it is within the same Python interpreter process

FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler
