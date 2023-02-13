WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200
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
clock.schedule(time_up, 7.0)
place_coin()
