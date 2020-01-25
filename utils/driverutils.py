# Mobivity 2019

import os
import tempfile

import pytest
from logzero import logger
from selenium import webdriver


def set_env_var(is_windowless="true"):
    os.environ["RUN_HEADLESS"] = is_windowless.upper()   # The value does not matter, just that it is equal to something


def get_driver(browser="chrome", is_windowless=True):
    # Setting the Environment Variables
    set_env_var(is_windowless=str(is_windowless))
    # Creates a temporary file
    temp_dir = tempfile.mkdtemp()
    # Establishes the logger with the temp file
    logger.info("temp_dir=" + temp_dir)
    # A dictionary for the temporary file
    prefs = {"download.default_directory": temp_dir}

    # Establishing Chrome via Chrome Options
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("prefs", prefs)
    # Sets the driver to headless if environment says to
    if "RUN_HEADLESS" in os.environ and os.environ["RUN_HEADLESS"] == "TRUE".upper():

        # """ Sets and off sets the headless
        driver_options.add_argument('--no-sandbox')
        driver_options.add_argument('--headless')
        driver_options.add_argument('--disable-gpu')
        driver_options.add_argument('--log-level=1')
        # """

    # starts the driver
    driver = __get_driver(browser, driver_options)
    # Allows temp_dir to be downloaded in chrome
    """if "RUN_HEADLESS" in os.environ:
        enable_download_in_headless_chrome(driver, temp_dir)"""

    return driver


def __get_driver(browser, options=None):
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options, executable_path="D:\\User-Mike-Big\\Micha\\chromedriver.exe")
        driver.get("about:blank")
        return driver
    else:
        pytest.fail('only chrome is supported at the moment')