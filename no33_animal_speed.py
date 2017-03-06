# 東京から各都市までの動物ごとの所要時間を算出

# 動物ごとの最高速度
animal_speed_dict = {
    "チーター": 110, "トナカイ": 80, "シマウマ":  60, "ライオン": 58,
    "猫　　　":  57, "犬　　　": 56, "キリン　":  50, "カバ　　": 120}

# 東京から各都市までの距離
distance_dict = {
    "静　岡": 183.7, "名古屋": 350.6, "大　阪": 507.5}

# 時間を計算する関数
def calc_time(dist, speed):
    t = dist / speed # 距離 ÷ 速度を計算
    t = round(t, 1) # 四捨五入
    return t

def calc_animal(animal, speed):
    res = "|" + animal
    for city in sorted(distance_dict.keys()):
        dist = distance_dict[city]
        t = calc_time(dist, speed)
        res += "|{0:>6}".format(t)
    return res + "|"

# 表頭を作成
print("+--------+------+------+------+")
print("|動物名前", end="")
for city in sorted(distance_dict.keys()):
    print("|" + city, end="")
print("|")
print("+--------+------+------+------+")

# 各動物ごとに結果を求めて表示
for animal, speed in animal_speed_dict.items():
    s = calc_animal(animal, speed)
    print(s)
print("+--------+------+------+------+")

### 出力結果
# +--------+------+------+------+
# |動物名前 |名古屋 |大　阪 |静　岡 |
# +--------+------+------+------+
# |チーター |   3.2|   4.6|   1.7|
# |トナカイ |   4.4|   6.3|   2.3|
# |シマウマ |   5.8|   8.5|   3.1|
# |ライオン |   6.0|   8.8|   3.2|
# |猫　　　 |   6.2|   8.9|   3.2|
# |犬　　　 |   6.3|   9.1|   3.3|
# |キリン　 |   7.0|  10.2|   3.7|
# |カバ　　 |   2.9|   4.2|   1.5|
# +--------+------+------+------+
