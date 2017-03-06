class BMI:
    '''bmiを計算するクラス'''

    def __init__(self, weight, height):
        '''初期化'''
        self.weight = weight
        self.height = height
        self.calcBMI()

    def calcBMI(self):
        '''BMIを計算する'''
        h = self.height / 100
        self.bmi = self.weight / (h ** 2)

    def printJudge(self):
        '''結果を表示する'''
        print("---")
        print("BMI=", self.bmi)
        b = self.bmi
        if (b < 18.5): print("瘦せ型")
        elif (b < 25): print("標準")
        else: print("肥満")

# 1人目
person1 = BMI(weight = 65, height = 170)
person1.printJudge()
# ---
# BMI= 22.49134948096886
# 標準

# 2人目
person1 = BMI(65, 160)
person1.printJudge()
# ---
# BMI= 25.390624999999996
# 肥満
