#!/usr/bin/env python3

import time
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
        return None

    def get_candidates(self, row, col):
        used = set()
        for r in range(9):
            used.add(self.cells[r][col])
        for c in range(9):
            used.add(self.cells[row][c])

        r_start, c_start = 3 * (row // 3), 3 * (col // 3)
        for r in range(r_start, r_start + 3):
            for c in range(c_start, c_start + 3):
                used.add(self.cells[r][c])

        return [num for num in range(1, 10) if num not in used]

    def solve(self):
        blank = self.getblank()
        if not blank:
            return True

        row, col = blank
        candidates = self.get_candidates(row, col)
        if not candidates:
            return False

        for candidate in candidates:
            self.cells[row][col] = candidate
            if self.solve():
                return True

            self.cells[row][col] = 0
        return False


def main():
    sdk = Sudoku()
    if sdk.solve():
        print("Solution found:")
        sdk.print_sudoku(sdk.cells)
    else:
        print("No solution exists.")


main()
