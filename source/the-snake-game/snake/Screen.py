import turtle


class Screen:
    def __init__(self, width, height):
        self.apple = None
        self.width = width
        self.height = height
        self.screen = turtle.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()

    def update_screen(self):
        if self.width > 400:
            self.width -= 40
            self.height -= 40
            self.screen.setup(self.width, self.height)
            if (self.apple.get_pos()[0] > (self.screen.window_width() / 2) - 40
                    or self.apple.get_pos()[0] < (self.screen.window_width() / -2) - 40
                    or self.apple.get_pos()[1] > (self.screen.window_height() / 2) - 40
                    or self.apple.get_pos()[1] < (self.screen.window_height() / -2) - 40):
                self.apple.spawn()
        self.screen.ontimer(self.update_screen, 5000)

    def get_screen(self):
        return self.screen

    def get_screen_width(self):
        return self.screen.window_width()

    def get_screen_height(self):
        return self.screen.window_height()

    def set_apple(self, apple):
        self.apple = apple

    def set_screen(self, width, height):
        self.width = width
        self.height = height
        self.screen.setup(width, height)
