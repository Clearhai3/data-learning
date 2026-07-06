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

# 不可变 (这是元组和列表唯一本质区别)
t = (1, 2, 3)
# t[0] = 10         # 错误 TypeError: 'tuple' object does not support item assignment
# 没有 append、remove、pop 等任何修改操作
# 只有两个方法: count 和 index
print(t.count(2))   # 1
print(t.count(3))   # 2

# 解包 (unpacking)
# 把元组元素一次性赋给多个变量
point = (3, 4)
x, y = point
print(x, y)         # 3 4

# 变量交换 (Python 独有优雅写法)
a, b = 10, 20
a, b = b, a
print(a, b)     # 20, 10

# 星号解包: 拿不定长度的
first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]  中间的被收集成一个列表
print(last)     # 5

# 什么时候用元组而不是列表?
# 数据创建后不需要修改      元组 (更安全，更省内存)
# 函数返回多个值            元组 (如 return x, y)
# 字典的键                 元组 (列表不能做键，因为列表可变)
# 需要增删改的集合          列表

# 元组做字典键:
locations = {(39.9, 116.4): "北京", (31.2, 121.5): "上海"}
print(locations[(39.9, 116.4)])         # "北京"
# 列表不能做键
# locations = {[39.9, 116.4]: "北京"}     # 报错 TypeError

# 集合set -- 无序、不重复
# 创建
# 花括号创建
s = {1, 2, 3, 3, 3}
print(s)        # {1, 2, 3} (自动去重)
# 空集合必须用 set(), 因为 {} 是空字典!
s = set()
print(type(s))      # <class 'set'>
# 从列表去重 (最常用场景)
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(nums))
print(unique)       # [1, 2, 3, 4] (顺序可能乱)

# 基本操作
s = {1, 2, 3}
# 增
s.add(4)            # 添加一个元素
print(s)            # {1, 2, 3, 4}
# 删
s.remove(2)         # 删除，原元素不存在会报 KeyError
print(s)            # {1, 3, 4}
s.discard(5)        # 删除，元素不存在不报错 (更安全)
popped = s.pop()    # 随机删除一个并返回 (集合无序, 不知道删了哪个)
# 查
print(1 in s)       # True
print(5 in s)       # False

# 集合运算 (交、并、差)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 交集 (两边都有的)
print(a & b)        # {3, 4}
print(a.intersection(b))
# 并集 (合在一起，自动去重)
print(a | b)        # {1, 2, 3, 4, 5, 6}
print(a.union(b))
# 差集 (a 有但 b 没有的)
print(a - b)        # {1, 2}
print(a.difference(b))
# 对称差集 (只在一边出现的，去掉共有部分)
print(a ^ b)        # {1, 2, 5, 6}
print(a.symmetric_difference(b))

# 函数
# 定义与调用
# def 函数名(参数列表):
#     """文档字符串 (可选，描述函数功能) """
#     代码块
#     return 返回值     # 可省略, 省略时返回 None

def greet(name):
    """向指定的人打招呼"""
    return f"你好, {name}!"
result = greet("张三")
print(result)

# 参数类型详解
# ———— 1. 位置参数 (按顺序传) ————
def add(a, b):
    return a + b
print(add(3, 5))    # 8

# ———— 2. 默认参数 (不传就用默认值) ————
def greet(name, greeting = "你好"):
    return f"{greeting}, {name}! "
print(greet("张三"))        # "你好，张三！"
print(greet("张三", "早上好"))  # "早上好，张三！"

# 注意: 默认参数必须是不可变类型! 千万别用列表做默认值!
# def bad_func(items=[]):         # 报错 危险写法
#     items.append(1)
#     return items
# print(bad_func())  # [1]
# print(bad_func())  # [1, 1]  <-  默认列表被多次调用共享了!
# 正确写法:
def good_func(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
print(good_func())
print(good_func())

# ———— 3. 关键字参数 (指定参数名，可以不按顺序) ————
def student_info(name, age, city):
    return f"{name}, {age}岁，来自{city}"
print(student_info(age=22, city="北京", name="张三"))   # 顺序无所谓

# ———— 4. 不定长参数 *args (接收任意数量的位置参数，存为元组) ————
def sum_all(*args):
    print(type(args))       # <class 'tuple'>
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10, 20))         # 30

# ———— 5. 不定长关键字参数 **kwargs (接收任意数量的关键字参数，存为字典) ————
def print_info(**kwargs):
    print(type(kwargs))     # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name = "张三", age = 22, city = "北京")
# name: 张三
# age: 22
# city: 北京

# ———— 混合使用时的参数顺序 (必须遵守!) ————
# def func(位置参数, *args, 默认参数, **kwargs):
#     pass

# 返回值
# 单个返回值
def square(x):
    return x ** 2

# 多个返回值 (本质是返回元组)
def min_max(nums):
    return min(nums), max(nums)
mn, mx = min_max([3, 1, 4, 1, 5])
print(mn, mx)   # 1 5

# 无 return -> 返回 None
def no_return():
    print("我没有返回值")
result = no_return()
print(result)   # None

# 作用域
x = 10      # 全局变量
def func():
    y = 20      # 局部变量，函数外无法访问
    global x
    x = 30
    print(x)    # 正确 可以读取全局变量
    # x = 30    # 错误 如果这样写，会在函数内创建一个局部变量 x
                # 和外部的 x 无关, print(x) 会报错 (还没赋值就读了)
    # 如果要修改全局变量:
    # global x
    # x = 30
func()
print(x)
# print(y)      # 报错 NameError (局部变量在函数外不可见)

# 原则: 尽量不用 global。通过参数传入，通过 return 传出。

# 类与面向对象 (入门)
# 定义类
class Student:
    # 类属性 (所有实例共享)
    school = "某某大学"
    # 构造方法 (初始化实例属性)
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    # 实例方法
    def introduce(self):
        return f"我叫{self.name}, {self.age}岁，成绩{self.score}分"
    # 修改成绩的方法
    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
        else:
            print("成绩必须在 0-100 之间")

# 使用类
# 创建实例 (调用类名即可，__init__ 自动执行)
s1 = Student("张三", 22, 85)
s2 = Student("李四", 21, 92)
# 访问属性
print(s1.name)      # "张三"
print(s1.school)    # "某某大学" (类属性, 所有实例都能访问)
# 调用方法
print(s1.introduce())   # "我叫张三，22岁，成绩85分"
s1.set_score(90)
print(s1.score)     # 90

# self是什么 (必须理解)
# self 代表实例本身。
# 当你写 s1.introduce() 时，Python实际上调用的是 Student.introduce(s1), 自动把，s1传给self
# 所以方法内部通过 self.xxx 访问的就是这个实例自己的属性。

# 下面两个完全等价:
# s1.introduce()
# Student.introduce(s1)

# 定义方法时第一个参数必须是 self (名字约定俗成，但不写会报错)。调用时不需要手动传 self。

# 继承 (了解即可)
class CollegeStudent(Student):      # 括号里写父类名
    def __init__(self, name, age, score, major):
        super().__init__(name, age, score)      # 调用父类的构造方法
        self.major = major
    # 重写父类方法（多态）
    def introduce(self):
        original = super().introduce()
        return f"{original}，专业是{self.major}"
cs = CollegeStudent("王五", 20, 88, "大数据")
print(cs.introduce())       # "我叫王五, 20岁，成绩88分，专业是大数据"
