import random
target = random.randint(1, 100)
win = False
for i in range(1, 8):
    a = input('请输入你猜的数字：')
    a = int(a)
    if a > target:
        print("大了")
    elif a < target:
        print("小了")
    else:
        print("猜对了")
        win = True
        break
if not win:
    print(f"次数用完了,答案是{target}")