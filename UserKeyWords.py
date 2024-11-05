import pathlib
import csv23


class UserKeyWords:
    def __init__(self):
        self.keyword_list = []

    @staticmethod
    def create_keyword_list(self):
        keyword_list_path = pathlib.Path(__file__).parent.absolute() / 'assets'

        if not keyword_list_path.exists():
            keyword_list_path.mkdir()

        keyword_list_file = keyword_list_path / 'keyword_list.csv'

        if not keyword_list_file.exists():
            with open(keyword_list_file, 'w', newline='') as new_file:
                pass


test1 = UserKeyWords()
test1.create_keyword_list()
