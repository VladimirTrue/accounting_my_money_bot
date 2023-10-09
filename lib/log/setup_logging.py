import logging.config
import os

import toml


def _base_setup_logging():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="(%(asctime)s) (%(name)s) (%(levelname)s) > %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)

    logging.basicConfig(level=10, handlers=[console_handler])


def setup_logging(log_config_path: str) -> None:
    if os.path.exists(log_config_path):
        try:
            config = toml.load(log_config_path)
            logging.config.dictConfig(config)
        except ValueError:
            _base_setup_logging()

    else:
        _base_setup_logging()
