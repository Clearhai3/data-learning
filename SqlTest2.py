# 聚合函数 + GROUP BY + HAVING
import sqlite3

# 创建内存数据库（关掉就没了，适合练习）
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# 建一张员工表
cur.execute("""
    CREATE TABLE employee (
        id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        age INTEGER,
        salary REAL,
        department TEXT,
        hire_date TEXT
    )
""")

# 插入练习数据
employees = [
    (1, '张三', '男', 28, 15000, '技术部', '2020-03-15'),
    (2, '李四', '女', 32, 18000, '技术部', '2018-07-01'),
    (3, '王五', '男', 25, 9000, '市场部', '2022-06-10'),
    (4, '赵六', '女', 29, 12000, '市场部', '2019-11-20'),
    (5, '钱七', '男', 35, 22000, '技术部', '2016-01-05'),
    (6, '孙八', '女', 27, 11000, '人事部', '2021-04-18'),
    (7, '周九', '男', 31, 16000, '人事部', '2018-09-30'),
    (8, '吴十', '女', 26, 8500, '市场部', '2023-01-12'),
    (9, '郑十一', '男', 40, 25000, '技术部', '2014-05-20'),
    (10, '冯十二', '女', 24, 7500, '人事部', '2023-08-01'),
]

cur.executemany("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?)", employees)
conn.commit()

# 以后每次查询就这样写：
def query(sql):
    """执行查询并打印结果"""
    cur.execute(sql)
    rows = cur.fetchall()
    # 打印列名
    col_names = [desc[0] for desc in cur.description]
    print(" | ".join(col_names))
    print("-" * 50)
    for row in rows:
        print(" | ".join(str(x) for x in row))
    print()

# COUNT -- 计数
# -- 公司有多少员工? 
# SELECT COUNT(*) FROM employee;
# -- 结果: 10
query("""
      SELECT COUNT(*) 
      FROM employee
      """)

# -- COUNT(列名): 统计该列非 NULL 的行数
# SELECT COUNT(department) FROM employee;
# -- 结果: 10 (因为没有 NULL )
query("""
      SELECT COUNT(department) 
      FROM employee
      """)

# -- COUNT(DISTINCT 列名): 去重后计数
# SELECT COUNT(DISTINCT department) FROM employee;
# -- 结果: 3 (技术部、市场部、人事部)
query("""
      SELECT COUNT(DISTINCT department)
      FROM employee
      """)

# COUNT(*) vs COUNT(列名)：

# COUNT(*)：统计所有行（包括 NULL）
# COUNT(列名)：只统计该列不为 NULL 的行
# 绝大多数情况下用 COUNT(*) 就行

# SUM -- 求和
# -- 公司每月工资总支出?
# SELECT SUM(salary) FROM employee;
# -- 结果: 144000.0
query("""
      SELECT SUM(salary) 
      FROM employee
      """)

# -- 技术部的总薪资
# SELECT SUM(salary) FROM employee WHERE department = '技术部';
# -- 结果: 80000.0
query("""
      SELECT SUM(salary) 
      FROM employee 
      WHERE department = '技术部'
      """)

# AVG -- 平均值
# -- 全体员工平均薪资
# -- 结果: 14400.0
# SELECT AVG(salary) FROM employee;
query("""
      SELECT AVG(salary)
      FROM employee
      """)

# 技术部平均薪资
# SELECT AVG(salary) FROM employee WHERE department = '技术部';
# -- 结果: 20000.0
# -- AVG 自动忽略 NULL 值
query("""
      SELECT AVG(salary)
      FROM employee
      WHERE department = '技术部'
      """)

# MAX / MIN -- 最大 / 最小值
# -- 最高薪资
# SELECT MAX(salary) FROM employee;
# -- 结果: 25000.0
query("""
      SELECT MAX(salary)
      FROM employee
      """)

# -- 最早入职日期 (日期字符串可以比大小，越早越小)
# SELECT MIN(hire_date) FROM employee;
# -- 结果: 2014-05-20
# -- 同时查多个聚合值
query("""
      SELECT MIN(hire_date)
      FROM employee
      """)

# -- 同时查多个聚合值
# SELECT MAX(salary), MIN(salary), AVG(salary) FROM employee;
# 结果: 25000.0 | 7500.0 | 14400.0
query("""
      SELECT MAX(salary), MIN(salary), AVG(salary)
      FROM employee
      """)

# 聚合函数的关键理解
# 聚合函数把多行压成一行。
# -- 这个会报错或者返回奇怪的结果 (取决于数据库) :
# SELECT name, MAX(salary) FROM employee;
# -- name 有 10 行, MAX(salary) 只有 1 行, 对不齐！
query("""
      SELECT name, MAX(salary)
      FROM employee
      """)

# 这就是为什么要用 GROUP BY。

# GROUP BY -- 分组
# GROUP BY 把数据按某一列的值分成多个组，每个组内部做聚合。
# -- 按部门分组，看每个部门的平均薪资
# SELECT department, AVG(salary) AS '平均薪资' FROM employee GROUP BY department;
query("""
      SELECT department, AVG(salary) AS '平均薪资'
      FROM employee
      GROUP BY department
      """)
# 人事部 | 11500.0
# 市场部 | 9833.333333333334
# 技术部 | 20000.0

# 原始数据（10行）：
# 技术部: 15000, 18000, 22000, 25000
# 市场部: 9000,  12000, 8500
# 人事部: 11000, 16000, 7500

# GROUP BY department 之后（3组）：
# 技术部 → AVG = (15000+18000+22000+25000)/4 = 20000
# 市场部 → AVG = (9000+12000+8500)/3 = 9833
# 人事部 → AVG = (11000+16000+7500)/3 = 11500

# GROUP BY 的铁律
# SELECT 中出现的列，要么在 GROUP BY 中, 要么被聚合函数包裹。否则必报错。
# -- 正确: department 在 GROUP BY 里，salary 被聚合
# SELECT department, AVG(salary) FROM employee GROUP BY department;
query("""
      SELECT department, AVG(salary)
      FROM employee
      GROUP BY department
      """)

# -- 错误: name 既不在 GROUP BY 也不在聚合函数里
query("""
      SELECT department, name, AVG(salary)
      FROM employee
      GROUP BY department
      """)

# -- 数据库不知道你的 name 该取组内的哪一个值，直接报错

# 多列分组
# -- 按部门和性别分组
# SELECT department, gender, COUNT(*) AS '人数', AVG(salary) AS '平均薪资' FROM employee GROUP BY department, gender ORDER BY department, gender;
query("""
      SELECT department, gender, COUNT(*) AS 人数, AVG(salary) AS '平均薪资'
      FROM employee
      GROUP BY department, gender
      ORDER BY department, gender
      """)

# GROUP BY 常用组合
# -- 每个部门的: 人数、平均薪资、最高薪资、最低薪资、总薪资
# SELECT
#     department AS '部门', 
#     COUNT(*) AS '人数',
#     ROUND(AVG(salary), 2) AS '平均薪资',
#     MAX(salary) AS '最高薪资',
#     MIN(salary) AS '最低薪资',
#     SUM(salary) AS '总薪资'
# FROM employee
# GROUP BY department
# ORDER BY '平均薪资' DESC;
query("""
      SELECT
          department AS '部门',
          COUNT(*) AS '人数',
          ROUND(AVG(salary), 2) AS '平均薪资',    
          MAX(salary) AS '最高薪资',
          MIN(salary) AS '最低薪资',
          SUM(salary) AS '总薪资'
      FROM employee
      GROUP BY department
      ORDER BY '平均薪资' DESC
      """)

# HAVING -- 分组后再过滤
# WHERE 过滤行 (在分组前) , HAVING 过滤组 (在分组后) 。这是面试必考。
# -- 查出平均薪资大于 12000 的部门。
# SELECT department, AVG(salary) AS '平均薪资'
# FROM employee
# GROUP BY department
# HAVING AVG(salary) > 12000;
query("""
      SELECT department, AVG(salary) AS '平均薪资'
      FROM employee
      GROUP BY department
      HAVING AVG(salary) > 12000
      """)
# -- 结果: 
# -- 技术部 | 20000.0
# -- 人事部 | 11500.0  (嗯，11500 不大于 12000，所以实际上不会显示)

# 注意: AVG(salary) > 12000 不能放在 WHERE 里！
# -- 错误示范:
# SELECT department, AVG(salary)
# FROM employee
# WHERE AVG(salary) > 12000     -- 报错！WHERE 中不能用聚合函数
# GROUP BY department

# -- 正确:
# SELECT department, AVG(salary)
# FROM employee
# GROUP BY department
# HAVING AVG(salary) > 12000;
query("""
      SELECT department, AVG(salary)
      FROM employee
      GROUP BY department
      HAVING AVG(salary) > 12000
      """)

# WHERE vs HAVING 对比
# | | WHERE | HAVING |
# |------|-------|--------|
# | 执行时机 | 分组**前**，对原始行过滤 | 分组**后**，对聚合结果过滤 |
# | 能用的条件 | 原始列条件（age > 25） | 聚合条件（AVG(age) > 25） |
# | 能否用聚合函数 | ❌ | ✅ |
# | 能否单独使用（不跟 GROUP BY） | ✅ | ✅（但很少这样用） |

# -- WHERE 和 HAVING 可以同时出现
# -- 先过滤行 (只保留技术部和市场部) , 再分组, 再过滤组 (只保留平均薪资>12000的组)
# SELECT department, AVG(salary) AS '平均薪资'
# FROM employee
# WHERE department IN ('技术部', '市场部')
# GROUP BY department
# HAVING AVG(salary) > 12000;
# -- 结果: 技术部 | 20000.0
query("""
      SELECT department, AVG(salary) AS '平均薪资'
      FROM employee
      WHERE department IN ('技术部', '市场部')
      GROUP BY department
      HAVING AVG(salary) > 12000
      """)

# SQL 子句的完整书写顺序和执行顺序
# 书写顺序 (必须按这个写, 否则语法报错)
# SELECT    <- 第5步
# FROM      <- 第1步
# WHERE     <- 第2步
# GROUP BY  <- 第3步
# HAVING    <- 第4步
# ORDER BY  <- 第6步
# LIMIT     <- 第7步

# 1. FROM          → 确定哪张表
# 2. WHERE         → 过滤行（原始数据）
# 3. GROUP BY      → 分组
# 4. HAVING        → 过滤组（聚合结果）
# 5. SELECT        → 选列、计算、别名
# 6. ORDER BY      → 排序（所以可以用 SELECT 中的别名！）
# 7. LIMIT         → 截断

# 为什么 WHERE 不能用 SELECT 的别名？
# -- 报错: 
# SELECT salary * 12 AS '年薪' FROM employee WHERE '年薪' > 200000;
# -- 因为 WHERE (第2步) 在 (第5步) 之前执行, 
# -- "年薪"这个别名还不存在!
# -- 必须这样写:
# SELECT salary * 12 AS '年薪' FROM employee WHERE salary * 12 > 200000;
query("""
      SELECT salary * 12 AS '年薪'
      FROM employee
      WHERE salary * 12 > 200000
      """)

# 题1: COUNT
# 公司有多少名员工?
query("""
      SELECT COUNT(*)
      FROM employee
      """)

# 题2: SUM
# 公司的月工资总额是多少? 给结果起个别名"月工资总额"。
query("""
      SELECT SUM(salary) AS '月工资总额'
      FROM employee
      """)

# 题3: AVG + WHERE
# 技术部员工的平均薪资是多少?
query("""
      SELECT AVG(salary)
      FROM employee
      WHERE department IN ('技术部')
      """)

# 题4: MAX + MIN
# 最高薪资和最低薪资相差多少? (提示: MAX - MIN, 给结果起别名"薪资差")
query("""
      SELECT (MAX(salary) - MIN (salary)) AS '薪资差'
      FROM employee
      """)

# 题5: GROUP BY + COUNT
# 每个部门各有多少人? 显示部门名称和人数。
query("""
      SELECT department, COUNT(*) AS '人数'
      FROM employee
      GROUP BY department
      """)

# 题6: GROUP BY + AVG
# 每个部门的平均薪资是多少? 按平均薪资从高到低排列。
query("""
      SELECT department, AVG(salary)
      FROM employee
      GROUP BY department
      ORDER BY salary DESC
      """)

# 题7: GROUP BY 多列
# 按部门和性别分组, 统计每组的人数和平均薪资。
query("""
      SELECT department, COUNT(*), AVG(salary)
      FROM employee
      GROUP BY department, gender
      """)

# 题8: HAVING
# 找出平均薪资超过 12000 的部门, 显示部门名称和平均薪资。
query("""
      SELECT department,
        AVG(salary)
      FROM employee
      GROUP BY department
      HAVING AVG(salary) > 12000
      """)

# 题9: WHERE + GROUP BY + HAVING 组合
# 先排除 id = 10 的员工 (假设他刚入职不算), 然后找出人数不少于3人的部门，显示部门名称和人数。
query("""
      SELECT department, COUNT(*) AS '人数'
      FROM employee
      WHERE id != 10
      GROUP BY department
      HAVING COUNT(*) >= 3
      """)

# 题10: 综合
# 统计每个部门中薪资大于 10000 的员工人数，只显示人数超过 1 的部门。显示部门名称和人数，按人数降序排列。
query("""
      SELECT department, COUNT(*) AS 人数
      FROM employee
      WHERE salary > 10000
      GROUP BY department
      HAVING COUNT(*) > 1
      ORDER BY 人数 DESC;
      """)

