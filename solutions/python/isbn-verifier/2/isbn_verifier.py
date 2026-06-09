import re


def verify(isbn):
    isbn_str = isbn.replace('-', '')

    def is_valid_isbn(string):
        return sum(int(n[0])*n[1] for n in zip(string, range(1, 11))) % 11 == 0

    if bool(re.match(r'\d{9}[X|\d]$', isbn_str)):
        isbn_list = list(isbn_str)
        if isbn_list[-1] == 'X':
            isbn_list[-1] = '10'
        return is_valid_isbn(isbn_list)
    return False
