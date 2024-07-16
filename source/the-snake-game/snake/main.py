import turtle
from Apple import Apple
from Snake import Snake
from Screen import Screen

WIDTH = 600
HEIGHT = 600
DELAY = 100
DEAD = False
UNITS = 20

offsets = {
    "Up": (0, UNITS),
    "Down": (0, -UNITS),
    "Left": (-UNITS, 0),
    "Right": (UNITS, 0)
}
count = 0
game_screen = Screen(640, 640)
apple = Apple(game_screen)
game_screen.set_apple(apple)

player1 = Snake("blue", "Up", "Right", "Down", "Left", 60, game_screen, apple, DELAY)
player2 = Snake("yellow", "w", "d", "s", "a", -60, game_screen, apple, DELAY)
players = [player1, player2]
player1.set_player_list(players)
player2.set_player_list(players)

apple.spawn()


def restart():
    print("Restarting...")
    player1.set_done()
    player2.set_done()
    game_screen.set_screen(WIDTH, HEIGHT)
    apple.spawn()


game_screen.get_screen().onkey(restart, "r")

player1.move()
player2.move()

game_screen.update_screen()

turtle.done()
