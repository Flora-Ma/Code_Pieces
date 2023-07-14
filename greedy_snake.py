from enum import Enum
import random
from collections import deque

class Direction(Enum):
    Up = [-1, 0]
    Down = [1, 0]
    Left = [0, -1]
    Right = [0, 1]

class Error(Enum):
    OffBoard = 1
    CrashSnake = 2

class Cell:
    def __init__(self, r, c, prev=None):
        self.r = r
        self.c = c
        self.prev = prev

class GreedySnake:
    def __init__(self, board_size:int):
        self.board_size = board_size
        apple_position, snake_head_position = random.sample(range(board_size ** 2), 2)
        #print(f'apple={apple_position}. snake={snake_head_position}')
        self.apple = (apple_position // board_size, apple_position % board_size)
        self.snake = deque([(snake_head_position // board_size, snake_head_position % board_size)])
        # self.opposite_directions = {Direction.Up, Direction.Down, Direction.Left, Direction.Right}

    def move(self, direction: Direction):
        snake_head = self.snake[0]
        new_head = (snake_head[0] + direction.value[0], snake_head[1] + direction.value[1])
        error = self.__check_error(new_head[0], new_head[1])
        if error:
            print(error)
            return False
        self.snake.appendleft(new_head)
        
        if self.apple == new_head:
            snake_head_position = self.snake[0][0] * self.board_size + self.snake[0][1]
            apple_position = random.choice([i for i in range(self.board_size ** 2) if i not in self.snake])
            self.apple = (apple_position // self.board_size, apple_position % self.board_size)
        else:
            self.snake.pop()
        print(self.snake)
        return True
    
    def find_solution(self) -> list[Direction]:
        shead = Cell(self.snake[0][0], self.snake[0][1])        
        def shortest_path(snake_head):
            queue = deque([snake_head])
            visited = set(queue)
            while queue:
                for i in range(len(queue)):
                    cell = queue.popleft()
                    if cell.r == self.apple[0] and cell.c == self.apple[1]:
                        return cell
                    for d in [Direction.Up, Direction.Down, Direction.Left, Direction.Right]:
                        next_cell = Cell(cell.r + d.value[0], cell.c + d.value[1], cell)
                        if self.__check_error(next_cell.r, next_cell.c) == None and next_cell not in visited:
                            queue.append(next_cell)
            return None
        last_cell = shortest_path(shead)
        def generate_directions(cell):
            moves = []
            while cell and cell.prev:
                moves.append(Direction([cell.r - cell.prev.r, cell.c - cell.prev.c]))
                cell = cell.prev
            moves.reverse()
            return moves
        return generate_directions(last_cell)                    
        
    def get_snake_length(self):
        return len(self.snake)
 
    def print_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (i, j) == self.apple and (i, j) in self.snake:
                    print('*', end='')
                elif (i, j) == self.apple:
                    print('a', end='')
                elif (i, j) == self.snake[0]:
                    print('h', end='')
                elif (i, j) in self.snake:
                    print('s', end='')
                else:
                    print('-', end='')
            print()

    def __check_error(self, r, c):
        if r < 0 or r >= self.board_size or c < 0 or c >= self.board_size:
            return Error.OffBoard
        if (r, c) in self.snake:
            return Error.CrashSnake
        return None 

def interaction_play(board_size):
    cmd_directions = {'u': Direction.Up, 'd': Direction.Down, 'l': Direction.Left, 'r': Direction.Right}
    gs = GreedySnake(board_size)
    print('Welcome to greedy snake!')
    gs.print_board()
    steps = 0
    while True:
        command = input('Enter move direction, u->UP, d->Down, l->Left, r->right, Enter q to quit:')
        command = command.strip().lower()
        if command == 'q':
            print(f'Bye! Current snake length = {gs.get_snake_length()}, Move steps = {steps}')
            break
        elif command in cmd_directions:
            if gs.move(cmd_directions[command]):
                steps += 1
                gs.print_board()

def auto_play(board_size):
    gs = GreedySnake(size)
    print('Welcome to greedy snake!')
    gs.print_board()
    while True:
        moves = gs.find_solution()
        print(f'The best play moves are {[m.name for m in moves]}')
        for direction in moves:
            gs.move(direction)
            gs.print_board()  
        if gs.get_snake_length() == 5:
            break  

size = int(input('Input board size:'))
#interaction_play(size)
auto_play(size)






        

