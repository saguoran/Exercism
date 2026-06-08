from itertools import groupby
from re import findall, match


def decode(string):
    codes = findall(r'\d*[A-Za-z ]',string)
    decoded_string = ''
    for code in codes:
        matches = match(r'(\d+)[\w ]', code)
        try:
            for num in range(int(matches.group(1))):
                decoded_string += code[-1]
        except AttributeError:
            decoded_string += code[0]
    return decoded_string


def encode(string):
    groups = [list(group) for key,group in groupby(string)]
    encoded_string = ''
    for group in groups:
        encoded_string += str(len(group)) + group[0] if len(group) > 1 else group[0]
    return encoded_string
