
import pytest

from utils import driverutils
from page import home
import instance
import numpy


def test_bullish_macd_cross(search):

    # Set up the Driver
    driver = driverutils.get_driver(is_windowless=True)
    driver.set_window_size(1350, 900)

    # Initialize the Pages Needed
    page = home.Home(driver)
    url = instance.predefined_scans_base + instance.searches[search]
    # Try the Test
    try:
        driver.get(url)
        assert page.load_page()
        assert page.sort_page()
        matrix = page.make_table()
        return matrix
    # If it fails, let pytest fail
    except Exception as e:
        pytest.fail()
    # Even if it passes or fails, always close the browser at the end
    finally:
        driver.close()


mat = test_bullish_macd_cross("parabolic sar")
print(numpy.asarray(mat))
numpy.savetxt("foo.csv", mat, delimiter=",", fmt="%s",
              newline='\n', header='', footer='', comments='# ', encoding=None)
