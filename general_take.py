# Mike Mathews Jan 5, 2020

import pytest

from utils import driverutils
import general_home
import numpy


url_to_use = "https://stockcharts.com/def/servlet/SC.scan"


def general_take(url):

    # Set up the Driver
    driver = driverutils.get_driver(is_windowless=False)
    driver.set_window_size(1350, 900)

    # Initialize the Pages Needed
    page = general_home.GeneralHome(driver)
    url = url
    # Try the Test
    try:
        driver.get(url)                 # Load the Page that has the table
        matrix = page.load_all_tables()     # create a 3d matrix of all the tables on the page
        return matrix
    # If it fails, let pytest fail
    except Exception as e:
        pytest.fail()
    # Even if it passes or fails, always close the browser at the end
    finally:
        driver.close()


# Call the function
mat = general_take(url_to_use)
print(mat)
# Save it as a csv, note it has some added [] "" '' because it is a 3d matrix.
numpy.savetxt("table.csv", mat, delimiter="\n", fmt="%s",
              newline='\n', header='', footer='', comments='# ', encoding=None)
