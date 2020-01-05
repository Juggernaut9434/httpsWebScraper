# Mike Mathews on Jan 4, 2020

from utils import mikeutils

class Home:

    _logoCSS = "#nav-upper > a > img:nth-child(1)"
    _chartAndToolNavCSS = "#navbar-menuCollapse > ul:nth-child(1) > li:nth-child(1) > a"
    _volControlCSS = "#scc-scans-resultstable > thead > tr > th:nth-child(10)"
    _resultsCSS = "#resultcount > span"
    volumeControl = None

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        # Finds the Logo on the page
        mikeutils.wait_until_present_css(self.driver, self._logoCSS)
        # Finds the Navigation bar on the page
        mikeutils.wait_until_present_css(self.driver, self._chartAndToolNavCSS)
        # Allow scenarios to have an assert
        return True

    def sort_page(self):
        self.volumeControl = mikeutils.wait_until_present_css(self.driver, self._volControlCSS)
        # Click twice
        self.volumeControl.click()
        self.volumeControl.click()

        return True

    def make_table(self, vol=500000):
        matrix = [['Symbol', "Sector", "Close", "Volume"]]
        results = mikeutils.wait_until_present_css(self.driver, self._resultsCSS)
        resultstext = int(results.text)
        # start at row 1 to ending at the last row
        for x in range(1, resultstext+1):
            a = []
            # start at column 2 and end at 10
            for y in [2, 5, 9, 10]:
                xpath = '//*[@id="scc-scans-resultstable"]/tbody/tr[{0}]/td[{1}]'\
                    .format(x, y)
                # text = mikeutils.wait_until_present_xpath(self.driver, xpath).text
                text = self.driver.find_element_by_xpath(xpath).text
                a.append(text)
            if y == 10 and int(text) < vol:
                pass
            else:
                matrix.append(a)
        return matrix

# //*[@id="scc-scans-resultstable"]/tbody/tr[11]
# //*[@id="scc-scans-resultstable"]/tbody/tr[1]
