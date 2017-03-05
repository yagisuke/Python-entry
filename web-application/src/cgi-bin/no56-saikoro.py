#!/usr/bin/env python3

import random

print("Content-Type: text/html; charset=utf-8")
print("")

# ランダムな数を取得
no = random.randint(1, 6)
print("""
<html>
<head>
<meta charset='utf-8'>
<body><h1>サイコロの目は{num}となりました。</h1></body>
</html>
""".format(num = no))
