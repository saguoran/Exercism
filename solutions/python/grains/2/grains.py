def square(number):
    if not (0<number<65):
        raise ValueError("square must be between 1 and 64")
    #return 2**(number-1)
    # x << n == x*(2**n)
    # x >> n == x/(2**n)
    return 1 << (number-1)

def total():
    # return sum([square(i) for i in range(1,65)])
    # return 2**64-1
    return (1<<64)-1