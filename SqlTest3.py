# SQL Day3: JOIN (多表连接)
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

# 建立一张部门表
cur.execute("""
        CREATE TABLE department (
            dept_id INTEGER PRIMARY KEY,
            dept_name TEXT,
            floor INTEGER,
            manager TEXT
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

departments = [
    (1, '技术部', 5, '钱七'),
    (2, '市场部', 3, '吴十'),
    (3, '人事部', 2, '周九'),
    (4, '财务部', 4, '郑十一')
]

cur.executemany("INSERT INTO department VALUES (?, ?, ?, ?)", departments)
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

query("""
      SELECT *
      FROM employee
      """)

query("""
      SELECT * 
      FROM department
      """)

# 现在你有两张表:
# employee (员工表) : id, name, gender, age, salary, department, hire_date
# department (部门表) : dept_id, dept_name, floor, manager
# employee.department 对应 department.dept_name (用部门名关联) 。
# 注意: department 表中有 "财务部", 但employee表中没有财务部的员工。employee 表中有 "技术部"、"市场部"、"人事部"的员工。这个设计就是为了演示各种 JOIN 的区别。

# 1.为什么需要 JOIN
# 实际数据都是分散在多张表里的。比如
# 员工表存在员工信息
# 部门表存部门信息
# 薪资表存薪资记录
# JOIN的作用: 把多张表的数据按某个条件拼成一张大表，方便查阅

# 2.INNER JOIN (内连接) —— 取交集
# 只返回两张表中匹配上的行。匹配不上的两边都丢弃。
# 语法
# SELECT 列名列表 FROM 表1 INNER JOIN 表2 ON 表1.列 = 表2.列;

# 查员工姓名 + 所在部门 + 部门所在楼层
# SELECT e.name, e.department, d.floor FROM employee e INNER JOIN department d ON e.department = d.dept_name;
query("""
      SELECT e.name, e.department, d.floor
      FROM employee e
      INNER JOIN department d ON e.department = d.dept_name;
      """)

# name   | department | floor
# 张三   | 技术部     | 5
# 李四   | 技术部     | 5
# 王五   | 市场部     | 3
# 赵六   | 市场部     | 3
# 钱七   | 技术部     | 5
# 孙八   | 人事部     | 2
# 周九   | 人事部     | 2
# 吴十   | 市场部     | 3
# 郑十一 | 技术部     | 5
# 冯十二 | 人事部     | 2

# 注意: 财务部 (dept_name='财务部') 没有出现在结果中，因为 employee 表里没有财务部的员工————两边没匹配上，被丢弃了。这就是INNER JOIN。

# 图解 INNER JOIN

# employee 表:                 department 表:
# 技术部 ✓                     技术部 ✓  → 保留
# 市场部 ✓                     市场部 ✓  → 保留
# 人事部 ✓                     人事部 ✓  → 保留
#                              财务部 ✗  → 丢弃（employee侧没有）

# 只取两个圆的交集

# 简化写法
# --JOIN 默认就是 INNER JOIN, 所以 INNER 可以省略
# SELECT e.name, d.floor FROM employee e JOIN department d ON e.department = d.dept_name;
query("""
      SELECT e.name, d.floor 
      FROM employee e
      JOIN department d ON e.department = d.dept_name;
      """)

# 多表 JOIN
# -- 三张表连接 (假设还有一张 salary_history 表)
# SELECT e.name, d.floor, s.amount
# FROM employee e
# JOIN department d ON e.department = d.dept_name
# JOIN salary_history s ON e.id = s.emp_id;

# 3.LEFT JOIN (左连接) -- 保留左表全部
# 左表 (FROM 后面的表) 的所有行都保留，右表匹配不上的填 NULL。
# SELECT e.name, e.department, d.floor FROM employee e LEFT JOIN department d ON e.department = d.dept_name;
query("""
      SELECT e.name, e.department, d.floor
      FROM employee e
      LEFT JOIN department d ON e.department = d.dept_name;
      """)
# name | department | floor
# --------------------------------------------------
# 张三 | 技术部 | 5
# 李四 | 技术部 | 5
# 王五 | 市场部 | 3
# 赵六 | 市场部 | 3
# 钱七 | 技术部 | 5
# 孙八 | 人事部 | 2
# 周九 | 人事部 | 2
# 吴十 | 市场部 | 3
# 郑十一 | 技术部 | 5
# 冯十二 | 人事部 | 2
# 结果和 INNER JOIN 一样 (因为每个 employee 的 department 都在 department 表中有对应) 

# 换个方向就看出区别了:
# -- 右表当主表: 保留 department 的所有行
# SELECT d.dept_name, e.name FROM department d LEFT JOIN employee e ON d.dept_name = e.department;
query("""
      SELECT d.dept_name, e.name
      FROM department d
      LEFT JOIN employee e ON d.dept_name = e.department;
      """)
# dept_name | name
# --------------------------------------------------
# 技术部 | 张三
# 技术部 | 李四
# 技术部 | 郑十一
# 技术部 | 钱七
# 市场部 | 吴十
# 市场部 | 王五
# 市场部 | 赵六
# 人事部 | 冯十二
# 人事部 | 周九
# 人事部 | 孙八
# 财务部 | None     <- 财务部没有员工，所以 name 为 None
# 左表全部保留, 右表匹配不上的填 None

# LEFT JOIN 最常用场景
# -- 找出没有员工的部门 (右表匹配不上的)
# SELECT d.dept_name FROM department d LEFT JOIN employee e ON d.dept_name = e.department WHERE e.id IS NULL;
query("""
      SELECT d.dept_name
      FROM department d
      LEFT JOIN employee e ON d.dept_name = e.department 
      WHERE e.id IS NULL
      """)
# 结果: 财务部

# -- 统计每个部门的员工人数 (包括没有员工的部门)
# SELECT d.dept_name, COUNT(e.id) AS 员工数 FROM department d LEFT JOIN employee e ON d.dept_name = e.department GROUP BY d.dept_name ORDER BY 员工数 DESC;
query("""
      SELECT d.dept_name, COUNT(e.id) AS '员工数'
      FROM department d 
      LEFT JOIN employee e ON d.dept_name = e.department
      GROUP BY d.dept_name
      ORDER BY '员工数' DESC
      """)
# dept_name | 员工数
# --------------------------------------------------
# 财务部 | 0
# 技术部 | 4
# 市场部 | 3
# 人事部 | 3
# 如果用 INNER JOIN, 财务部根本不会出现在结果中

# 4.RIGHT JOIN (右连接) -- 保留右表全部
# 和LEFT JOIN 一样, 只是方向反过来, 右表全部保留
# SELECT d.dept_name, e.name FROM employee e RIGHT JOIN department d ON e.department = d.dept_name
query("""
      SELECT d.dept_name, e.name 
      FROM employee e 
      RIGHT JOIN department d ON e.department = d.dept_name
      """)
# dept_name | name
# --------------------------------------------------
# 技术部 | 张三
# 技术部 | 李四
# 市场部 | 王五
# 市场部 | 赵六
# 技术部 | 钱七
# 人事部 | 孙八
# 人事部 | 周九
# 市场部 | 吴十
# 技术部 | 郑十一
# 人事部 | 冯十二
# 财务部 | None
# 结果和上面 department LEFT JOIN employee 一样.
# 实际上 A RIGHT JOIN B 等价于 B LEFT JOIN A, 所以大多数开发者只用 LEFT JOIN, 不用 RIGHT JOIN,统一思维方向

# 三种 JOIN 对比总结
# | JOIN 类型 |    保留  |  丢弃 |
# |-----------|------|------|
# | INNER JOIN | 两边都匹配的行 | 两边不匹配的都丢弃 |
# | LEFT JOIN | 左表全部 | 右表不匹配的填 NULL |
# | RIGHT JOIN | 右表全部 | 左表不匹配的填 NULL |

# 练习题
# 题1 : INNER JOIN 基础
# 查询每个员工的姓名、部门和所在楼层
query("""
      SELECT e.name, e.department, d.floor
      FROM employee e
      INNER JOIN department d ON e.department = d.dept_name
      """)

# 题2 : LEFT JOIN 基础
# 列出所有部门及每个部门的员工数 (用 LEFT JOIN，确保没有员工的部门也显示)
query("""
      SELECT d.dept_name, COUNT(e.id)
      FROM department d
      LEFT JOIN employee e ON d.dept_name = e.department
      GROUP BY d.dept_name
      """)

# 题3 : 找出没有员工的部门
query("""
      SELECT d.dept_name
      FROM department d
      LEFT JOIN employee e ON d.dept_name = e.department
      WHERE e.id IS NULL
      """)

# 题4 : 找出每个部门薪资最高的员工姓名和薪资
# 提示: 先 JOIN, 再分组，要用子查询或窗口函数。先尝试用子查询做。
# 方法一:
query("""
      SELECT e.name, e.department, MAX(e.salary) AS 'max_salary'
      FROM employee e
      LEFT JOIN department d ON e.department = d.dept_name
      GROUP BY e.department
      """)

# 方法二:
query("""
      SELECT e.name, e.department, e.salary
      FROM employee e
      INNER JOIN (
        SELECT name, department, MAX(salary) AS 'max_salary'
        FROM employee
        GROUP BY department
      ) t ON e.department = t.department AND e.salary = t.max_salary;
      """)

# 题5 : 查询所有男性员工及其所在部门楼层
query("""
      SELECT e.name, e.gender, e.department, d.floor
      FROM employee e
      LEFT JOIN department d ON e.department = d.dept_name
      WHERE e.gender IN ('男');
      """)

# 题6 : 每个楼层有多少员工
query("""
      SELECT d.floor, COUNT(e.id) AS '员工数'
      FROM department d
      LEFT JOIN employee e ON d.dept_name = e.department
      GROUP BY d.floor
      ORDER BY d.floor ASC
      """)