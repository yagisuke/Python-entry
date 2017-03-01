# モジュールの呼び出し
import module.no42_shaku;
# モジュールの関数を使う
v = module.no42_shaku.shaku_to_cm(10)
print("10尺=", v, "cm") # 10尺= 303.03 cm


# モジュール(別名)呼び出し
import module.no42_shaku as mod_shaku;
# モジュールの関数を使う
v = mod_shaku.shaku_to_cm(20)
print("20尺=", v, "cm") # 20尺= 606.06 cm


# モジュールの関数呼び出し
from module.no42_shaku import shaku_to_cm;
# モジュールの関数を使う
print("30尺=", shaku_to_cm(30), "cm") # 30尺= 909.09 cm


# モジュールの関数(別名)呼び出し
from module.no42_shaku import shaku_to_cm as to_cm;
# モジュールの関数を使う
print("40尺=", to_cm(40), "cm") # 40尺= 1212.12 cm
