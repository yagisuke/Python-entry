# カレントディレクト配下の指定したキーワードがあるファイル内テキストを取得します
import sys
import os

# Pythonで受け取ったコマンドライン引数は、sys.argvに代入される
if len(sys.argv) <= 1:
    print("[USAGE] no49-file-scan.py {Search Word}")
    sys.exit(0) # プログラムを終了する

# 検索キーワードを取得
search_word = sys.argv[1]

# os.walkでカレントディレクトリ以下のファイルを列挙して検索する
# print(os.walk(".")) <generator object walk at 0x101a42d58>
for root, dirs, files in os.walk("."):
    for fi in files:
        result = []
        # UTF-8以外のファイルを読み込むとエラーとなるため、try..except..を使用
        try:
            path = os.path.join(root, fi) # os.path.joinでフルパスを取得
            with open(path, encoding="utf-8") as f:
                for no, line in enumerate(f):
                    if line.find(search_word) >= 0:
                        line = line.strip() # memo: strip()は、空白と改行を削除してくれる
                        s = "| {0:4}: {1}".format(no + 1, line) # 表示の書式を設定
                        result.append(s)
        except:
            continue

        # resultに検索結果があれば結果を表示
        if len(result) > 0:
            print("+ file:", fi)
            for li in result:
                print(li)
                # $ python3 no49-search-file.py import
                # + file: no15-create-line.py
                # |    4: from tkinter import *
                # + file: no20-kakugen.py
                # |    1: import random
                # + file: no29-word-counter.py
                # |    3: import re
                # + file: no42-shaku.py
                # |    2: import module.no42_shaku;
                # |    9: import module.no42_shaku as mod_shaku;
                # |   16: from module.no42_shaku import shaku_to_cm;
                # |   22: from module.no42_shaku import shaku_to_cm as to_cm;
                # + file: no43-random-module.py
                # |    2: import random;
                # + file: no44-datetime-module.py
                # |    1: import datetime;
                # + file: no45-create-qrcode.py
                # |    6: import qrcode;
                # + file: no46-aes.py
                # |    7: from Crypto.Cipher import AES
                # |    8: import base64
                # + file: no48-json.py
                # |    1: import json;
                # + file: no49-search-file.py
                # |    1: import sys
                # |    2: import os
