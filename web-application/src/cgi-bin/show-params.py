#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable() # webブラウザにエラーを表示させる

print("Content-Type: text/html; charset=utf-8")
print("")

# リクエストパラメータを取得
form = cgi.FieldStorage()

# --- 特定のパラメータを取得して表示 ---
mode = form.getvalue("mode", default="")
print("mode = ", mode, "<br>") # modeのパラメータを表示

# --- すべてのパラメータを取得して表示 ---
for k in form.keys():
    print(k, "=", frm.getvalue(k), "<br>") # 全てのパラメータを表示
