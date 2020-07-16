#!/usr/bin/env python

a = 1                  # モジュールスコープに変数を定義
b = 2

def foo():
    b = 10             # ローカルスコープで変数に代入
    print(a, b)        # a, bという2つの変数を表示

foo()                  # 関数foo()を呼び出す

print(a, b)            # a, bという2つの変数を表示
