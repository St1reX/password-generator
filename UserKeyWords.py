import pathlib
import csv23


class UserKeyWords:
    def __init__(self):
        self.keyword_list = []

    def create_keyword_list(self):
        keyword_list_path = pathlib.Path(__file__).parent.absolute() / 'assets'
        print(keyword_list_path)

        if not keyword_list_path.exists():
            keyword_list_path.mkdir()

        keyword_list_file = keyword_list_path / 'keyword_list.csv'

        with open(keyword_list_file, 'w', newline='') as csv:
            reader = csv23.reader(csv)

            for row in reader:
                self.keyword_list.append(row)

        print(self.keyword_list)


test1 = UserKeyWords()
test1.create_keyword_list()
