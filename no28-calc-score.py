# テスト結果発表！！

records = {
    "鈴木": 20, "橋田": 20, "今田": 19,
    "佐藤": 10, "斎藤": 89, "青木": 12,
    "土屋": 40, "金本": 55, "前野": 88,
    "金子": 90, "山田": 25, "上野": 99}

# 合計点 / 平均点
sum_v = sum(records.values())
avg_v = int(sum_v / len(records))
print("合計点:", sum_v)
print("平均点:", avg_v)

print_format = "| {0:<7} | {1:>4} | {2:>5} |"
print("| 名前      |  点数|    差 |" )
for name, v in sorted(records.items()):
    diff_v = v - avg_v
    diff_v = round(diff_v, 1)
    print(print_format.format(name, v, diff_v))

### 実行結果
# 合計点: 567
# 平均点: 47
# | 名前      | 点数 |  差   |
# | 上野      |   99 |    52 |
# | 今田      |   19 |   -28 |
# | 佐藤      |   10 |   -37 |
# | 前野      |   88 |    41 |
# | 土屋      |   40 |    -7 |
# | 山田      |   25 |   -22 |
# | 斎藤      |   89 |    42 |
# | 橋田      |   20 |   -27 |
# | 金子      |   90 |    43 |
# | 金本      |   55 |     8 |
# | 鈴木      |   20 |   -27 |
# | 青木      |   12 |   -35 |
