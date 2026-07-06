# Python Day 3: 字典 + 元组 + 集合 + 函数 + 类入门

# 字典 dict -- 键值对 (极其重要)

# 创建字典
# 花括号创建 (最常用)
student = {"name": "张三", "age": 22, "score": 85}

# dict() 构造函数
student2 = dict(name = "李四", age = 23, score = 92)

# 空字典
empty = {}

# 取值
student = {"name": "张三", "age": 22, "score": 85}
# 方式1: 方括号 (键不存在会报错 KeyError)
print(student["name"])          # "张三"
# print(student["gender"])        # 错误 KeyError : 'gender'
# 方式2: get() (键不存在返回 None, 不报错, 推荐! )
print(student.get("name"))      # "张三"
print(student.get("gender"))    # None
print(student.get("gender", "未知"))    # "未知" (可指定默认值)

# 结论: 取值优先用 get() , 不会崩程序。

# 增 / 改
student = {"name": "张三", "age": 22}
# 键存在 -> 修改
student["age"] = 23
print(student)      # {'name': '张三', 'age': 23}
# 键不存在 -> 新增
student["gender"] = "男"
print(student)      # {'name': '张三', 'age': 23, 'gender': '男'}
# 批量更新
student.update({"age": 24, "score": 88, "city": "北京"})
print(student)
# {'name': '张三', 'age': 24, 'gender': '男', 'score': 88, 'city': '北京'}

# 删
student = {"name": "张三", "age": 22, "score": 85, "gender": "男"}
# del: 删除键值对
del student["gender"]
print(student)      # {'name': '张三', 'age': 22, 'score': 85}
# pop: 删除并返回被删的值
score = student.pop("score")
print(score)        # 85
print(student)      # {'name': '张三', 'age': 22}
# popitem: 删除并返回最后一个键值对 (Python 3.7+ 字典有序)
key, value = student.popitem()
print(key, value)
# clear: 清空
student.clear()
print(student)      # {}

# 遍历字典
student = {"name": "张三", "age": 22, "score": 85}
# 遍历键
for key in student:
    print(key)          # name, age, score
for key in student.keys():
    print(key)          # 同上，显示写法
# 遍历值
for value in student.values():
    print(value)        # 张三, 22, 85
# 同时遍历键和值 (最常用！)
for key, value in student.items():
    print(f"{key}: {value}")
# name: 张三
# age: 22
# score: 85

# 字典推导式
# 语法: {键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
# 把列表转成字典: 单词 -> 长度
words = ["apple", "banana", "cat"]
word_len = {w: len(w) for w in words}
print(word_len)
# {'apple': 5, 'banana': 6, 'cat': 3}

# 过滤
long_words = {w: len(w) for w in words if len(w) > 4}
print(long_words)
# {'apple': 5, 'banana': 6}

# 反转键和值
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)
# {1: 'a', 2: 'b', 3: 'c'}

# 字典嵌套 (实际开发极常用)
# 列表套字典
students = [
    {"name": "张三", "age": 22, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 23, "score": 78},
]
# 遍历列表中的字典
for s in students:
    print(f"{s['name']} - {s['score']}分")
# 字典套列表
grades = {
    "张三": [85, 90, 88],
    "李四": [92, 95, 89],
}
print(grades["张三"][1])     # 90 (张三的第2次成绩)

# 元组 tuple -- 不可变的列表
# 创建
# 括号创建
t = (1, 2, 3)
# 括号可省略
t = 1, 2, 3
print(t)    # (1, 2, 3)
# 单元素元组: 必须加逗号! (高频易错点)
t = (1)     # 错误 这不是元组，是加了括号的整数 1
print(type(t))  # <class 'int'>
t = (1,)    # 正确 这才是单元素元组
print(type(t))  # <class 'tuple'>
# 空元组
t = ()

# 取值 (支持索引、切片，和列表一样)
t = (10, 20, 30, 40, 50)
print(t[0])         # 10
print(t[-1])        # 50
print(t[1:4])       # (20, 30, 40)