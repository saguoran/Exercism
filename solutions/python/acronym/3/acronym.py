def abbreviate(words):
    abbreviation = [word[0] for word in words.split() if word[0].isalpha()]
    return ''.join(abbreviation).upper()


