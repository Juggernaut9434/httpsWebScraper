from selenium import webdriver  # Imports the web driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Lets the Web wait until an element is found
from selenium.webdriver.support import expected_conditions as ec  # Used in xwait()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, StaleElementReferenceException  # Used for Try / Except

from time import sleep
from random import randint
import json


# Opens Browser with arguments of headless
def get_driver(headless=False):
    """
    Decide whether you want the driver to headless or not
    :param headless: True or False
    :return: the driver instance
    """
    chrome_options = Options()
    chrome_options.headless = headless
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1350, 900)
    return driver


# Waits for the element to be visible then present on the page
def wait_until_present_xpath(driver, xpath, hold=7, debug=0):
    """
    Wait until the driver has found the element
    :param driver: the browser
    :param xpath: the location of the element in the xpath format
    :param hold: wait for a certain amount of seconds
    :param debug: Whether you want to debug or not
    :return: return the element
    """
    # The new name for past "xwait"
    waiter = WebDriverWait(driver, hold)

    try:
        try:
            waiter.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            if debug != 0:
                print("xpath: " + xpath)
            else:
                pass

        element_found = waiter.until(ec.presence_of_element_located((By.XPATH, xpath)))

        return element_found

    except NoSuchElementException as g:
        raise g

    except TimeoutException as f:
        raise f


# Waits for the element to be visible then present on the page
def wait_until_present_id(driver, id_name, hold=7, debug=0):
    # The waiter allows for an easier call for the explicit waits
    waiter = WebDriverWait(driver, hold)

    try:
        try:
            waiter.until(ec.visibility_of_element_located((By.ID, id_name)))
        except TimeoutException:
            if debug != 0:
                print("id: " + id_name)
            else:
                pass

        element_found = waiter.until(ec.presence_of_element_located((By.ID, id_name)))

        return element_found

    except NoSuchElementException as g:
        raise g

    except TimeoutException as f:
        raise f


# Waits for the element to be visible then present on the page
def wait_until_present_css(driver, css, hold=7, debug=0):
    """
    Waiting and finding an element on a browser
    :param driver: initialized in driverutils.py
    :param css: The location of the element from the css selector
    :param hold: Waiting for how many seconds
    :param debug: If you need to debug, put in 1, else 0
    :return: The element that is found in the browser
    """
    # The new name for past "xwait"
    waiter = WebDriverWait(driver, hold)

    try:
        try:
            waiter.until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except TimeoutException:
            if debug != 0:
                print("css: " + css)
            else:
                pass

        element_found = waiter.until(ec.presence_of_element_located((By.CSS_SELECTOR, css)))

        return element_found

    except NoSuchElementException as g:
        raise g

    except TimeoutException as f:
        raise f


# Scrolls to the top or the bottom of the web page
def scroll_to(driver, place="top"):
    if place == "top":
        driver.execute_script("window.scrollTo(0,0)")
    elif place == "end":
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    else:
        print("only 'top' or 'end'")
        raise ValueError


def wait_for_block_ui_to_disappear(driver, block_ui_xpath='//div[@class="blockUI blockOverlay"]', hold=7):
    try:
        # Waits until the block ui xpath disappears
        waiter = WebDriverWait(driver, hold)

        waiter.until(ec.invisibility_of_element_located((By.XPATH, block_ui_xpath)))
        return True
    except TimeoutException:
        return False


# Clicks the element untils the element works. usually because of Stale Element
def click_until_element_loads(driver, id2, title=None):
    loop = 0
    while driver.title != title:  # loops it b/c was receiving " Element was Stale "
        if loop == 20:
            raise Exception("Load Broken")
        else:
            try:
                g = wait_until_present_id(driver, id2)
                g.click()
                loop = 0
                print(loop)
            except StaleElementReferenceException:
                loop += 1
                print(loop)


# Debug tool to tell you when you are sleeping instead of being a good developer
def sleep_pr(seconds):
    for i in range(seconds):
        sleep(1)
        print("sleeping " + str(i))


# Opens and Returns the json file as a python dict
def get_json_data(name):
    with open(name) as f:
        data = json.load(f)
    return data


# Selects element, clears the text field, and sends the keys
def click_clear_sendkeys_element(element, keys):
    # Used for Text Fields
    element.click()
    element.clear()
    element.send_keys(Keys.HOME)
    element.send_keys(keys)
    return True


# Gives 5 Random characters
def five_random_char():
    text = "_a"   # sting that adds a space to the end of a name
    charset = "abcdefghijklmnopqrstuvwxyz0123456789"    # All available characters for naming

    # Adds a character by random to the empty string text
    for i in range(5):
        text = text + charset[randint(0, len(charset) - 1)]
    return text


# Debugging
def driver_debug(driver, log):
    try:
        log.debug(driver.title + driver.current_url)
    except:
        print(driver.title + " -- " + driver.current_url)


# Alerts
# driver.switch_to.alert.accept() to accept; .dismiss(); .send_keys(); .text() to retrieve keys

# Screenshots of failures?
# driver.save_screenshot("name.png")

const = five_random_char()