#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html

# ブラウザでのデバッグを有効にする
cgitb.enable()

# 全体の設定
FILE_LOG = "log/chat-log.txt"

# HTMLを画面に出力する
def print_html(body):
    # ヘッダ出力
    print("Content-Type: text/html; charset=utf-8")
    print("")
    # HTMLを出力する
    print("""
        <html>
        <head>
            <meta charset='utf-8'>
            <title>チャット</title>
        </head>
        <body>
            <h1>チャット</h1>
            <div>
                <form>
                    <input type="hidden" name="mode" value="write">
                    名前：<input type="text" name="name" size="8">
                    本文：<input type="text" name="body" size="20">
                    <input type="submit" value="発信">
                </form>
            </div>
            <hr>
            {0}
        </body>
        </html>
        """.format(body))

# 画面に書き込みログを表示する
def mode_read(form):
    # ログを読み取る
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            log = f.read()
    print_html(log)

# 任意のURLにjumpする
def jump(url):
    # ヘッダを出力
    print("status: 301 Moved Permanently")
    print("Location:", url)
    print("")
    # HTMLを出力
    print("<html>")
    print("<head><meta http-equiv=\"refresh\" content=\"0;", url, "\"></head>")
    print("<body>")
    print("<a href=\"", url, "\">jump</a>")
    print("</body>")
    print("</html>")

def mode_write(form):
    # パラメータを取得
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")
    # HTMLに変換
    name = html.escape(name)
    body = html.escape(body)
    # ファイルに保存
    with open(FILE_LOG, "a+", encoding='utf-8') as f:
        f.write("<p>{0}: {1}</p><hr>\n".format(name, body))
    # 書き込み後にリダイレクトする
    jump('chat.py')

# メイン処理
def main():
    # リクエストパラメータを取得
    form = cgi.FieldStorage()
    # modeパラメータを取得
    mode = form.getvalue("mode", "read")
    # modeの値によって処理を変更
    if mode == "read": mode_read(form)
    elif mode == "write": mode_write(form)
    else: mode_read(form)

if __name__ == "__main__":
    main()
