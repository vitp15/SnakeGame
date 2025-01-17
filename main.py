import sys
import keyboard
import timeit
import pyautogui
from explorer_snakegame import *

X, Y = 170, 56 # replace with your coordonates for refresh button

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: python main.py <lines> <columns> <FolderLocation>")
		sys.exit(1)
	
	print("All files from directory: " + sys.argv[3] + " will be deleted, are you sure you want to continue? (yes / no)")
	answer = input()
	if answer.lower() != "yes":
		print("Action canceled")
		sys.exit(0)

	snakeGame = ExplorerSnakeGame(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
	time = timeit.default_timer()
	# snakeGame.print_board()
	delay = 0.2 

	while snakeGame.is_alive():
		if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
			snakeGame.move(Direction.N)
		elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
			snakeGame.move(Direction.S)
		elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
			snakeGame.move(Direction.W)
		elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
			snakeGame.move(Direction.E)
		elif keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
			break

		if snakeGame.is_playng and (timeit.default_timer() - time) >= delay:
			snakeGame.update()
			pyautogui.click(X, Y)
			# snakeGame.print_board()
			time = timeit.default_timer()
