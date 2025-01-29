import sys
import keyboard
import timeit
import threading, pyautogui
from explorer_snakegame import *
from paint_snakegame import *

X, Y = 170, 56 # replace with your coordonates for refresh button

def explorer_snake():
	if len(sys.argv) != 4:
		print("Usage: python main.py <lines> <columns> <FolderLocation>")
		sys.exit(1)
	
	print("All files from directory: " + sys.argv[3] + " will be deleted, are you sure you want to continue? (yes / no)")
	answer = input()
	if answer.lower() != "yes":
		print("Action canceled")
		sys.exit(0)

	return ExplorerSnakeGame(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])

def paint_snake():
	if len(sys.argv) != 3:
		print("Usage: python main.py <lines> <columns>")
		sys.exit(1)

	return PaintSnakeGame(int(sys.argv[1]), int(sys.argv[2]))

def game_loop(snakeGame: SnakeGame):
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
			snakeGame.alive = False
			break

if __name__ == "__main__":
	snakeGame = paint_snake()
	curr_time = timeit.default_timer()
	delay = 0.01

	game_thread = threading.Thread(target=game_loop, args=(snakeGame,))
	game_thread.start()

	while snakeGame.is_alive():
		if snakeGame.is_playng and (timeit.default_timer() - curr_time) >= delay:
			snakeGame.update()
			# snakeGame.print_board()
			curr_time = timeit.default_timer()

	game_thread.join()
