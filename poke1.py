# 機能の読み込み
from game import *

# 画像の読み込みpoke
image_player = image('ddpoke.png')

# 自機の処理
def player(p):
    v = 0.01
    if key(LEFT):
        p.x -= v
    if key(RIGHT):
        p.x += v
    if key(UP):
        p.y += v
    if key(DOWN):
        p.y -= v

# ゲームの開始処理
def start():
    add(player, image_player, 0.1)

run(start, 1280, 720)