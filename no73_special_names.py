# 特殊メソド
# http://docs.python.jp/3/reference/datamodel.html#specialnames

# 比較演算子のオーバーロード
# 座標を取得する処理
class Pos:
    '''座標を表すクラス'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        '''+演算子の振る舞いを定義'''
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __mul__(self, other):
        if isinstance(other, (int, float)): # otherがint, floatの時だけ
            x2 = self.x * other
            y2 = self.y * other
            return Pos(x2, y2)
        else:
            raise TypeError

    def __str__(self):
        '''文字列として取得する際の振る舞いを定義'''
        return "({0}, {1})".format(self.x, self.y)

# 座標p1とp2を作成
p1 = Pos(10, 20)
p2 = p1 * 1.5
p3 = p1 + p2
print(p3) # (25.0, 50.0)
print("=======================================")



# インデックス番号やキーでのアクセスを実現する__getitem__, __setitem__
# 月名を取得する処理
class Tsukimei:
    tsuki = [
        "睦月", "如月", "弥生", "卯月", "皐月", "水無月",
        "文月", "葉月", "長月", "神無月", "霜月", "師走"
    ]

    def __getitem__(self, key):
        i = int(key)
        return self.tsuki[i - 1]

    def __setitem__(self, key, value):
        i = int(key)
        self.tsuki[i - 1] = value

t = Tsukimei()
t[3] = "March"
print(t[3]) # March
print(t[12]) # 師走
print("\n=======================================")



# イテレータとして振る舞う（__iter__, __next__）
class PrimeIter:
    def __init__(self, max_num):
        '''最大値を設定'''
        self.max_num = max_num

    def __iter__(self):
        '''イテレータを初期化する'''
        self.num = 1
        return self

    def __next__(self):
        '''次の素数を探して返す'''
        is_prime = False
        self.num += 1

        # 素数を探す
        while not is_prime:
            is_prime = True
            for i in range(2, self.num):
                if self.num % i == 0:
                    is_prime = False
                    break
            if is_prime: break
            self.num += 1
            # 最大値に達したら例外を出す
            if self.num >= self.max_num:
                raise StopIteration
        return self.num

it = PrimeIter(100)
for num in it:
    print(num, end=",")
print("=======================================")



# アクセサとゲッターセッターについて
class Clock:
    def __init__(self, hour):
        self._hour = hour
        self._ampm = "am"

    @property
    def hour(self): return self._hour # hourのゲッター

    @property
    def ampm(self): return self._ampm # ampmのゲッター

    @hour.setter # hourのセッター
    def hour(self, value):
        self._hour = value % 12
        self._ampm = "am" if value <= 12 else "pm"

clock = Clock(11)
print(clock.ampm, clock.hour) # am 11
clock.hour = 20
print(clock.ampm, clock.hour) # pm 8
