def abbreviate(words):
    return ''.join(list(acronym[0].upper() for acronym in words.split()))

