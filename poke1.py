# 機能の読み込み
from game import *

# 画像の読み込みpoke
image_player = image('ddpoke.png')

# 自機の処理
def player(p):
    p.x += p.vx

# ゲームの開始処理
def start():
    add(player, image_player, 0.1, -1.1, 0, 0.01, 0)

run(start, 1280, 720)