from enum import Enum
import random

class Direction(Enum):
	N = 0
	W = 1
	S = 2
	E = 3
	NOTHING = 10

def oposite(first, second) -> bool:
	if first.value + 2 == second.value or first.value - 2 == second.value:
		return True

class SnakeGame:
	lines: int
	columns: int
	alive: bool = True
	direction: Direction
	is_playng: bool = False

	def __init__(self, lines: int, columns: int):
		self.direction = Direction.NOTHING
		self.columns = columns
		self.lines = lines
		self.board = [(x, y) for x in range(self.lines) for y in range(self.columns)]
		self.snake = [random.choice(self.board)]
		self.apple = random.choice(list(set(self.board) - set(self.snake)))

	def move(self, direction: Direction):
		if self.alive and not oposite(self.direction, direction):
			self.direction = direction
			if not self.is_playng:
				self.is_playng = True

	def is_alive(self):
		return self.alive

	def update(self):
		if self.alive:
			head = self.snake[0]
			if self.direction == Direction.N:
				new_head = (head[0] - 1, head[1])
			elif self.direction == Direction.S:
				new_head = (head[0] + 1, head[1])
			elif self.direction == Direction.W:
				new_head = (head[0], head[1] - 1)
			elif self.direction == Direction.E:
				new_head = (head[0], head[1] + 1)

			last = self.snake.pop()

			if new_head in self.snake or new_head not in self.board:
				self.snake.append(last)
				self.alive = False
			else:
				self.snake.insert(0, new_head)
				if new_head == self.apple:
					self.snake.append(last)
					self.apple = random.choice(list(set(self.board) - set(self.snake)))

	def print_board(self):
		board = ""
		for i in range(self.lines):
			for j in range(self.columns):
				if (i, j) in self.snake:
					board += "* " if self.is_alive() else "x "
				elif (i, j) == self.apple:
					board += "o "
				else:
					board += ". "
			board += "\n"
		print(board)
