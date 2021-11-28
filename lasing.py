from os import system
from time import sleep
from typing import NewType, TypedDict
import random

GRID_CHAR = '*'
BOARD_WIDTH = 80
BOARD_HEIGHT = 40


class Walker(TypedDict):
	pos: list[int]
	free: bool


Traversed = bool
BoardType = NewType("BoardType", list[list[Traversed]])
WalkersType = NewType("WalkersType", list[Walker])


def populate_board(board: BoardType, n: int) -> WalkersType:
	walkers = WalkersType([{"pos": [0, 0], "free": True} for _ in range(n)])

	for i in range(n):
		while True:
			r: int = random.randint(0, BOARD_HEIGHT-1)
			c: int = random.randint(0, BOARD_WIDTH-1)
			if not board[r][c]:
				walkers[i]["pos"] = [r, c]
				board[r][c] = True
				break 

	return walkers


def check_and_update_board(direction: int, old_pos: list[int], 
			   board: BoardType) -> tuple[bool, list[int]]:
	occupied: bool = True  
	r, c  = old_pos
	match direction:
		case 0:	# UP
			r += 1
		case 1: # RIGHT
			c += 1
		case 2: # DOWN
			r -= 1
		case 3: # LEFT
			c -= 1

	if 0 < r < BOARD_HEIGHT and 0 < c < BOARD_WIDTH:
		occupied = board[r][c]
		if not occupied:
			board[r][c] = True

	return (occupied, [r, c])


def clear_screen() -> None:
	system('cls')


def print_board(board: BoardType, clear: bool = True) -> None:
	board_str = "\n".join(["".join([GRID_CHAR if e else " " for e in row]) 
			       for row in board])
	print(board_str)
	if clear:
		sleep(0.001)
		clear_screen()


def main():
	n = int(input("n: "))
	board = BoardType([[False for _ in range(BOARD_WIDTH)] 
			   	for _ in range(BOARD_HEIGHT)])
	walkers: WalkersType = populate_board(board, n)

	stuck_count = 0
	while stuck_count != n:
		print_board(board)
		for i in range(len(walkers)):
			available: list[int] = [0, 1, 2, 3]

			if walkers[i]["free"]:
				while len(available):
					direction: int = random.choice(available)
					occupied, new_pos = \
						check_and_update_board(direction, 
								       walkers[i]["pos"], board)	

					if occupied:
						available.remove(direction)
					else:
						walkers[i]["pos"] = new_pos
						break

				if not len(available):
					walkers[i]["free"] = False 
					stuck_count += 1

	print_board(board, clear= False)


if __name__ == "__main__":
	main()
