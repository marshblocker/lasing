from os import system
from time import sleep
import random
from typing import Callable, NewType


GRID_CHAR = '*'
BOARD_WIDTH = 50
BOARD_HEIGHT = 25

BoardType = NewType("BoardType", list[list[bool]])


def check_and_update_board(direction: int, old_pos: tuple[int, int], 
			 			   board: BoardType) -> tuple[bool, tuple[int, int]]:
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

	return (occupied, (r, c))


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
	board = BoardType([[False for _ in range(BOARD_WIDTH)] 
							for _ in range(BOARD_HEIGHT)])
	r: int = random.randint(0, BOARD_HEIGHT-1)
	c: int = random.randint(0, BOARD_WIDTH-1)
	board[r][c] = True

	while True:
		print_board(board)
		tries = 0
		while tries < 100:
			direction: int = random.randint(0, 3)
			occupied, new_pos = \
				check_and_update_board(direction, (r, c), board)	
			if not occupied:
				r, c = new_pos
				break
			else:
				tries += 1
		if tries >= 100:
			break
	print_board(board, clear= False)


if __name__ == "__main__":
	main()
