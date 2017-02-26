# 英単語の出現回数を数えるプログラム

import re

message = """
Subject: Unavailability Notification

Dear Mr. Carter:

I will be out of the office starting tomorrow and will be back on February 8th. During those days, I will have limited access to my cell phone and e-mail, so please contact Masaaki Oota,（phone: 000-000-000 / e-mail address: oota@vvwxyzz.co.jp） in place of me.

Thank you.

Sincerely yours,
Hitoshi Makise
"""
# 参照: http://ejje.weblio.jp/template/OETMS/%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B/%E4%B8%8D%E5%9C%A8%E3%81%AE%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B

# 単語を区切る
message =  re.sub(r"[^a-zA-Z\s]", "", message) # 英文字とスペース以外を削除
words = message.split() # スペースで区切る

counter = {}
for word in words:
    ws = word.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

for k, v in counter.items():
    if 1 < v: print(k, v)
