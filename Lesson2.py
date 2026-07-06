# 条件判断+列表+for循环+while循环

# 条件判断 if / elif / else
# 基本语法
# 单分支
# if 条件:
#     执行代码

# 双分支
# if 条件:
#     执行代码
# else:
#     执行代码

# 多分支
# if 条件1:
#     执行代码
# elif 条件2:
#     执行代码
# else:
#     执行代码

# 三条铁律:
# 条件后面必须有冒号:
# 代码块必须缩进 (4个空格，整个项目统一就好)
# 缩进不对直接报 IndentationError

# 示例
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 注意: 从上到下依次判断，命中一个就跳出。
# 如果 score = 95，它会输出"优秀"然后结束，不会往下再看 80 和 60。

# 条件表达式 (三元表达式，一行写法)
# 语法: 值1 if 条件 else 值2
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)   # "成年"

# 实际场景: 输出调整
score = 88
print("及格" if score >= 60 else "不及格")

# 条件嵌套
age = 25
has_ticket = True
if age >= 18:
    if has_ticket:
        print("可以入场")
    else:
        print("请先购票")
else:
    print("未成年人禁止入场")

# 嵌套不要超过3层，否则很难读。能用 and 合并的就合并:
# 上面的嵌套等价于:
if age >= 18 and has_ticket:
    print("可以入场")
elif age >= 18 and not has_ticket:
    print("请先购票")
else:
    print("未成年人禁止入场")

# 条件判断中的"真"与"假"
# 以下值在 if 中被视为 False:
if 0:
    print("不会执行")
if "":
    print("不会执行")
if []:
    print("不会执行")
if None:
    print("不会执行")

# 以下值在 if 中被视为 True:
if 1:
    print("会执行")
if "hello":
    print("会执行")
if [1, 2]:
    print("会执行")

# 判断列表是否为空
users = []
if users:
    print("有用户")     # 等价于 if len(users) > 0:
else:
    print("无用户")     # 输出这个

# 判断用户输入是否为空
name = input("输入姓名: ").strip()      # 注意: strip()是去空白的
if name:                # 非空字符串 = True
    print(f"你好，{name}")
else:
    print("姓名不能为空")

# 列表 list (核心中的核心)
# 列表是 python 最常用的容器: 有序、可修改、元素可重复。

# 创建列表
nums = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橘子"]
mixed = [1, "hello", 3.14, True]    # 可以混合类型 (一般不建议)
empty = []                          # 空列表

# list() 构造函数
chars = list("hello")               # ['h', 'e', 'l', 'l', 'o']

# 索引 (和字符串完全一样)
fruits = ["苹果", "香蕉", "橘子", "西瓜"]
# 正向索引: 从 0 开始
print(fruits[0])    # "苹果"
print(fruits[1])    # "香蕉"
# 反向索引: -1 是最后一个
print(fruits[-1])   # "西瓜"
print(fruits[-2])   # "橘子"
# 切片: 和字符串一样 [起始:结束:步长], 左闭右开
print(fruits[0:2])  # ['苹果', '香蕉']      索引 0, 1，不含 2
print(fruits[1:3])  # ['香蕉', '橘子']
print(fruits[:2])   # ['苹果', '香蕉']      省略起始 = 从 0 开始
print(fruits[1:])   # ['香蕉', '橘子', '西瓜']  省略结束 = 到末尾
print(fruits[::2])  # ['苹果', '橘子']  步长 2
print(fruits[::-1]) # ['西瓜', '橘子', '香蕉', '苹果']  反转列表

# 增 (添加元素)
fruits = ["苹果", "香蕉"]
# append: 末尾追加一个元素 (最常用)
fruits.append("橘子")
print(fruits)       # ['苹果', '香蕉', '橘子']
# insert: 在指定索引位置插入
fruits.insert(1, "西瓜")
print(fruits)       # ['苹果', '西瓜', '香蕉', '橘子']
# 插入后，原来索引 1 及后面的元素全部后移
# extend: 合并另一个列表 (这个添加)
fruits.extend(["桃", "李"])
print(fruits)       # ['苹果', '西瓜', '香蕉', '橘子', '桃', '李']

# append vs extend 对比 (面试常问):
a = [1, 2]
a.append([3, 4])
print(a)    # [1, 2, [3, 4]]    -> 把整个列表当一个元素追加
a = [1, 2]  # 重置
a.extend([3, 4])
print(a)    # [1, 2, 3, 4]      -> 把列表拆开，逐个追加

# 删 (删除元素)
fruits = ["苹果", "香蕉", "橘子", "香蕉"]
# remove: 按值删除 (只删第一个匹配的)
fruits.remove("香蕉")
print(fruits)   # ['苹果', '橘子', '香蕉']  ->  只删掉了第一个"香蕉"
# 注意: 如果值不存在，会报 ValueError
# pop: 按索引删除并返回被删的元素
popped = fruits.pop()       # 不传参数 = 删除最后一个
print(popped)               # '香蕉'
print(fruits)               # ['苹果', '橘子']
popped = fruits.pop(0)      # 传参数 = 删除指定索引
print(popped)               # '苹果'
print(fruits)               # ['橘子']
# del :按索引删除，不返回
del fruits[0]
print(fruits)               #[]     当前的数组只剩下橘子，索引删除'橘子'
# clear: 清空整个列表
fruits.clear()
print(fruits)               #[]

# 改 (修改元素)
fruits = ["苹果", "香蕉", "橘子"]
# 直接按索引赋值
fruits[0] = "红富士"
print(fruits)               # ['红富士', '香蕉', '橘子']
# 批量修改 (切片赋值)
fruits[0:2] = ["哈密瓜", "葡萄"]
print(fruits)               # ['哈密瓜', '葡萄', '橘子']
# 切片赋值甚至可以改变列表长度
fruits[0:2] = ["瓜"]        # 把前两个元素替换成一个
print(fruits)               # ['瓜', '橘子']

# 查 (查找元素)
fruits = ["苹果", "香蕉", "橘子", "香蕉"]
# in: 判断是否存在 (最常用)
print("苹果" in fruits)         # True
print("西瓜" in fruits)         # False
# not in
print("西瓜" not in fruits)     # True
# index: 获取索引 (第一次出现的位置)
print(fruits.index("香蕉"))     # 1
# 如果不存在，会报 ValueError
# count: 统计出现次数
print(fruits.count("香蕉"))     # 2
print(fruits.count("西瓜"))     # 0

# 其他常用操作
nums = [3, 1, 4, 1, 5, 9, 2, 6]
len(nums)           # 长度: 8
max(nums)           # 最大值: 9
min(nums)           # 最小值: 1
sum(nums)           # 求和: 31
# sorted(): 返回新列表，原来列表不变
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(nums)         # [3, 1, 4, 1, 5, 9, 2, 6]  ->  没变
# sort(): 原地排序，原列表被修改
nums.sort()
print(nums)         # [1, 1, 2, 3, 4, 5, 6, 9]
# sort(reverse = True):降序
nums.sort(reverse=True)
print(nums)         # [9, 6, 5, 4, 3, 2, 1, 1]
# reverse(): 原地反转
nums.reverse()
print(nums)         # [1, 1, 2, 3, 4, 5, 6, 9]  -> 又反回来了

# for 循环
# 遍历列表
fruits = ["苹果", "香蕉", "橘子"]
# 直接遍历元素 (最常用)
for fruit in fruits:
    print(fruit)
# 苹果
# 香蕉
# 橘子

# 同时获取索引和元素: enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: 苹果
# 1: 香蕉
# 2: 橘子

# enumerate 可以指定起始索引
for i, fruit in enumerate(fruits, start = 1):
    print(f"{i}: {fruit}")
# 1: 苹果
# 2: 香蕉
# 3: 橘子

# range() —— 生辰数字序列
# range(n): 0 到 n-1
for i in range(5):
    print(i)            # 0, 1, 2, 3, 4
# range(start, stop): start 到 stop-1
for i in range(3, 8):
    print(i)            # 3, 4, 5, 6, 7
# range(start, stop, step): 带步长
for i in range(0, 10, 2):
    print(i)            # 0, 2, 4, 6, 8
# 反向: 步长为负数
for i in range(10, 0, -1):
    print(i)            # 10, 9, 8, ..., 1
# range 生成的不是列表，是"惰性序列"，按需产数字，不占内存
print(range(5))         # range(0, 5) -> 不是 [0,1,2,3,4]
print(list(range(5)))   # [0, 1, 2, 3, 4] -> 转成列表就看得到

# 循环嵌套: 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end = "\t")
    print()     # 每行结束换行
# 1*1=1
# 1*2=2   2*2=4
# 1*3=3   2*3=6   3*3=9
# 1*4=4   2*4=8   3*4=12  4*4=16
# 1*5=5   2*5=10  3*5=15  4*5=20  5*5=25
# 1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
# 1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
# 1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
# 1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81

# 遍历字典
student = {"name": "张三", "age": 22, "score": 85}
# 遍历键
for key in student:
    print(key)              # name, age, score

# 遍历值
for value in student.values():
    print(value)            # 张三, 22, 85

# 同时遍历键和值
for key, value in student.items():
    print(f"{key}: {value}")
# name: 张三
# age: 22
# score: 85

# while 循环
# 基本用法
count = 0
while count < 5:
    print(count)
    count += 1      # 必须更新条件变量，否则死循环!
# 输出: 0, 1, 2, 3, 4

# 无限循环 + break
# 不知道用户输入多少次，用 while True + break
while True:
    user_input = input("输入 'quit' 退出: ")
    if user_input == "quit":
        break                   # 立即跳出整个循环
    print(f"你输入了: {user_input}")

# continue —— 跳过本次循环
# 打印 0-9 中的奇数 (偶数跳过)
for i in range(10):
    if i % 2 == 0:
        continue        # 跳过本次循环，不执行下面的 print
    print(i)
# 输出: 1, 3, 5, 7, 9
# while 中用 continue (注意: 必须先把 count 自增，否则死循环)
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
# 输出: 1, 3, 5, 7, 9

# break 和 continue 的区别
#           break	continue
# 作用	结束整个循环	结束本次循环，进入下一次
# 后面代码	不执行，循环直接结束	不执行，但循环继续

# break 示例
for i in range(5):
    if i == 3:
        break
    print(i)
# 输出: 0, 1, 2 -> 到 3 就彻底停了
# continue 示例
for i in range(5):
    if i == 3:
        continue
    print(i)
# 输出: 0, 1, 2, 4  -> 跳过 3，继续后面的

# for vs while: 什么时候用哪个
# 知道循环次数 -> for
# for i in range(10):
#    ...

# 不知道循环次数，依赖某个条件 -> while
# while user_input != "quit":
#   ...

# 遍历一个容器 -> for
# for item in items:
#   ...

# else 子句 (Python 特有，了解即可)
# 循环正常结束 (没被 break 打断) 时执行 else
for i in range(5):
    print(i)
else:
    print("循环正常结束")   # 会执行

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("循环正常结束")   # 不会执行，因为break 打断了

# 实际用途: 查找元素，没找到时执行某个操作。
names = ["张三", "李四", "王五"]
target = "赵六"
for name in names:
    if name == target:
        print("找到了")
        break
else:
    print("没找到")     # 循环跑完都没 break，说明没找到

