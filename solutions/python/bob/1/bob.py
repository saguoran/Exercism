from re import compile, sub
sure = 'Sure.'
whoa = 'Whoa, chill out!'
clam = "Calm down, I know what I'm doing!"
fine = 'Fine. Be that way!'
whatever = 'Whatever.'


def hey(phrase):
    nothing = compile(r'\s*$')
    question = compile(r'.*\?$')
    yell = compile(r'[A-Z]+!*$')
    yell_question = compile(r'^[A-Z\s]+\?$',)
    if nothing.match(phrase):
        return fine
    phrase = sub(r'\s+', '', phrase)  # substitute all whitespaces
    phrase = sub(r'\d', '', phrase)   # substitute all numbers
    if yell_question.match(phrase):
        return clam
    elif yell.search(phrase):
        return whoa
    elif question.match(phrase):
        return sure
    else:
        return whatever
