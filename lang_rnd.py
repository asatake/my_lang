# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'asatake'

import random

offset = ord('A')  # ASCIIコードにおける'A'の番号
resault = []
num = []
p = []

# 入力
instr = input("print: ")

# 入力した文字列をASCIIコードの順番に変換
for i in range(len(instr)):
    num.append(ord(instr[i]) - offset)

# 乱数テーブルを生成
while True:
    if len(p) == ord('z') - ord('A') + 1:
        break
    tmp = random.randrange(ord('z') - ord('A') + 1)
    if p.count(tmp) == 0:
        p.append(tmp)

# 乱数テーブルにしたがって文字列を変換
for i in range(len(num)):
    # 記号を含まないように条件を書く
    if (((ord('A') - offset) <= p[num[i]] <= (ord('Z') - offset))
        or ((ord('a') - offset) <= p[num[i]] <= (ord('z') - offset))):
        resault.append(chr(offset + p[num[i]]))
    else:
        resault.append(chr(offset + num[i]))

# 表示
print("".join(resault))