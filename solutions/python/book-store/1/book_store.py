from itertools import groupby
COST = [800, 1520.0, 2160.0, 2560.0, 3000.0]


def calculate_total(books):
    books = sorted(books)
    books = sorted([len(list(group)) for key,group in groupby(books)], reverse=True)
    cost = set()
    different_books = len(books)
    if different_books < 5:
        cost.add(operate(different_books, books))
        cost.add(operate(different_books-1, books))
    else:
        cost.add(operate(5, books))
        cost.add(operate(4, books))
    return min(cost)


def operate(different_books, books):
    cost = 0
    if books:
        books = list(books)
        while True:
            try:
                for n in range(different_books)[::-1]:
                        books[n] -= 1
                books = list(filter(lambda x: x != 0, books))
                cost += COST[different_books - 1]
                if len(books) < 2:
                    try:
                        cost += 800*books[0]
                        return cost
                    except IndexError:
                        return cost
            except IndexError:
                different_books -= 1
    else:
        return cost
