def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(f'{strand_a} and {strand_b} have different length.')
    else:
        return sum((a != b) for a,b in zip(strand_a,strand_b))
