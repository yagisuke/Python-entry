# FizzBuzzゲームのプログラム
#  - 3で割り切れる数はFizz
#  - 5で割り切れる数はBuzz
#  - 3でも5で割り切れる数はFizzBuzz

for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)
