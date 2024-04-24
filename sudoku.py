#!/usr/bin/env python3


# shebang
class Sudoku:
	def __init__(self):
		all_values = input().split(" ")
		self.cells = []
		count = 0
		for _ in range(9):
			array = []
			for i in range(9):
				array.append(all_values[count])
				count += 1
			self.cells.append(array)

	def print_sudoku(self, board):
		for i in range(len(board)):
			if i % 3 == 0 and i != 0:
				print("-" * 23)
			for j in range(len(board[0])):
				if j % 3 == 0 and j != 0:
					print(" |", end="")
				value = " " if board[i][j] == "-" else board[i][j]
				if j == 8:
					print(" " + value)
				else:
					print(" " + value, end="")

	def getblank(self):
		for i in range(len(self.cells)):
			if self.cells[i] == "-":
				return (i % 9, i / 9)
		raise RuntimeError

	def dump(self):
		self.print_sudoku(self.cells)


def main():
	sdk = Sudoku()
	sdk.getblank()
	sdk.dump()


main()
