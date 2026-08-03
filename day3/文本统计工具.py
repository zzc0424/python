def read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("文件不存在,请检查路径")
        return ""
    return content
def count_words(text):
    words = text.split()
    counts = {}
    for w in words :
        counts[w] = counts.get(w, 0) + 1
    return counts
text = read_file("test.txt")
print(count_words(text))
print(len(text.replace("\n", "")), len(text.splitlines()))