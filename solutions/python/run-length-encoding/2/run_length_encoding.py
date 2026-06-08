from re import sub


def decode(string):
    return sub(r'(\d+)([a-zA-Z ])', lambda x: int(x.group(1)) * x.group(2), string)


def encode(string):
    return sub(r'([a-zA-Z ])\1+', lambda x: str(len(x.group(0))) + x.group(1), string)

