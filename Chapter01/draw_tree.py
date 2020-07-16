#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *   # turtleの機能を読み込む

def tree(length):
    # 木を描く関数
    if length > 5:
        forward(length)
        right(20)
        tree(length-15)
        left(40)
        tree(length-15)
        right(20)
        backward(length)

color("green")   # カーソルの色を緑色にする
left(90)         # 左に90度させて上を向かせる
backward(150)    # 下に下げる
tree(120)        # 木を描く関数を呼び出す

input('type to exit')  # 描画終了後の入力待ち

