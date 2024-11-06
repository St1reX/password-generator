import random
import string
import math


class PasswordGenerator:
    def __init__(self, keyword_list):
        self.password = ""

    def numbers_in_password(self):
        print('Here you can select amount of and position of numbers in password.')

        while True:
            try:
                numbers_amount = int(input('What amount of numbers you want to include in password (Provide number '
                                           'between 1 and 10)?'))
                if numbers_amount < 1 or numbers_amount > 10:
                    raise ValueError

                numbers_position = int(input('What position of numbers you want to include in password? (1 - after '
                                             'keyword, 2 - before keyword)'))

                if numbers_position == 1:
                    for i in range(numbers_amount):
                        self.password += str(random.randint(0, 10))
                elif numbers_position == 2:
                    for i in range(numbers_amount):
                        self.password = str(random.randint(0, 10)) + self.password
                else:
                    raise ValueError
            except ValueError:
                print('Please enter valid parameters to generate password')
