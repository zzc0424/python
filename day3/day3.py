class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_pass(self):
        return self.score >= 60

students = [
    Student("小明", 85),
    Student("小红", 58),
    Student("小刚", 92),
]

lines = []
for s in students:
    if s.is_pass():
        status = "及格"
    else:
        status = "不及格"
    lines.append(f"{s.name}: {s.score}分 {status}")

with open("成绩报告.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("已写入 成绩报告.txt")