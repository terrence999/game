WIDTH = 400
HEIGHT = 400
from random import randint

score = 0
game_over = False
fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 100, 100

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        score = score + 10
        place_coin()

def time_up():
    pass

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
coin.y = randint(20, (HEIGHT - 20))

clock.schedule(time_up, 7.0)
place_coin()



def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
