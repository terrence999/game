character = Actor ('face')
character.pos = 100, 56

WIDTH = 500
HEIGHT = character.height + 20

def draw():
    screen.clear()
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0
# Write your code here :-)
# Write your code here :-)
