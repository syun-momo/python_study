form game import *

image_player = image('')

def player(p):
    p.x += p.vx

def start():
    add(player, image_player, 0.1, -1.1, 0, 0.01, 0)

run(start,1280,720)
