import logging
import pathlib

from lib.log.setup_logging import setup_logging

log_config = pathlib.Path(__file__).parent / 'log_config.toml'


def get_logger(name: str, config_path: str = str(log_config)) -> logging.Logger:
    setup_logging(log_config_path=config_path)
    return logging.getLogger(name)

