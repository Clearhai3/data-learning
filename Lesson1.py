# 变量
name1 = "张三"   # 把 "张三" 存到 name 里
age1 = 22        # 把 22 存到 age 里
height1 = 1.75   # 把 1.75 存到 height 里

# Python 变量不需要声明类型，直接写名字 = 值即可。运行时自动推断类型。


# 命名规则（违反直接报错）：

# 只能由字母、数字、下划线组成
# 不能以数字开头（1name 非法）
# 不能用 Python 关键字（if、for、class、def 等）

# 约定俗成的风格：

#变量名全部小写，单词之间用下划线: user_name、total_price
# 见名知意: a = 100 不如 student_count = 100

#type()

name2 = "Baka";
print(type(name2))

#整形int —— 整数
age2 = 22
count = -5
big = 999999999999999999999  # Python 不限制整数大小，自动处理

#注意: python的int没有溢出问题，多大都能存

#浮点型float —— 小数
height2 = 1.75
pi = 3.14159
negative = -0.5

#注意: 浮点数有精度问题(二进制无法精确表示某些小数)，这是所有语言的通病:
print(0.1 + 0.2)  # 输出 0.30000000000000004，不是 0.3

#字符串 str —— 文本
#单引号或双引号包裹都可以，没有区别:
name3 = 'Baka'
city1 = "北京"

# 三引号用于多行文本:
intro = """这是第一行
这是第二行
这是第三行"""

# 字符串一旦创建，不可修改(和java 一样，是immutable的):
s = "hello"
# s[0] = "H"   错误 报错 TypeError
# 想改只能重新赋值:
s = "H" + s[1:]  # 正确 "Hello"

# 布尔值bool —— 真假
# 只有两个值: True 和 False (首字母必须大写)。
is_student = True
is_working = False

# 布尔值由比较运算产生:
print(10 > 5)   # True
print(10 == 5)  # False
print(10 != 5)  # True

# True 等价于 1，False 等价于 0
print(True + 1)   # 2
print(False * 0)  # 0
# 空的东西都是 False，非空的是True
bool(0)       # False
bool("")      # False
bool([])      # False
bool("abc")   # True
bool(42)      # True

# 类型转换
# 三个最常用的转换函数:
int("123")     # 字符串 -> 整数: 123
float("3.14")  # 字符串 -> 浮点: 3.14
str(100)       # 数字 -> 字符串: "100"

# 常见踩坑:
# int("3.14")         # 错误 报错！ int() 不接受带小数点的字符串
int(float("3.14"))  # 正确 先转 float 再转 int -> 3 (直接截断)

# print() —— 输出到屏幕
print("你好")               # 输出：你好
print("你好", "世界")       # 输出：你好 世界（自动空格分隔）
print("你好", end="!!!")    # 输出：你好!!!（end 默认是换行符 \n）

print("")

# f-string (Python最推荐的格式化方式):
name4 = "Baka"
age3 = 22
# f 开头，花括号里直接写变量名:
print(f"我叫{name4}, 今年{age3}岁")
# 输出: 我叫张三，今年22岁
# 花括号里可以写表达式:
print(f"5年后我{age3 + 5}岁")
# 输出 5年后我27岁
# 控制小数位数:
pi = 3.14159
print(f"圆周率: {pi:.2f}")
#输出: 圆周率: 3.14

# % 格式化（老式，不推荐）
print("我叫%s，今年%d岁" % (name4, age3))
# .format()（过渡方案）
print("我叫{}，今年{}岁".format(name4, age3))

# 结论：只用 f-string。 简洁、直观、性能最好。

# input() —— 从键盘读取输入
# 最关键的一点: input()返回的永远是字符串!
# name5 = input("请输入你的名字: ")
# print(f"你好, {name5}")

# 如果要获取数字，必须手动转换:
# age_str = input("请输入年龄: ")  # 用户输入 "22"
# age4 = int(age_str)             # 转成整数
# print(f"5年后你{age4 + 5}岁")   # 5年后你27岁

# 常见错误:
# age = input("请输入年龄: ")
# print(f"5年后你{age + 5}岁")   # ❌ 报错！字符串不能加数字
# 因为 age 是 "22"（字符串），"22" + 5 没有意义

# 运算符
# 算术运算符
# +	加	10 + 3	13
# -	减	10 - 3	7
# *	乘	10 * 3	30
# /	除（结果总是浮点）	10 / 3	3.3333333333333335
# //	整除（向下取整）	10 // 3	3
# %	取余（模运算）	10 % 3	1
# **	幂运算	10 ** 3	1000

# / 和 // 的区别是高频考点：
print(10 / 3)       # 3.3333333333333335 (普通除法，结果是浮点)
print(10 // 3)      # 3 (整除，丢掉小数部分，结果是整数)
print(-10 // 3)     # -4 (因为 -3.333... 向下取整 = -4，不是 -3)

# % 取余的实际用途：

# 判断奇数偶数
print(7 % 2)        # 1 -> 奇数
print(8 % 2)        # 0 -> 偶数
# 取个位数
print(123 % 10)     # 3

# 比较运算符
# 结果永远是True或False:
# ==	等于
# !=	不等于
# >	    大于
# <	    小于
# >=	大于等于
# <=	小于等于

# 最常见新手错误:混淆 = 和 ==
# = 是赋值
x = 10
# == 是比较
print(x == 10)      # True
print(x == 5)       # False
# if 条件里必须用 ==
if x == 10:     # 正确
    print("x 是 10")
# if x = 10:    # 错误

# 逻辑运算符
# 用来组合多个条件:
# and: 同时满足
print(10 > 5 and 3 < 8)     # True (两个都对)
print(10 > 5 and 3 > 8)     # False (一个错就全错)
# or: 有一个满足就行
print(10 > 5 or 3 > 8)      # True (有一个对就行)
print(10 < 5 or 3 > 8)      # False (两个都错才行)
# not: 取反
print(not True)             # False
print(not 10 > 5)           # False (因为 10>5 是 True，取反就是 False)

# 短路逻辑
# and 短路: 左边是False, 右边不执行
False and print("不会打印")     # 右边根本不会运行
# or 短路: 左边是True, 右边不执行
True or print("不会打印")       # 右边根本不会运行

# 赋值运算符（简写）

# x = 10
# x += 3    # 等价于 x = x + 3，现在 x 是 13
# x -= 2    # 等价于 x = x - 2，现在 x 是 11
# x *= 3    # 等价于 x = x * 3，现在 x 是 33
# x /= 2    # 等价于 x = x / 2，现在 x 是 16.5
# x //= 3   # 等价于 x = x // 3
# x %= 4    # 等价于 x = x % 4
# x **= 2   # 等价于 x = x ** 2

# 运算符优先级（记住一条就够了）

# 算术 > 比较 > 逻辑。 记不住就加括号：
# 不确定顺序? 直接加括号，永远不出错
result = (10 + 5) * (3 - 1)     # 清晰明了
# 下面两个等价，但加括号更易读
score = 90
if (age1 >= 18 ) and (score >= 60):
    print("及格")
if age1 >= 18 and score >= 60:
    print("及格")

# 字符串操作
# 字符串定义回顾
s1 = 'hello'
s2 = "hello"     # 单双引号没区别
s3 = """多行
文本"""          # 三引号保留换行

# 索引与切片（核心中的核心）
# 字符串中每个字符都有编号，从 0 开始：
# 字符： h   e   l   l   o
# 索引： 0   1   2   3   4
# 反向：-5  -4  -3  -2  -1

s = "hello"
# 索引取单个字符
print(s[0])     # 'h'
print(s[2])     # 'l'
print(s[-1])    # 'o' (负数从右边数，-1 是最后一个)
print(s[-2])    # 'l'
# 越界会报错:
# print(s[10])  # x IndexError

# 切片: [起始:结束:步长] — 这是重点，多花 10 分钟彻底搞懂。
s = "hello"
# 规则: 包含起始，不包含结束(左闭右开)
print(s[0:3])       # 'hel'     (索引 0,1,2，索引 3 不包含)
print(s[1:4])       # 'ell'     (索引 1,2,3)
print(s[:3])        # 'hel'     (省略起始 = 从0开始)
print(s[2:])        # 'llo'     (省略结束 = 到末尾)
print(s[:])         # 'hello'   (省略两边 = 整个字符串)
# 步长(第三个参数) :
print(s[::2])       # 'hlo'     (每隔一个取一个)
print(s[::-1])      # 'olleh'   (步长负数 = 反向! 这是最常用的反转字符串技巧)
#综合:
print(s[0:4:2])     # 'hl'      (从索引 0 到 4，步长 2)

# 字符串拼接
# 用 + 拼接 (简单但效率低，适合少量字符串)
s = "hello" + " " + "world"     # "hello world"
# 用 join 拼接 (大量字符串拼接必须用这个，效率高)
words = ["你好", "世界", "Python"]
s = " ".join(words)             # "你好 世界 Python"
s = ", ".join(words)            # "你好，世界，Python"
# f-string 中也算拼接
name = "Baka"
s = f"欢饮{name}"               # "欢迎张三"

# 最常用的字符串方法
# replace —— 替换
s = "hello world"
print(s.replace("world", "Python"))     # "hello Python"
print(s.replace("l", "L"))              # "heLLo worLd" (所有匹配的都替换)
print(s.replace("l", "L", 1))           # "heLlo world" (只替换第一个)

# split —— 切割 (极其常用)
s = "苹果,香蕉,橘子"
print(s.split(","))     # ['苹果', '香蕉', '橘子'] (返回列表)
s = "hello world python"
print(s.split())        # ['hello', 'world', 'python'] (默认按空白字符切)
# 注意: split 返回的永远是列表

# strip / lstrip / rstrip — 去空白
s = "  hello world  \n"
print(s.strip())        # "hello world" (去掉两端空白和换行)
print(s.lstrip())       # "hello world  \n" (只去左边)
print(s.rstrip())       # "  hello world" (只去右边)
# 也可以去掉指定字符:
s = "!!!hello!!!"
print(s.strip("!"))     # "hello"

# upper / lower — 大小写
s = "Hello World"
print(s.upper())        # "HELLO WORLD"
print(s.lower())        # "hello world"
# 实际用途: 不区分大小写的比较
user_input = input()
if user_input.upper() == "YES":     # 用户输入 yes/YES/Yes
    print("确认")

# find / index — 查找子串位置
s = "hello world"
print(s.find("world"))      # 6 (返回第一次出现的位置，没找到返回 -1)
print(s.find("l"))          # 2 (返回第一次出现的位置)
print(s.find("xxx"))        # -1 (没找到)
print(s.index("world"))     # 6 (和 find 一样，但没找到会报错而非返回 -1)

# 实际使用建议：用 find，别用 index。 find 找不到返回 -1，index 找不到直接报错，程序会崩。

# startswith / endswith —— 判断开头结尾
s = "report_2026.pdf"
print(s.startswith("report"))   # True
print(s.endswith(".pdf"))       # True
print(s.endswith(".xlsx"))      # False

# count —— 统计出现次数
s = "hello hello world"
print(s.count("hello"))     # 2
print(s.count("l"))         # 5

# isdigit / isalpha — 判断字符类型
print("123".isdigit())      # True (纯数字)
print("12.3".isdigit())     # False (小数点不算数字)
print("abc".isalpha())      # True (纯字母)
print("abc123".isaplpha())  # False (混合了数字)

# len() — 获取长度
# len() 不是字符串的方法，是内置函数，但极其常用：
s = "hello world"
print(len(s))       # 11 (空格也算一个字符)
print(len(""))      # 0
print(len("您好"))   # 2 (一个汉字算一个字符)

# 转义字符
print("第一行\n第二行")     # \n 换行
print("他说: \"你好\"")     # \" 在字符串里放双引号
print("C:\\User\\张三")     # \\ 表示一个真正的反斜杠
print("hello\tworld")       # \t 制表符 (Tab)

# 字符串不可变性 (再强强调一次)
s = "hello"
# s[0] = "H"       # ❌ 报错！不能原地修改

# 正确的做法是创建新字符串：
s = "H" + s[1:]  # ✅ s 现在指向新字符串 "Hello"
