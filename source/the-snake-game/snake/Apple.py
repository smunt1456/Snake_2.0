import random
import turtle


class Apple:
    def __init__(self, the_screen):
        self.screen = the_screen
        self.apple = turtle.Turtle()
        self.apple.shape("square")
        self.apple.color("red")
        self.apple.penup()
        self.spawned = True
        if not self.spawned:
            self.spawn()

    def spawn(self):
        constant = abs(int(((self.screen.get_screen_width() - 20) / 20) - 17))
        x_value = 20 * (random.randint(0, constant * 2) - constant)
        y_value = 20 * (random.randint(0, constant * 2) - constant)
        self.apple.goto(x_value, y_value)

    def get_pos(self):
        return self.apple.pos()
