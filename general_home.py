# Mike Mathews on Jan 5, 2020


class GeneralHome:

    # Initialize the driver in the class
    def __init__(self, driver):
        self.driver = driver

    def load_row(self, table=1, row=1):
        """
        utility function, otherwise it would be too confusing
        :param table: determines which table to read from
        :param row: determines which row to read from
        :return: return the row of the table as an array
        """
        a = []
        col = 1
        while True:
            xpath = "//table[{0}]/tbody/tr[{1}]/td[{2}]".format(table, row, col)
            try:
                text = self.driver.find_element_by_xpath(xpath).text
            except:
                row += 1
                break
            a.append(text)
            col += 1
        return a

    def load_table(self, table=1):
        """
        Adds each row at a time until it doesn't have any more rows / breaks
        :param table: the table being read on the webpage
        :return: the 2d matrix of the table
        """
        matrix = []
        row = 1
        while True:
            a = self.load_row(table, row)

            if a == []:
                break

            matrix.append(a)
            row += 1
        return matrix

    def load_all_tables(self):
        """
        utility function that continues the table reading for all tables on the page
        :return: mega_matrix, a 3d matrix with each table being a row
        """
        mega_matrix = []
        table_set = 1
        while True:
            try:
                table = self.load_table(table_set)
                if table == [[]] or table == []:
                    break
                table_set += 1
            except:
                break
            mega_matrix.append(table)

        return mega_matrix
