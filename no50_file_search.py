# カレントディレクト配下のファイルをファイル名を指定して取得します
# <name search>
# [command]
#     $ python3 no50-file-search.py --name "no01-hello.py"
# [result]
#     + option
#     | search_mode= name
#     | desc_mode= False
#     ./no01-hello.py
#
# <wild search>
# [command]
#     $ python3 no50-file-search.py --wild "no0*.py"
# [result]
#     + option
#     | search_mode= wild
#     | desc_mode= False
#     ./no01-hello.py
#     ./no02-calc.py
#     ./no03-inch-to-cm.py
#     ...
import sys
import os
import fnmatch
import datetime
import math

# 引数の確認と使い方を表示
if len(sys.argv) <= 1:
    print("[USAGE] no50-file-search.py [--name][--wild][--desc] name")
    sys.exit(0)

# オプションの初期値
search_mode = "name"
search_func = lambda target, name : (target == name)
name = ""
desc_mode = False

# オプションを解析
for v in sys.argv:
    if v == "--name":
        search_mode = "name"
        search_func = lambda target, name : (target == name)
    elif v == "--wild":
        search_mode = "wild"
        search_func = lambda target, pat : fnmatch.fnmatch(target, pat)
    elif v == "--desc":
        desc_mode = True
    else:
        name = v

# オプションの解析結果を表示
print("+ option")
print("| search_mode=", search_mode)
print("| desc_mode=", desc_mode)

# ファイルの検索を開始
for root, dirs, files in os.walk("."):
    for fname in files:
        path = os.path.join(root, fname)
        b = search_func(fname, name)

        if b == False : continue

        if desc_mode:
            info = os.stat(path)
            kb = math.ceil(info.st_size / 1024)
            mt = datetime.datetime.fromtimestamp(info.st_mtime)
            s = "{0}, {1}KB, {2}".format(path, kb, mt.strftime("%Y-%m-%d"))
            print(s)
        else:
            print(path)
