import math

class CalcFee:

    def __init__(self):
        '''初期化メソッド'''
        self.shipping_fee = 1000 # 送料
        self.tax_rate = 0.08 # 税率
        self.value = 0 # 合計

    def addItem(self, price):
        '''商品の値段を加算する'''
        self.value += price

    def calc(self):
        '''最終的な料金を計算する'''
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        return math.ceil(total + tax)

# 実際の計算を行う
fee1 = CalcFee()
fee1.addItem(500)
print(fee1.calc(), "円") # 1620 円

fee2 = CalcFee()
fee2.shipping_fee = 1500
fee2.addItem(200)
fee2.addItem(300)
print(fee2.calc(), "円") # 2160 円
