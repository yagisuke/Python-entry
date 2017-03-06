# 継承(inheritance)
class Car:
    '''基本的な自動車の機能を備えたクラス'''

    def __init__(self, owner):
        self.handle = 0
        self.car_type = "normal"
        self.owner = owner

    def turn_left(self):
        '''ハンドルを左に回す'''
        self.handle -= 90

    def turn_right(self):
        '''ハンドルを右に回す'''
        self.handle += 90

    def show_status(self):
        '''状態を表示'''
        print("---")
        print("owner:", self.owner)
        print("car_type:", self.car_type)
        print("handle:", self.handle)

class Van(Car):
    '''ワゴン車のクラス'''

    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "van"

    def open_door(self):
        '''自動でドアを開ける'''
        print("ドアを開けました")

    def close_door(self):
        '''自動でドアを閉める'''
        print("ドアを閉じました")

class Camper(Car):
    '''キャンピングカーのクラス'''

    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "camper"

    def make_ice(self):
        '''氷を作る'''
        print("氷を作りました")
