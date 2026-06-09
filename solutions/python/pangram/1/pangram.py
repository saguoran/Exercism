def is_pangram(sentence):
    import string
    sentence = sentence.lower()
    for letter in string.ascii_lowercase[:27]:
        if letter not in sentence:
            return False
    return True





