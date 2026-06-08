def raindrops(number):
    from functools import reduce

    def factors(n):
        factors_in_pairs = ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
        return set(reduce(list.__add__, factors_in_pairs))

    factors_list = factors(number)
    match_numbers = [3, 5, 7]
    words = ['Pling', 'Plang', 'Plong']
    picked_words = [o for m, o in zip(match_numbers, words) if m in factors_list]
    if picked_words:
        return ''.join(picked_words)
    else: return str(number)






