def is_armstrong(number):
    length = len(str(number))
    return number == sum(int(digit) ** length for digit in str(number))
