import logging
import pathlib

from lib.log.setup import setup_logging


toml_path = pathlib.Path(__file__).parent / 'logging_config.toml'


def get_logger(name: str,
               config_path: str = str(toml_path),
               ) -> logging.Logger:
    """Function for getting the logger with the given name.
    Before initialization of the logger setups process of logging from
    the logger config file.

    Args:
        name (str): The name of the logger. Default practice is to give
            '__name__' as the name of the logger.
        config_path (str): The path to the config file with settings for
            the logger. Default value is path to logging_config.toml in
            log package of project.

    Returns:
        Initialized logger (logging.Logger) with the given name and
            setup from config file.

    """
    setup_logging(log_config_path=config_path)
    return logging.getLogger(name)
