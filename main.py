import sys
import keyboard
import timeit
from snake_game import SnakeGame, Direction

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: python main.py <lines> <columns> <FolderLocation>")
		sys.exit(1)

	snakeGame = SnakeGame(int(sys.argv[1]), int(sys.argv[2]))
	time = timeit.default_timer()
	snakeGame.print_board()
	while snakeGame.is_alive():
		if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
			snakeGame.move(Direction.N)
		elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
			snakeGame.move(Direction.S)
		elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
			snakeGame.move(Direction.W)
		elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
			snakeGame.move(Direction.E)
		if snakeGame.is_playng and (timeit.default_timer() - time) >= 0.2:
			snakeGame.update()
			snakeGame.print_board()
			time = timeit.default_timer()
