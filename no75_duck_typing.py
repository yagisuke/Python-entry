# duck typing
# クラスの方は違えど、同じメソッドを持っていれば同様に処理する

def test_duck(it):
    it.sound()
    it.walk()

class Duck:
    def sound(self): print("ガァガァ")
    def walk(self): print("アヒルが歩く")

class Dock:
    def sound(self): print("ワァンワァン")
    def walk(self): print("犬が歩く")

inu = Dock()
test_duck(inu)
# ワァンワァン
# 犬が歩く

ahiru = Duck()
test_duck(ahiru)
# ガァガァ
# アヒルが歩く
