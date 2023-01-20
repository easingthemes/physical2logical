import logging

from physical2logical import __name__
from physical2logical.config import Style

custom_levels = ["EMPTY", "SUCCESS", "INFO_"]


def add_logging_level(level_name, level_num, method_name=None):
    if not method_name:
        method_name = level_name.lower()

    def log_for_level(self, message="", *args, **kwargs):
        if level_name == custom_levels[0]:
            print()
            return

        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message="", *args, **kwargs):
        if level_name == custom_levels[0]:
            print()
            return

        logging.log(level_num, message, args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, log_for_level)
    setattr(logging, method_name, log_to_root)


for i, lev_name in enumerate(custom_levels, start=1):
    add_logging_level(lev_name, logging.DEBUG + i)


def format_part(fmt, log_content):
    return f"{fmt}{log_content}{Style.ENDC}"


def format_message(fmt):
    log_header = "[%(name)s]::%(levelname)s::"
    log_file = " (%(filename)s:%(lineno)d)"
    log_message = " %(message)s"

    return format_part(fmt + Style.BOLD, log_header)\
        + format_part(fmt, log_message)\
        + format_part(Style.DEBUG, log_file)


class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: format_message(Style.DEBUG),
        logging.INFO: format_message(""),
        logging.WARNING: format_message(Style.WARNING),
        logging.ERROR: format_message(Style.ERROR),
        logging.SUCCESS: format_message(Style.SUCCESS),
        logging.INFO_: format_message(Style.HIGHLIGHT)
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def create_logger():
    __logger = logging.Logger(__name__)
    __logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setFormatter(CustomFormatter())

    __logger.addHandler(ch)

    return __logger


logger = create_logger()
