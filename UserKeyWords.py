import pathlib
import csv23


class UserKeyWords:

    def __init__(self):
        self.keyword_list_directory = pathlib.Path(__file__).parent.absolute() / 'assets'
        self.keyword_list_file = self.keyword_list_directory / 'keyword_list.csv'

        self.keyword_list = []

        self.create_keyword_list()

    def create_keyword_list(self):
        if not self.keyword_list_directory.exists():
            self.keyword_list_directory.mkdir()

        if not self.keyword_list_file.exists():
            with open(self.keyword_list_file, 'w', newline=''):
                pass

    def fetch_keyword_list_from_file(self):
        with open(self.keyword_list_file, 'r', newline='') as csv_file:
            csv_reader = csv23.reader(csv_file)

            for row in csv_reader:
                self.keyword_list.append(row)
                print(row)


test1 = UserKeyWords()
test1.fetch_keyword_list_from_file()
