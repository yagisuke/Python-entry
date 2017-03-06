# 画面に100本の縦線を引く

# グラフィックライブラリを取り込む
from tkinter import *
# 画面の初期化
w = Canvas(Tk(), width= 300, height= 300)
w.pack()

# トリコロールカラーの線をたくさん引く
for i in range(100):
    x = i * 3

    border_color = ""
    if i % 2 == 0:
        border_color = "red"
    else:
        border_color = "blue"

    w.create_line(x, 0, x, 300, fill= border_color)
mainloop()
