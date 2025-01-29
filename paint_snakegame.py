from snake_game import *
import keyboard
import timeit, time
import pyautogui

pyautogui.PAUSE = 0

MAXLINES, MAXCOLUMNS = 45, 110
PAINT_X, PAINT_Y = 237, 100
SCREEN_MIN_X, SCREEN_MIN_Y = 6, 175
SCREEN_MAX_X, SCREEN_MAX_Y = 1902, 976
BLACK = 793, 84
RED = 864, 84
GREEN = 935, 84
GRAY = 822, 84
ERASER = 269, 134
RECTANGLE = 537, 91
PENCIL = 260, 85
SELECTION = 34, 95

def screen_coord(paint_x, paint_y):
	screen_x = paint_x / PAINT_X * (SCREEN_MAX_X - SCREEN_MIN_X)
	screen_y = paint_y / PAINT_Y * (SCREEN_MAX_Y - SCREEN_MIN_Y)
	return SCREEN_MIN_X + screen_x, SCREEN_MIN_Y + screen_y

class PaintSnakeGame(SnakeGame):
	def __init__(self, lines, columns):
		if lines > MAXLINES or columns > MAXCOLUMNS:
			raise Exception(f"You cannot use more than {MAXLINES} line and {MAXCOLUMNS} columns")
		super().__init__(lines, columns)
		print("Click enter for board to be painted in paint (only when you are in paint app already)")
		while True:
			if keyboard.is_pressed("enter"):
				# clear board
				pyautogui.click(SELECTION)
				pyautogui.moveTo(screen_coord((PAINT_X - MAXCOLUMNS * 2) / 2, (PAINT_Y - MAXLINES * 2) / 2))
				pyautogui.mouseDown()
				pyautogui.dragTo(screen_coord((PAINT_X - MAXCOLUMNS * 2) / 2 + MAXCOLUMNS * 2 + 1, (PAINT_Y - MAXLINES * 2) / 2 + MAXLINES * 2 + 1))
				pyautogui.mouseUp()
				pyautogui.press("delete")
				# draw board
				pyautogui.click(RECTANGLE)
				pyautogui.click(BLACK)
				self.paint_x_min = (PAINT_X - self.columns * 2) / 2
				self.paint_y_min = (PAINT_Y - self.lines * 2) / 2
				pyautogui.moveTo(screen_coord(self.paint_x_min, self.paint_y_min))
				pyautogui.mouseDown(duration=0)
				self.paint_x_max = (PAINT_X - self.columns * 2) / 2 + self.columns * 2 + 1
				self.paint_y_max = (PAINT_Y - self.lines * 2) / 2 + self.lines * 2 + 1
				pyautogui.dragTo(screen_coord(self.paint_x_max, self.paint_y_max))
				pyautogui.mouseUp()
				# draw snake
				pyautogui.click(PENCIL)
				pyautogui.click(GREEN)
				for x, y in self.snake:
					pyautogui.click(self.pixel_click(x, y))
					pyautogui.mouseDown()
					pyautogui.mouseUp()
				# draw apple
				pyautogui.click(PENCIL)
				pyautogui.click(RED)
				pyautogui.click(self.pixel_click(self.apple[0], self.apple[1]))
				pyautogui.mouseDown()
				pyautogui.mouseUp()
				break

	def finish_update(self, new_head, tail):
		if new_head in self.snake or new_head not in self.board:
			self.snake.append(tail)
			self.alive = False
			pyautogui.click(PENCIL)
			pyautogui.click(GRAY)
			for x, y in self.snake:
					pyautogui.click(self.pixel_click(x, y))
					pyautogui.mouseDown()
					pyautogui.mouseUp()
		else:
			self.snake.insert(0, new_head)
			pyautogui.click(PENCIL)
			pyautogui.click(GREEN)
			pyautogui.click(self.pixel_click(new_head[0], new_head[1]))
			pyautogui.mouseDown()
			pyautogui.mouseUp()
			pyautogui.click(ERASER)
			pyautogui.click(self.pixel_click(tail[0], tail[1]))
			pyautogui.mouseDown()
			pyautogui.mouseUp()
			if new_head == self.apple:
				self.snake.append(tail)
				self.apple = random.choice(list(set(self.board) - set(self.snake)))
				pyautogui.click(PENCIL)
				pyautogui.click(GREEN)
				pyautogui.click(self.pixel_click(tail[0], tail[1]))
				pyautogui.mouseDown()
				pyautogui.mouseUp()
				pyautogui.click(PENCIL)
				pyautogui.click(RED)
				pyautogui.click(self.pixel_click(self.apple[0], self.apple[1]))
				pyautogui.mouseDown()
				pyautogui.mouseUp()

	def pixel_click(self, i, j):
		# because x + ... will be as columns, and same for y + ... will be for line
		x_coord = self.paint_x_min + 2 + 2 * j
		y_coord = self.paint_y_min + 2 + 2 * i
		return screen_coord(x_coord, y_coord)
