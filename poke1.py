# 機能の読み込み
from game import *
from crash import *
import math
import random

# 画像の読み込みpoke
image_player = image('poke.png')
image_enemy = image('ball.png')

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
    # 自機とボールの衝突判定
    #全てのボールに対して順に処理を行う
    for e in group(enemy):
        if math.dist((p.x, p.y), (e.x, e.y)) < (p.sx+e.sx)*1:
            new_crash(p.x, p.y, 0.01, 20, 0.98)
            p.life = 0

#　ボールの処理
def enemy(e):
    e.x += e.vx
    e.r = math.sin(e.time*0.2)*0.01
    e.time += 1
    if abs(e.x) > SW+e.sx:
        e.life = 0

#　ステージ処理
def stage(s):
    if random.random() < 0.05:
        size = 0.1
        side = random.choice([-1, 1])
        y = random.uniform(-SH+size, SH-size)
        add(enemy, image_enemy, size, (SW+size)*side, y, -0.01*side)

# ゲームの開始処理
def start():
    add(stage)
    add(player, image_player, 0.08)

run(start, 1280, 720)