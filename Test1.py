# 题1:用户输入姓名和年龄，输出"我叫xx，今年x岁，5年后我x岁"
name = input("请输入姓名:")
age = int(input("请输入年龄:"))

print(f"我叫{name}，今年{age}岁，5年后我{age + 5}岁")

# 题2:输入一个字符串，输出它的长度、全部大写、全部小写、去掉两端空格
s = input("请输入一句英语:")
print(f"长度:{len(s)}")
print(f"全部大写:{s.upper()}")
print(f"全部小写:{s.lower()}")
print(f"去掉两端:{s.strip()}")

# 题3:理解切片--写出下面每行的输出(自己在纸上算，再敲代码验证)
s = "Python"
print(s[0:3])       # Pyt
print(s[3:])        # hon
print(s[::-1])      # nothyP
print(s[::2])       # Pto
print(s[1:5:2])     # yh

# 题4: 输入用逗号分隔的三个单词，用 split 拆开，反转顺序后输出
words = input("请输入三个单词，用逗号隔开:")
word_list = words.split(",")
print(f"{word_list[2]}{word_list[1]}{word_list[0]}")

# 题5: 输入一个整数，判断它是奇数还是偶数
n = int(input("请输入一个整数:"))
print(f"{n}是{'偶数' if n % 2 == 0 else '奇数'}")
