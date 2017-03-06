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


# ducktypingを利用した鶴亀算
class Tsuru:
    def get_name(self): return "鶴"
    def get_legs(self): return 2

class Kame:
    def get_name(self): return "亀"
    def get_legs(self): return 4

class Tako:
    def get_name(self): return "タコ"
    def get_legs(self): return 8

class Ika:
    def get_name(self): return "イカ"
    def get_legs(self): return 10

# 鶴亀算を解く関数
def calc_tsurukame(tsuru, kame, heads, legs):

    tsuru_1 = tsuru.get_legs()
    kame_1 = kame.get_legs()
    tsuru_name = tsuru.get_name()
    kame_name = kame.get_name()

    kame_num = (legs - (tsuru_1 * heads)) // (kame_1 - tsuru_1)
    tsuru_num = heads - kame_num

    print("---")
    print("頭=", heads, "足=", legs)
    print(tsuru_name, "=", tsuru_num)
    print(kame_name, "=", kame_num)

    return (tsuru_num, kame_num)

if __name__ == "__main__":
    calc_tsurukame(Tsuru(), Kame(), heads=10, legs=28)
    # ---
    # 頭= 10 足= 28
    # 鶴 = 6
    # 亀 = 4
    calc_tsurukame(Tako(), Ika(), heads=11, legs=100)
    # ---
    # 頭= 11 足= 100
    # タコ = 5
    # イカ = 6
