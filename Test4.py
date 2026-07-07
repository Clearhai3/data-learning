# Python Day 4 练习题
# 题1: 列表推导式
# 用一行代码生成 1 到 20 中所有 3 的倍数的平方
result = [x**2 for x in range(1, 21) if x % 3 == 0]
print(result)       # [9, 36, 81, 144, 225, 324]

# 题2: 列表推导式 (if-else)
# 把一个列表中的正数保持不变，负数变成它的绝对值, 0 变成 "zero"
nums = [-3, 5, 0, -1, 8, -6, -0]
processed = [n if n > 0 else (abs(n) if n < 0 else "zero") for n in nums]
print(processed)        # [3, 5, 'zero', 1, 8, 6, 'zero']

# 题3: 字典推导式
# 给定字符串，生成每个字符出现次数字典
s = "hello world"
char_count = {c: s.count(c) for c in set(s) if c != " "}
print(char_count)
# {'r': 1, 'd': 1, 'h': 1, 'w': 1, 'l': 3, 'e': 1, 'o': 2}

# 题4: map
# 把一个字符串列表中的所有字符串转大写
words = ["hello", "world", "python"]
upper_words = list(map(lambda w: w.upper(), words))
# 或者更简单的
upper_words = list(map(str.upper, words))
print(upper_words)
# ['HELLO', 'WORLD', 'PYTHON']

# 题5: filter
# 过滤出列表中所有大于等于 60 的数
scores = [45, 78, 92, 33, 65, 88, 59]
passed = list(filter(lambda x: x >= 60, scores))
# 推导式写法 (推荐)
passed = [x for x in scores if x >= 60]
print(passed)
# [78, 92, 65, 88]

# 题6: reduce
# 求列表中所有元素的乘积
from functools import reduce
nums = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)
# 120

# 题7: sorted
# 给定一个包含文件名的列表，按文件扩展名排序
files = ["report.py", "data.csv", "image.png", "main.py", "readme.md"]
sorted_files = sorted(files, key = lambda f: f.split(".")[-1])
print(sorted_files)
# ['data.csv', 'readme.md', 'image.png', 'report.py', 'main.py']

# 题8: 综合
# 有一个学生列表，要求:
# - 筛选出成绩 >= 80 的学生
# - 按成绩降序排列
# - 只取姓名
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 88},
    {"name": "钱七", "score": 60},
]
top_names = [s["name"] for s in sorted(students, key = lambda s: s["score"], reverse = True) if s["score"] >= 80]
print(top_names)
# ['李四', '赵六', '张三']