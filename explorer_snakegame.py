from snake_game import *
from main import X, Y
from PIL import Image
import os, pyautogui

BACKGROUND = (127, 127, 127)
SNAKE = (0, 255, 0)
DEATH_SNAKE = (0, 0, 0)
APPLE = (255, 0, 0)
SIZE = (100, 100)

class ExplorerSnakeGame(SnakeGame):
	folder: str

	def __init__(self, lines, columns, folder):
		super().__init__(lines, columns)
		self.folder = folder
		delete_files_in_directory(self.folder)
		snake = Image.new("RGB", SIZE, SNAKE)
		snake.save(self.folder + "\\" + str((self.snake[0][0] * self.columns + self.snake[0][1])) + ".png")
		apple = Image.new("RGB", SIZE, APPLE)
		apple.save(self.folder + "\\" + str((self.apple[0] * self.columns + self.apple[1])) + ".png")
		file = Image.new("RGB", SIZE, BACKGROUND)
		for i, j in list(set(self.board) - set(self.snake) - set([self.apple])):
			file.save(self.folder + "\\" + str((i * self.columns + j)) + ".png")

	def finish_update(self, new_head, tail):
			pyautogui.click(X, Y)
			if new_head in self.snake or new_head not in self.board:
				self.snake.append(tail)
				self.alive = False
				dead_snake = Image.new("RGB", SIZE, DEATH_SNAKE)
				for i, j in self.snake:
					dead_snake.save(self.folder + "\\" + str((i * self.columns + j)) + ".png")
			else:
				self.snake.insert(0, new_head)
				file_snake = Image.new("RGB", SIZE, SNAKE)
				file_background = Image.new("RGB", SIZE, BACKGROUND)
				file_apple = Image.new("RGB", SIZE, APPLE)
				file_snake.save(self.folder + "\\" + str((new_head[0] * self.columns + new_head[1])) + ".png")
				file_background.save(self.folder + "\\" + str((tail[0] * self.columns + tail[1])) + ".png")
				if new_head == self.apple:
					self.snake.append(tail)
					self.apple = random.choice(list(set(self.board) - set(self.snake)))
					file_snake.save(self.folder + "\\" + str((tail[0] * self.columns + tail[1])) + ".png")
					file_apple.save(self.folder + "\\" + str((self.apple[0] * self.columns + self.apple[1])) + ".png")

def delete_files_in_directory(directory_path):
	try:
		files = os.listdir(directory_path)
		for file in files:
			file_path = os.path.join(directory_path, file)
			if os.path.isfile(file_path):
				os.remove(file_path)
		print("All files deleted successfully.")
	except OSError:
		print("Error occurred while deleting files.")
