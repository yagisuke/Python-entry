#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable() # webブラウザにエラーを表示させる

print("Content-Type: text/html; charset=utf-8")
print("")

# リクエストパラメータを取得
form = cgi.FieldStorage()

FORM = """
    <form action="/cgi-bin/tashizan.py" method="get">
        <input type="text" name="v1" placeholder="数字をいれてね">
        &nbsp;+&nbsp;
        <input type="text" name="v2" placeholder="数字をいれてね">
        <input type="submit" value="計算">
    </form>
    """

if (not 'v1' in form) or (not 'v2' in form):
    # 含まれないのでformを表示
    print("<h1>足し算できるもん</h1>", FORM)

else:
    # formの値を取得して計算結果を表示

    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")

    try:
        result = int(v1) + int(v2)
        print("<h1>", v1, "+", v2, "=", result, "</h1>", FORM)
    except:
        result = 0
        print("<h1>数値を入力してください。</h1>", FORM)
