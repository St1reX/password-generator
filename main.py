from UserKeyWords import UserKeyWords
from PasswordGenerator import PasswordGenerator


def main():
    user_keywords = UserKeyWords()
    PasswordGenerator(keyword_list=user_keywords.keyword_list)


main()
