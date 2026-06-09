from typing import List


def verify(isbn: str) -> bool:
    """ replace the '-'s for ''s, just in case, then turn isbn into string list """
    isbn_str: List[str] = [e for e in isbn.replace('-', '')]
    if len(isbn_str) == 10:
        ''' check if the string list contains 10 elements,'''
        ''' and if the last character is 'X' then replace it for a integer 10 '''
        if isbn_str[-1] == 'X':
            isbn_str[-1] = '10'
        if ''.join(isbn_str).isdigit():
            ''' check if the joined string list is a number, then calculate if it is invalid '''
            ascending = [a for a in range(1, 11)]
            isbn_int = [int(code) for code in isbn_str]
            invalid = sum(ascending[i] * isbn_int[i] for i in range(10)) % 11
            if not invalid:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

