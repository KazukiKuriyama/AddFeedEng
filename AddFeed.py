#!/usr/bin/env python3
"""
英語を指定行数で改行し、単語の途中の場合は一つ前のスペースで改行する。

引数1：ファイルパス
引数2：最大桁数
"""

import sys
import os
import fileinput
from pathlib import Path

filePath = sys.argv[1] # ファイルパス
sourceFile = open(filePath)
feedDigit = int(sys.argv[2]) # 改行桁数
# fileNameExtension = os.path.basename(filePath) # ファイルパスからファイル名+拡張子を取得する。
path, ext = os.path.splitext(filePath)
newPath = path + '_AddFeed' # 書き込み先のファイルパス＋ファイル名
if Path(filePath).exists():  # 第一引数がファイルだったら
    print('ファイルを読み込みを開始します')
    candidatePath = newPath + ext # ファイル名候補
    i = 0
    while True:
      # 重複しないファイル名になるまでループする
      if not os.path.exists(candidatePath): # パスの存在確認
          newFilePath = candidatePath       # 重複無し
          break
      # 数値を3桁などにしたい場合は({:0=3})とする
      i += 1
      candidatePath = "{} ({}){}".format(newPath, i, ext)
    print(newFilePath)
    addFeedFile = open(newFilePath, 'x') # ファイルが存在していない場合にファイルを作成する
    for line in sourceFile.readlines():  # ファイルの内容を一行ずつprint
      print(line)
      if len(line) <= feedDigit:
        print(line)
        addFeedFile.write(line)
      else :
        currentLine = line
        testCharPosition = feedDigit # 現在の検索位置設定
        while True:
          if len(currentLine) <= feedDigit:
            # 残りの文字数が少ない場合、そのまま改行する
            addFeedFile.write(currentLine)
            break # 読み込み元の行の最後に到達
          if testCharPosition == 0:
            # 行末までスペースがなかった場合または、指定の桁数で改行する
            addFeedFile.write(currentLine[feedDigit])
            break # 読み込み元の行の最後に到達
          if currentLine[testCharPosition] == " ":
            # スペースが見つかれば、その位置で改行する
            addFeedFile.write(currentLine[0:testCharPosition]+"\r")
            currentLine = currentLine[testCharPosition+1:] # 検索対象行から書き込み済みの
            testCharPosition = feedDigit # 現在の検索位置設定
          else:
            # スペース以外
              testCharPosition -= 1 # 次ループでは一つ手前の文字を調べる
    # 書き込み終了
    addFeedFile.close()
    sourceFile.close()


else:  # 第一引数がファイルではなかったら
    print('指定したファイルパスは不正です。')
    for i in sys.argv[1:]:  # 引数の文字列をprint
        print(i)