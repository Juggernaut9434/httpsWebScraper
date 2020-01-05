# Mike Mathews on Jan 4, 2020


class GeneralHome:

    _headerXPATH = "//tbody/thead"

    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)

    def load_row(self, body=1, row=1):

        a = []
        col = 1
        while True:
            xpath = "//table[{0}]/tbody/tr[{1}]/td[{2}]".format(body, row, col)
            try:
                text = self.driver.find_element_by_xpath(xpath).text
            except:
                row += 1
                break
            a.append(text)
            col += 1
        return a

    def load_table(self, body=1):
        matrix = []
        row = 1
        while True:
            a = self.load_row(body, row)

            if a == []:
                break

            matrix.append(a)
            row += 1
        return matrix

    def load_all_tables(self):
        mega_matrix = []
        tableset = 1
        while True:
            try:
                table = self.load_table(tableset)
                if table == [[]] or table == []:
                    break
                tableset += 1
            except:
                break
            mega_matrix.append(table)

        return mega_matrix
