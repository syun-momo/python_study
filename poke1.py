# 機能の読み込み
from game import *

# 画像の読み込みpoke
image_player = image('ddpoke.png')

#　画面のサイズ
SW, SH = 1, 9/16

# 自機の処理
def player(p):
    # 自機の移動速度
    v = 0.01
    # 自機移動処理
    if key(LEFT):
        p.x -= v
    if key(RIGHT):
        p.x += v
    if key(UP):
        p.y += v
    if key(DOWN):
        p.y -= v
    # 移動可能範囲指定
    p.x = max(-SW+p.sx, min(SW-p.sx, p.x))
    p.y = max(-SH+p.sy, min(SH-p.sy, p.y))

# ゲームの開始処理
def start():
    add(player, image_player, 0.1)

run(start, 1280, 720)