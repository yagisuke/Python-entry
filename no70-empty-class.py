# 空クラス(Empty Class)

class Empty: pass

o = Empty()
o.id = 100
o.name = "Jiro"
o.job = "Programmer"
print(o.id) # 100
print(o.name) # Jiro

calc = Empty()
calc.x2 = lambda x : x * 2
calc.x3 = lambda x : x * 3
print(calc.x2(8)) # 16
print(calc.x3(5)) # 15
