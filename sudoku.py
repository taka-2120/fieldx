#!/usr/bin/env python3

# shebang
class Sudoku:
	def __init__(self):
		all_values = input().split(" ")
		print(problem)
		self.cells = []
		for (x, value in enumerate(all_values):
			// TODO: 
		self.cells = [[0 for _ in range(9)] for _ in range(9)]

	def print_sudoku(self, board):
    		for i in range(len(board)):
        		if i % 3 == 0 and i != 0:
            			print("-" * 23)
        		for j in range(len(board[0])):
		            if j % 3 == 0 and j != 0:
		                print(" |", end="")
		            if j == 8:
		                print(" " + str(board[i][j]))
		            else:
		                print(" " + str(board[i][j]), end="")

	def dump(self):
		self.print_sudoku(self.cells)

def main():
	sdk = Sudoku()
	sdk.dump()

main()
