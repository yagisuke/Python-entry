# 継承(inheritance)の使用方法

import module.no66_car as car;

car1 = car.Van("Taro")
car1.turn_left()
car1.show_status()
# ---
# owner: Taro
# car_type: van
# handle: -90

car2 = car.Camper("Jiro")
car2.turn_right()
car2.show_status()
car2.make_ice()
# ---
# owner: Jiro
# car_type: camper
# handle: 90
# 氷を作りました
