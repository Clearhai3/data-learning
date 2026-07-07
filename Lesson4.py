# Python Day 4: 推导式 + Lambda + map/filter/reduce + sorted

# 列表推导式 
# 基本语法
# [表达式 for 变量 in 可迭代对象 if 条件]

# 把 for 循环压缩到一行。所有能用列表推导式的地方，都能展开成普通 for 循环。

# 基础用法
# 普通 for 循环写法
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 推导式一行搞定
squares = [x**2 for x in range(10)]

# 对比记忆: 把 for 循环的写法在脑子里反转一下————先想"我要什么结果 (x^2)"，再想"数据从哪来 (for x in range(10))"。

# 带条件过滤
# 只要偶数
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
# [0, 4, 16, 36, 64]
# 普通写法对比
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)

# 带 if - else (注意位置！)
# if - else 写在 for 前面，if 过滤写在 for 后面。这是最容易混淆的地方。
# if-else 在 for 前面 -> 是对表达式做条件判断 (每个元素都有输出)
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(5)]
print(labels)
# ['偶数', '奇数', '偶数', '奇数', '偶数']
# if 在 for 后面 -> 是过滤 (不符合条件的直接丢掉)
evens = [x for x in range(5) if x % 2 == 0]
print(evens)
# [0, 2, 4]

# 记忆诀窍:
# 结果需要每个元素都出现 (只是值不同) -> A if 条件 else B 放 for 前面
# 结果需要筛掉某些元素 -> if 条件 放 for 后面

# 嵌套循环
# 两层循环: 生成坐标对
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 等价普通写法
pairs = []
for x in range(3):
    for y in range(3):
        pairs.append((x, y))
print(pairs)
# 循环顺序: 外层在前，内层在后，和普通 for 循环的嵌套顺序一致。

# 实际场景
# 提取字典列表中某个字段
students = [{"name": "张三", "score": 85}, {"name": "李四", "score": 92}]
names = [s["name"] for s in students]
print(names)
# ['张三', '李四']
# 过滤 + 转换
high_scores = [s["name"] for s in students if s["score"] >= 90]
print(high_scores)
# ['李四']
# 字符串操作
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)
# ['HELLO', 'WORLD', 'PYTHON']

# 字典推导式
# 语法: {键表达式：值表达式 for 变量 in 可迭代对象 if 条件}
# 单词 -> 长度
words = ["apple", "banana", "cat"]
word_len = {w: len(w) for w in words}
print(word_len)
# {'apple': 5, 'banana': 6, 'cat': 3}

# 带过滤: 只要长度大于 3 的
long_word_len = {w: len(w) for w in words if len(w) > 3}
print(long_word_len)
# {'apple': 5, 'banana': 6}

# 反转键值对
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)
# {1: 'a', 2: 'b', 3: 'c'}

# 从两个列表创建字典
keys = ["name", "age", "city"]
values = ["张三", 22, "北京"]
d = {k: v for k, v in zip(keys, values)}
print(d)
# {'name': '张三', 'age': 22, 'city': '北京'}

# Lambda 匿名函数
# 语法
# lambda 参数1, 参数2, ... : 返回值表达式
# 特点:
# 只能写一个表达式 (不能写多行代码，不能有循环、赋值语句)
# 自动 return 表达式的值 (不需要写 return)
# 用完即扔，不需要起函数名
# 普通函数
def add(a, b):
    return a + b
print(add(3, 5))
# lambda 等价
add = lambda a, b: a + b
print(add(3, 5))        # 8 (两种方式调用完全一样)

# lambda 真正的用武之地 ———— 作为参数
# lambda 单独用意义不大，它的核心价值是传给其他函数当参数。典型场景就是下面要讲的 map、filter、sorted。
# 不推荐的用法 (不如直接写普通函数)
# square = lambda x: x**2
# 推荐用法一直接当参数传
x = list(map(lambda x: x**2, [1, 2, 3]))
print(x)

# map -- 对每个元素执行相同操作
# 语法: map(函数，可迭代对象)
# 返回 map 对象（惰性），需要 list() 转换才能看到
nums = [1, 2, 3, 4, 5]
# 每个元素平方
squared = list(map(lambda x: x**2, nums))
print(squared)
# [1, 4, 9, 16, 25]
# 转换成字符串
str_nums = list(map(str, nums))
print(str_nums)
# ['1', '2', '3', '4', '5']
# 用内置函数 (不需要 lambda)
abs_nums = list(map(abs, [-1, -2, 3, -4]))
print(abs_nums)
# [1, 2, 3, 4]

# 多个可迭代对象
a = [1, 2, 3]
b = [10, 20, 30]
# 两个列表对应位置相加
summed = list(map(lambda x, y: x + y, a, b))
print(summed)
# [11, 22, 33]
# 多个列表，按最短的截断
c = [100, 200]
short = list(map(lambda x, y, z: x + y + z, a, b, c))
print(short)
# [111, 222]  <-  只处理了前两个，因为 c 只有两个元素

# map vs 列表推导式
nums = [1, 2, 3, 4, 5]
# 列表推导式 (更 Pythonic, 更推荐)
[x**2 for x in nums]
# map + lambda (功能一样，但可读性略差)
list(map(lambda x: x**2, nums))

# 结论: 能用列表推导式就用列表推导式，更直观。map 只有一种情况更简洁————函数名直接传入 (如 map(str, nums))。

# filter ——— 过滤不符合条件的元素
# 语法: filter(函数，可迭代对象)
# 函数返回 True 的元素保留，返回 False 的丢弃
nums = [1, 2, 3, 4, 5, 6]
# 只保留偶数
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
# [2, 4, 6]
# 过滤空字符串
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda s: s != "", strings))
print(non_empty)
# ['hello', 'world', 'python']
# 更简洁: filter(None, ...) 自动过滤掉 False 值
non_empty = list(filter(None, strings))
print(non_empty)
# ['hello', 'world', 'python'] ("" 是 False，被过滤)

# filter vs 列表推导式
nums = [1, 2, 3, 4, 5, 6]
# 列表推导式 (推荐)
[x for x in nums if x % 2 == 0]
# filter (也行)
list(filter(lambda x: x % 2 == 0, nums))
# 同样，列表推导式更直观。

# reduce —— 累积计算
from functools import reduce
# 语法: reduce(函数，可迭代对象[, 初始值])
# 函数接收两个参数: 累积值和当前元素
nums = [1, 2, 3, 4, 5]
# 求和: (((1+2)+3)+4)+5
total = reduce(lambda acc, x: acc + x, nums)
print(total)    # 15
# 阶乘: (((1*2)*3)*4)*5
product = reduce(lambda acc, x: acc * x, nums)
print(product)  # 120
# 带初始值 (初始值参与第一次计算)
total_with_init = reduce(lambda acc, x: acc + x, nums, 10)
print(total_with_init)  # 25 (10+1+2+3+4+5)

# acc  当前元素  操作后
#   1     2      1+2=3     ← 默认初始值是列表第一个元素
#   3     3      3+3=6
#   6     4      6+4=10
#  10     5      10+5=15
# 最终返回 15

# acc  当前元素  操作后
#  10     1      10+1=11   ← 从初始值开始
#  11     2      11+2=13
#  13     3      13+3=16
#  16     4      16+4=20
#  20     5      20+5=25
# 最终返回 25

# reduce 常见场景
# 找最大值
max_val = reduce(lambda acc, x: acc if acc > x else x, [3, 7, 2, 9, 1])
print(max_val)
# 9 (其实直接用 max() 就行)
# 字符串拼接
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda acc, w: acc + w, words)
print(sentence)
# "Hello World!" (其实直接用 "".join(words) 更高效)
# 注意: reduce 没有直接的推导式替代方案。但实际开发中 reduce 用得不多，大部分场景有更直接的方法 (sum、max、join等)。

# sorted + lambda (极其常用，务必掌握)
# sorted() 基本用法
# sorted(可迭代对象，key=排序依据函数，reverse=是否降序)
# 返回新列表，原列表不变
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)      
sorted_desc = sorted(nums, reverse = True)
print(sorted_nums)          # [1, 1, 2, 3, 4, 5, 9]
print(sorted_desc)          # [9, 5, 4, 3, 2, 1, 1]

# key 参数 ———— 真正的威力
# key 不是比较规则，而是"提取比较依据"。对每个元素执行 key 函数，按函数返回值排序。
# 按字符串长度排序
words = ["apple", "pie", "banana", "a", "cat"]
sorted_words = sorted(words, key = len)
print(sorted_words)
# ['a', 'pie', 'cat', 'apple', 'banana']
# 按绝对值排序
nums = [-5, 3, -1, 4, -2]
sorted_nums = sorted(nums, key = abs)
print(sorted_nums)
# [-1, -2, 3, 4, -5]    ← 按绝对值：1, 2, 3, 4, 5

# 排序字典列表 (面试必考)
students = [
    {"name": "张三", "age": 22, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 23, "score": 78},
]
# 按分数升序
sorted_by_score = sorted(students, key = lambda s: s["score"])
print(sorted_by_score)
# [{'name': '王五', 'age': 23, 'score': 78}, {'name': '张三', 'age': 22, 'score': 85}, {'name': '李四', 'age': 21, 'score': 92}]
# 王五(78) → 张三(85) → 李四(92)
# 按分数降序
sorted_by_score_desc = sorted(students, key = lambda s: s["score"], reverse = True)
print(sorted_by_score_desc)
# [{'name': '李四', 'age': 21, 'score': 92}, {'name': '张三', 'age': 22, 'score': 85}, {'name': '王五', 'age': 23, 'score': 78}]
# 先按年龄，再按分数（元组作为 key）
sorted_multi = sorted(students, key = lambda s: (s["age"], s["score"]))
print(sorted_multi)
# [{'name': '李四', 'age': 21, 'score': 92}, {'name': '张三', 'age': 22, 'score': 85}, {'name': '王五', 'age': 23, 'score': 78}]
# 李四(21,92) → 张三(22,85) → 王五(23,78)

# sorted() vs list.sort()
# | | `sorted()` | `list.sort()` |
# |------|-----------|---------------|
# | 返回值 | 返回**新列表** | 返回 **None** |
# | 原列表 | **不变** | **被修改** |
# | 适用类型 | 任何可迭代对象 | 只能列表用 |

nums = [3, 1, 2]
# sorted: 原列表不变
new_nums = sorted(nums)
print(nums)         # [3, 1, 2]  <-  没变
print(new_nums)     # [1, 2, 3]
# sort: 原地修改
nums.sort()
print(nums)         # [1, 2, 3]  <-  被改了