class Cat:
    # クラス変数
    nakigoe = "ニャー"

    # メソッド
    def naku(self):
        print(self.nakigoe)

mike = Cat()
nora = Cat()

mike.nakigoe = "ヴゥー"

mike.naku() # ヴゥー
nora.naku() # ニャー
