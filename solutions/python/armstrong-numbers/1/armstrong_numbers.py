def is_armstrong(num):
    length = len(str(num))
    digits = (digit for digit in str(num))
    armstrong = 0
    for digit in digits:
        armstrong += int(digit) ** length
    return num == armstrong

