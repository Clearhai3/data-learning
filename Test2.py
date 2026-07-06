# 第二天的练习题

# 题1: if 判断
# 用户输入一个分数 (0-100) , 输出等级: 90+ 为 "A"，80-89 为 "B"，60-79 为 "C"，60 以下为 "D"。
print("题1: 用户输入一个分数 (0-100) , 输出等级: 90+ 为 \"A\"，80-89 为 \"B\"，60-79 为 \"C\"，60 以下为 \"D\"。")
score = int(input("请输入一个分数 (0-100): "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

# 题2: 三元表达式
# 输入一个数，判断是奇数还是偶数 (一行解决) 。
num = int(input("请输入一个数: "))
print("偶数" if num % 2 == 0 else "奇数")

# 题3: 列表增删
# 创建一个空列表，用 append 依次添加 3 个你喜欢的食物，然后删除第二个。
foods = [];
foods.append("面条")
foods.append("汉堡")
foods.append("面包")
print(foods)
foods.pop(1)
print(foods)

# 题4: 列表去重
# 给定列表 num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 用循环和新列表实现去重 (不能用 set)。
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique) 

# 题5: range
# 用 range 生成 1 到 50 中所有 5 的倍数，存到列表里
result = list(range(5, 51, 5))
print(result)

# 题6: for 遍历
# 给定列表 prices = [29.9, 99.9, 49.9, 199.9, 9.9]，计算总价和平均价。
prices = [29.9, 99.9, 49.9, 199.9, 9.9]
total = sum(prices)             # 偷懒写法
avg = total / len(prices)

# 或者用循环:
total = 0
for price in prices:
    total += price
avg = total / len(prices)
print(f"总价: {total:.2f}，平均: {avg:.2f}")

# 题7: 九九乘法表
# 用 for 循环嵌套输出完整的九九乘法表。
for i in range (1, 10):
    for j in range (1, i + 1):
        print(f"{j}x{i}={i*j}", end = "\t")
    print()

# 题8: 猜数字游戏
# 程序随机生成 1-100 的数字，用户输入猜测，提示"大了"/"小了"，直到猜对为止，显示猜了几次
import random
target = random.randint(1, 101)
print(target)
total = 0
while True:
    user_input = int(input("请输入一个数字，来猜数字: "))
    total += 1
    if user_input == target:
        break
    elif user_input > target:
        print("大了")
    elif user_input < target:
        print("小了")
print(f"总共猜了 {total} 次")

# 题9: 密码输入
# 模拟登录: 密码为"123456", 用户最多输错3次，错满提示锁定，正确则提示成功并退出。
password = "123456"
max = 3
attempts = 0
max += 1
while attempts < max:
    user_input = input("请输入密码:")
    if user_input == password:
        print("密码正确")
        break
    else:
        attempts += 1
        print(f"密码错误, 还剩{max - attempts}次")
if attempts == max:
    print("已锁定。")
else:
    print("输入正确。")

# 题10: 统计正负数
# 输入 5 个整数，统计其中正数、负数、零的个数
positive = 0
negative = 0
zero = 0
nums = []
for i in range(5):
    user_input = int(input(f"请输入第{i + 1}个整数: "))
    nums.append(user_input)
    if user_input > 0:
        positive += 1
    elif user_input < 0:
        negative += 1
    else:
        zero += 1
print(f"输入的数字为:{nums}")
print(f"其中正数有{positive}个, 负数有{negative}个, 0有{zero}个")

# 总结：
# if / elif / else 多分支判断
# 知道三元表达式怎么写
# 列表增删改查 (append / insert / pop / remove)
# append 和 extend 的区别
# sort() 和 sorted() 的区别
# range()生成各种数字序列
# for 和 while 各写一个循环。
# break 和 continue 的区别

    
