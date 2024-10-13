from pygame import *


class GameSprite(sprite.Sprite):
    """Base class with make sprites"""
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        # конструктор class
        super().__init__()
        # all sprites - this images
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # all sprites - this прямоугольники rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        # draw person
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """Class-наследник with make main person"""
    def move_left(self):
        """left racket - стрелки вверх/down"""
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

    def move_right(self):
        """right racket - клавиши W/S"""
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed


# game window
win_width = 1000
win_height = 800
window = display.set_mode((win_width, win_height))
display.set_caption('PIPIBALL')
# background game window
back = 'darkturquoise'
window.fill(back)
# persons game
racket1 = Player('racket.png', 30, 300, 4, 80, 190)
racket2 = Player('racket.png', 880, 300, 4, 80, 190)
ball = Player('ppball.png', 500, 300, 4, 50, 50)

# game cycle
game = True
finish = False
clock = time.Clock()
FPS = 74

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        # draw background and persons game
        window.fill(back)

        racket1.move_left()
        racket2.move_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # if ball коснулся racket, меняем направление his move
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)