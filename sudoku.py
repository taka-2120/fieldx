#!/usr/bin/env python3


import time

# shebang
from typing import List


class Sudoku:
    def __init__(self):
        all_values = input().split(" ")
        self.count = 0
        self.cells: List[List[int]] = []
        count = 0
        for _ in range(9):
            array = []
            for _ in range(9):
                array.append(0 if all_values[count] == "-" else int(all_values[count]))
                count += 1
            self.cells.append(array)

    def print_sudoku(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("-" * 23)
            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" |", end="")
                value = " " if board[i][j] == 0 else str(board[i][j])
                if j == 8:
                    print(" " + value)
                else:
                    print(" " + value, end="")

    def getblank(self):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if self.cells[row][col] == 0:
                    return (row, col)
        raise RuntimeError

    def get_candidates(self, row, col):
        counter = {i: 0 for i in range(len(self.cells) + 1)}

        for r in range(len(self.cells)):
            counter[int(self.cells[r][col])] += 1

        for c in range(len(self.cells[row])):
            counter[int(self.cells[row][c])] += 1

        for r in range(3 * (row // 3), 3 * (col // 3) + 3):
            for c in range(3 * (col // 3), 3 * (row // 3) + 3):
                counter[int(self.cells[r][c])] += 1

        result: List[int] = []
        for key, value in counter.items():
            if value == 0:
                result.append(key)
        return result

    def solve(self):
        try:
            row, col = self.getblank()
        except RuntimeError:
            print("solved")
            return True

        candidates = self.get_candidates(row, col)
        if len(candidates) == 0:
            return False

        for candidate in candidates:
            self.cells[row][col] = candidate
            self.print_sudoku(self.cells)
            time.sleep(1.3)  # Seconds
            # if enter == "":
            #     pass
            # else:
            #     raise RuntimeError

            if self.solve():
                return True
            self.cells[row][col] = 0
        return False

    def dump(self):
        self.print_sudoku(self.cells)


def main():
    sdk = Sudoku()
    if sdk.solve():
        sdk.dump()


main()
