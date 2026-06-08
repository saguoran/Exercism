def score(word):
    from itertools import product
    d_score = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}
    return sum(d_score[key] for l, key in product(word.upper(), d_score) if l in key)


