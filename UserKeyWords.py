import os
import pathlib
import sys

import csv23


class UserKeyWords:

    def __init__(self):
        self.keyword_list_directory = pathlib.Path(__file__).parent.absolute() / 'assets'
        self.keyword_list_file = self.keyword_list_directory / 'keyword_list.csv'
        self.keyword_list = []

        self.create_keyword_list()
        self.fetch_keyword_list_from_file()
        self.user_key_word_menu()

    def create_keyword_list(self):
        if not self.keyword_list_directory.exists():
            self.keyword_list_directory.mkdir()

        if not self.keyword_list_file.exists():
            with open(self.keyword_list_file, 'w', newline=''):
                pass

    def fetch_keyword_list_from_file(self):
        try:
            with open(self.keyword_list_file, 'r', newline='') as csv_file:
                csv_reader = csv23.reader(csv_file)
                for row in csv_reader:
                    self.keyword_list.append(row[0])
        except Exception as e:
            print(f"Error reading keyword list: {e}")
            sys.exit()

    def display_keyword_list(self):
        if not self.keyword_list:
            print('Keyword list is empty.')
            print('Add a keyword to your list before displaying it.')
        else:
            print('Keyword list:')
            for keyword in self.keyword_list:
                print(f"> {keyword}")

        input('Press Enter to continue...')

    def save_new_keyword_file(self):
        while True:
            try:
                print('Enter your new keyword')
                keyword = input().strip()

                if keyword == '':
                    raise ValueError("Empty keyword")
                if keyword in self.keyword_list:
                    raise ValueError('Keyword already exists')

                self.keyword_list.append(keyword)

                print(f'Keyword {keyword} saved')
                input('Press Enter to continue...')
                break
            except Exception as e:
                print(f"Error while adding new keyword: {e}")
                print("Provide a valid keyword")
                input('Press Enter to continue...')
                os.system('cls')

    def delete_certain_keyword_file(self):
        if not self.keyword_list:
            print('Keyword list is empty.')
            print('Add a keyword to your list before deleting it.')
        else:
            print('Enter your desired keyword to be deleted')
            keyword = input()

            if keyword not in self.keyword_list:
                print(f'Keyword {keyword} does not exist in keyword list')
            else:
                self.keyword_list.remove(keyword)
                print(f'Keyword {keyword} deleted')

        input('Press Enter to continue...')

    def update_csv(self):
        with open(self.keyword_list_file, 'w', newline='') as csv_file:
            csv_writer = csv23.writer(csv_file)

            for keyword in self.keyword_list:
                csv_writer.writerow([keyword])

    def user_key_word_menu(self):
        while True:
            os.system('cls')

            print('Menu')
            print('1. Add keyword')
            print('2. Remove keyword')
            print('3. Display keywords')
            print('4. Continue to password generation')

            option = input("Choose an option (1-4):\n")

            match option:
                case '1':
                    self.save_new_keyword_file()
                case '2':
                    self.delete_certain_keyword_file()
                case '3':
                    self.display_keyword_list()
                case '4':
                    if not self.keyword_list:
                        print('Keyword list is empty.')
                        print('Add a keyword to your list before generating password. ')
                        input('Press Enter to continue...')
                    else:
                        os.system('cls')
                        self.update_csv()
                        return
                case _:
                    print('Invalid option')
                    input('Press Enter to continue')
