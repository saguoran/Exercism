from typing import List


def cast_into_ints(strings : List[str]) -> List[int]:
    return [int(num) for num in strings]

class Matrix:
    def __init__(self,matrix_str: str) -> None:
        self.matrix: List[List[int]] = [cast_into_ints(line.split(' ')) for line in matrix_str.splitlines()]

    def row(self, index: int) -> List[int]:
        return self.matrix[index]

    def column(self, index: int) -> List[int]:
        return [row[index] for row in self.matrix]

