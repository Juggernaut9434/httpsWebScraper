
import pytest

from utils import driverutils
from page import general_home
# import instance
import numpy


def general_take(url):

    # Set up the Driver
    driver = driverutils.get_driver(is_windowless=True)
    driver.set_window_size(1350, 900)

    # Initialize the Pages Needed
    page = general_home.GeneralHome(driver)
    url = url
    # Try the Test
    try:
        page.load_page(url)
        matrix = page.load_all_tables()
        return matrix
    # If it fails, let pytest fail
    except Exception as e:
        pytest.fail()
    # Even if it passes or fails, always close the browser at the end
    finally:
        driver.close()


mat = general_take("https://www.w3schools.com/html/html_tables.asp")
numpy.savetxt("bar.csv", mat, delimiter="\n", fmt="%s",
              newline='\n', header='', footer='', comments='# ', encoding=None)
