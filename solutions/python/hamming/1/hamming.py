def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(f'{strand_a} and {strand_b} have different length.')
    else:
        from itertools import count
        init = count(len(strand_a), -1)
        pairs = ((a,b) for a,b in zip(strand_a,strand_b))
        for pair in pairs:
            if pair[0] == pair[1]: next(init)
        return next(init)
