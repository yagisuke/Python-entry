# BMI判定プログラム
# BMI = 体重(kg) / ( 身長(m) x 身長(m) )
weight_kg = float(input("体重何キロあるん？"))
height_cm = float(input("身長は何センチあるん？"))
height_m = height_cm / 100
bmi = weight_kg / (height_m * height_m)

# 結果はどうなるか？
result = ""

if bmi < 18.5:
    result = "痩せとるなぁ"
if 18.5 <= bmi < 25: # (18.5 <= bmi) and (bmi < 25)
    result = "ふつぅ"
if 25 <= bmi < 30: # (25 <= bmi) and (bmi < 30)
    result = "ぽちゃってきてるで"
if bmi >= 30:
    result = "太りすぎです"

# 結果
print("BMI: ", bmi)
print("結果: ", result)
