def word_count(phrase):
    import re
    pattern = re.compile(r'([a-zA-Z0-9]+\'?[a-zA-Z0-9]+|[0-9])')
    matchs = re.finditer(pattern, phrase)
    keywords = [[str(match[0]).lower(), 0] for match in matchs]
    pair_set = {(x, y) for x, y in keywords}
    dictionary = {}
    for x in pair_set:
        key_value = 0
        for comparison in keywords:
            if x[0] == comparison[0]:
                key_value += 1
        dictionary[x[0]] = key_value
    return dictionary
