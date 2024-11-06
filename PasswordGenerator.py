import random
import os


class PasswordGenerator:
    def __init__(self, keyword_list):
        self.keyword_list = keyword_list
        self.password = ""

        self.generate_password()

    def numbers_in_password(self):
        while True:
            try:
                print('Here you can add numbers to your password.')

                numbers_amount = int(input('What amount of numbers you want to include in password? (Provide number '
                                           'between 0 and 10)\n'))
                if numbers_amount < 0 or numbers_amount > 10:
                    raise ValueError
                elif numbers_amount == 0:
                    return

                numbers_position = int(input('What position of numbers you want to include in password? (1 - after '
                                             'keyword, 2 - before keyword)\n'))

                if numbers_position == 1:
                    for i in range(numbers_amount):
                        self.password += str(random.randint(0, 9))
                elif numbers_position == 2:
                    for i in range(numbers_amount):
                        self.password = str(random.randint(0, 9)) + self.password
                else:
                    raise ValueError
                break
            except ValueError:
                print('Please enter valid parameters to generate password')
                input('Press enter to continue')
                os.system('cls')

    def special_characters_in_password(self):
        special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

        while True:
            try:
                print('Here you can add special characters to your password.')

                special_characters_amount = int(input('What amount of special characters amount you want to include '
                                                      'in password? (Provide number between 0 and 5)\n'))
                if special_characters_amount < 0 or special_characters_amount > 5:
                    raise ValueError
                elif special_characters_amount == 0:
                    return

                special_characters_position = int(input('What position of special characters you want to include in '
                                                        'password? (1 - after keyword, 2 - before keyword)\n'))

                if special_characters_position == 1:
                    for i in range(special_characters_amount):
                        self.password += str(random.choice(special_characters))
                elif special_characters_position == 2:
                    for i in range(special_characters_amount):
                        self.password = str(random.choice(special_characters)) + self.password
                else:
                    raise ValueError
                break
            except ValueError:
                print('Please enter valid parameters to generate password')
                input('Press enter to continue')
                os.system('cls')

    def generate_password(self):
        self.password += random.choice(self.keyword_list)
        self.numbers_in_password()
        self.special_characters_in_password()

        print(f"Your password is: {self.password}")
        input("Press Enter to end the program")
        os.system('cls')
