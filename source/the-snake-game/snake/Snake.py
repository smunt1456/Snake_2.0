import turtle


class Snake:

    def __init__(self, color, up, right, down, left, start, screen, apple, delay):
        self.start = start
        self.screen = screen
        self.apple = apple
        self.delay = delay
        self.player_list = None
        self.start = start
        self.dead = False
        self.DONE = False
        self.snake = turtle.Turtle()
        self.snake.shape("square")
        self.snake.color(color)
        self.snake.penup()
        self.snake_coord = []
        for i in range(4):
            self.snake_coord.append([start, i * 20])
        self.snake_coord.append([start, 80])
        self.snake_direction = up
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        self.offsets = {
            up: (0, 20),
            down: (0, -20),
            left: (-20, 0),
            right: (20, 0)
        }
        self.screen.get_screen().listen()
        self.screen.get_screen().onkey(self.go_up, up)
        self.screen.get_screen().onkey(self.go_right, right)
        self.screen.get_screen().onkey(self.go_down, down)
        self.screen.get_screen().onkey(self.go_left, left)
        for item in range(0, len(self.snake_coord) - 1):
            self.snake.goto(self.snake_coord[item][0], self.snake_coord[item][1])
            self.snake.stamp()

    def move(self):
        self.snake.clearstamps()
        self.snake_coord.append([self.snake_coord[-1][0] + self.offsets[self.snake_direction][0],
                                 self.snake_coord[-1][1] + self.offsets[self.snake_direction][1]])
        self.snake_coord.pop(0)
        for item in range(len(self.snake_coord) - 1):
            self.snake.goto(self.snake_coord[item][0], self.snake_coord[item][1])
            self.snake.stamp()
        if self.snake_coord[-2] == [self.apple.get_pos()[0], self.apple.get_pos()[1]]:
            self.apple.spawn()
            self.snake_coord.insert(0, [self.snake_coord[-1][0] -
                                        self.offsets[self.snake_direction][0],
                                        self.snake_coord[-1][1] -
                                        self.offsets[self.snake_direction][1]])
        self.check_die()
        self.out_of_bounds()
        self.screen.get_screen().update()
        if not self.DONE and not self.dead:
            turtle.ontimer(self.move, self.delay)

    def check_die(self):
        if self.DONE:
            self.snake_coord = []
            for i in range(4):
                self.snake_coord.append([self.start, i * 20])
            self.snake_coord.append([self.start, 80])
            self.snake_direction = self.up
            self.DONE = False
            if self.dead:
                self.dead = False
                self.move()

        else:
            for people in self.player_list:
                if self.snake_coord != people.get_coords():
                    for item in people.get_coords():
                        if [self.snake_coord[-1][0], self.snake_coord[-1][1]] == item:
                            print(f"you died {self.snake.color()[0]}")
                            self.snake_coord.pop(-1)
                            self.dead = True

    def out_of_bounds(self):
        if self.snake_coord[-1][0] >= (self.screen.get_screen_width() / 2) + 20:
            self.set_coords(-1, 0, (-self.screen.get_screen_width() / 2) + 20)  # -240
        if self.snake_coord[-1][1] >= (self.screen.get_screen_width() / 2) + 20:
            self.set_coords(-1, 1, (-self.screen.get_screen_width() / 2) + 20)
        if self.snake_coord[-1][0] <= (-self.screen.get_screen_width() / 2) - 20:  # works
            self.set_coords(-1, 0, (self.screen.get_screen_width() / 2) + 20)
        if self.snake_coord[-1][1] <= (-self.screen.get_screen_width() / 2) - 20:  # works
            self.set_coords(-1, 1, (self.screen.get_screen_width() / 2) + 20)

    def go_up(self):
        if self.snake_direction != self.down:
            self.snake_direction = self.up

    def go_down(self):
        if self.snake_direction != self.up:
            self.snake_direction = self.down

    def go_right(self):
        if self.snake_direction != self.left:
            self.snake_direction = self.right

    def go_left(self):
        if self.snake_direction != self.right:
            self.snake_direction = self.left

    def get_coords(self):
        return self.snake_coord

    def set_coords(self, index, xy, value):
        self.snake_coord[index][xy] = value

    def set_done(self):
        self.DONE = True
        self.check_die()

    def set_player_list(self, player_list):
        self.player_list = player_list
