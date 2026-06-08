def is_isogram(string):
    import re
    isogram = re.sub(r'[ |-]', '', string).lower()
    # words_str = ''.join(string.replace('-','').split()).lower()
    return len(list(isogram)) == len(set(isogram))


