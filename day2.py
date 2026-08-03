fruits = ["苹果","香蕉","橘子"]
fruits.append("西瓜")
for fruit in fruits:
    print(fruit)
fruits.remove("香蕉")
for fruit in fruits:
    print(fruit)
fruits[1] = "草莓"
print(fruits)
print(f"现在有{len(fruits)}种水果")