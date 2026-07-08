# SQL Day 4: 多表 JOIN 进阶

# 多表连接和自连接，以及 UNION

# 多表 JOIN (3张表)
# 语法和两表 JOIN 一样，继续用 JOIN ... ON ... 往后连。
# 假设在之前的 sql_practice.py 里再加一张 salary_history 表 (每个员工的调薪记录):

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

# 建立一张员工的调薪记录
cur.execute("""
    CREATE TABLE salary_history (
        id INTEGER PRIMARY KEY,
        emp_id INTEGER,
        old_salary REAL,
        new_salary REAL,
        change_date TEXT
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

# 插入市场部数据
departments = [
    (1, '技术部', 5, '钱七'),
    (2, '市场部', 3, '吴十'),
    (3, '人事部', 2, '周九'),
    (4, '财务部', 4, '郑十一')
]

cur.executemany("INSERT INTO department VALUES (?, ?, ?, ?)", departments)
conn.commit()

# 插入员工调薪记录的数据
histories = [
    (1, 1, 12000, 15000, '2021-06-01'),
    (2, 1, 15000, 16500, '2022-06-01'),
    (3, 2, 16000, 18000, '2021-01-15'),
    (4, 5, 20000, 22000, '2020-03-01'),
]

cur.executemany("INSERT INTO salary_history VALUES (?, ?, ?, ?, ?)", histories)
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

query("SELECT * FROM employee")

query("SELECT * FROM department")

query("SELECT * FROM salary_history")

# 三表连接查询: 员工姓名、部门楼层、调薪记录

# SELECT e.name, d.floor, sh.old_salary, sh.new_salary, sh.change_date
# FROM employee e
# JOIN department d ON e.department = d.dept_name
# JOIN salary_history sh ON e.id = sh.emp_id
# ORDER BY e.name, sh.change_date;
query("""
      SELECT e.name, d.floor, sh.old_salary, sh.new_salary, sh.change_date
      FROM employee e
      JOIN department d ON e.department = d.dept_name
      JOIN salary_history sh ON e.id = sh.emp_id
      ORDER BY e.name, sh.change_date
      """)
# 关键: 连接条件写清楚，列名前加表别名避免混淆。

# 自连接 (Self JOIN)
# 一张表自己连接自己，常用于找关联数据，比如员工和其经理。
# 给 employee 表加一个 manager_id 字段 (经理的员工 id), 经理本身也是员工，然后自连接找出每个员工和他的经理。
# 在练习中可以模拟，但因为我们现有表没有 manage_id, 我们用另一种典型场景: 找出同一部门薪资相同的员工 (实际意义不大，只为演示自连接)。
# -- 找出在同一部门且薪资相同的不同员工
# SELECT e1.name AS '员工1', e2.name AS '员工2', e1.department, e1.salary
# FROM employee e1
# JOIN employee e2 ON e1.department = e2.department
#                 AND e1.salary = e2.salary
#                 AND e1.id < e2.id;    -- 避免匹配自己和重复对
query("""
      SELECT e1.name AS '员工1', e2.name AS '员工2', e1.department, e1.salary
      FROM employee e1
      JOIN employee e2 ON e1.department = e2.department
                       AND e1.salary = e2.salary
                       AND e1.id < e2.id
      """)

# UNION / UNION ALL -- 上下拼接查询结果
# UNION 把两个 SELECT 的结果上下合并 (要求列数相同，列类型兼容)。
# UNION ALL 保留重复行，UNION 会自动去重
# -- 列出所有员工和部门经理的姓名 (假设经理也存在于员工表)
# SELECT name, '员工' AS role 
# FROM employee
# UNION
# SELECT manager, '经理' AS role 
# FROM department;
query("""
      SELECT name, '员工' AS role
      FROM employee
      UNION
      SELECT manager, '经理' AS role
      FROM department;
      """)

# 子查询 (Subquery)
# 查询中嵌套查询，括号内的先执行。
# WHERE 子查询 (最常用)
# -- 高于平均薪资的员工
# SELECT name, salary
# FROM employee
# WHERE salary > (SELECT AVG(salary) FROM employee);
query("""
      SELECT name, salary
      FROM employee
      WHERE salary > (
        SELECT AVG(salary) 
        FROM employee
      )
      """)

# 返回单值用 >、= 等比较符; 返回多值用 IN。
# -- 部门楼层 <= 3 的员工 (使用 IN)
# SELECT name
# FROM employee
# WHERE department IN (
#       SELECT dept_name FROM department WHERE floor <= 3
# );
query("""
      SELECT name
      FROM employee
      WHERE department IN (
        SELECT dept_name 
        FROM department 
        WHERE floor <= 3
      )
      """)

# FROM 子查询 (临时表，必须加别名)
# SELECT dept_avg.department, dept_avg.avg_sal
# FROM (
#   SELECT department, AVG(salary) AS 'avg_sal'
#   FROM employee
#   GROUP BY department
# ) AS dept_avg;
query("""
      SELECT dept_avg.department, dept_avg.avg_sal
      FROM (
        SELECT department, AVG(salary) AS 'avg_sal'
        FROM employee
        GROUP BY department
      ) AS dept_avg
      """)

# SELECT 子查询 (标量子查询，只能返回一行一列)
# SELECT name, salary,
#        salary - (
#                   SELECT AVG(salary)
#                   FROM employee
#                  ) AS diff
# FROM employee;
query("""
      SELECT name, salary,
            salary - (
                    SELECT AVG(salary)
                    FROM employee
                    ) AS diff
      FROM employee
      """)

# EXISTS vs IN
# EXISTS 检查子查询是否有行返回，有则真。通常比 IN 快。
# -- 有员工的部门 (EXISTS)
# SELECT dept_name
# FROM department d
# WHERE EXISTS (
#   SELECT 1 
#   FROM employee e 
#   WHERE e.department = d.dept_name
# );
query("""
      SELECT dept_name
      FROM department d
      WHERE EXISTS (
        SELECT 1
        FROM employee e
        WHERE e.department = d.dept_name
      );
      """)

# -- 无员工的部门 (NOT EXISTS, 比 NOT IN 安全)
# SELECT dept_name
# FROM department d
# WHERE NOT EXISTS (
#   SELECT 1 
#   FROM employee e 
#   WHERE e.department = d.dept_name
# )

query("""
      SELECT dept_name
      FROM department d
      WHERE NOT EXISTS (
        SELECT 1 
        FROM employee e
        WHERE e.department = d.dept_name
      );
      """)

# UNION / UNION ALL - 上下拼接
# UNION 去重，UNION ALL 保留重复
# 列数、类型必须一致
# -- 列出薪资最高和年龄最小的员工 (UNION ALL)
# SELECT name, salary AS 'val', '最高薪' AS 'type'
# FROM employee 
# WHERE salary = (
#   SELECT MAX(salary)
#   FROM employee
#   )
# UNION ALL
# SELECT name, age, '最小龄'
# FROM employee
# WHERE age = (
#   SELECT MIN(age)
#   FROM employee
#   )
query("""
      SELECT name, salary AS 'val', '最高薪' AS 'type'
      FROM employee 
      WHERE salary = (
        SELECT MAX(salary)
        FROM employee)
      UNION ALL
      SELECT name, age, '最小龄'
      FROM employee 
      WHERE age = (
        SELECT MIN(age)
        FROM employee
      );
      """)

# 窗口函数 (重点)
# 不压缩行数，在每一行上做聚合/排序计算。
# 函数名() OVER (PARTITION BY 分组列 ORDER BY 排序列)

# ROW_NUMBER() - 顺序编号 (不并列)
# SELECT name, salary,
#       ROW_NUMBER() OVER (ORDER BY salary DESC) AS 'rn'
# FROM employee;
query("""
      SELECT name, salary,
            ROW_NUMBER() OVER (ORDER BY salary DESC) AS 'rn'
      FROM employee;
      """)

# RANK() - 有并列排名，跳号
# SELECT name, department, salary,
#       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS 'rank'
# FROM employee;
query("""
      SELECT name, department, salary,
            RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS 'rank'
      FROM employee;
      """)
# | 函数 | 特点 |
# |------|------|
# | ROW_NUMBER | 1,2,3,4... 不重复 |
# | RANK | 1,1,3,4... 并列跳号 |
# | DENSE_RANK | 1,1,2,3... 并列不跳号 |

# 练习题
# 题1: 
# 年龄 > 公司平均年龄的员工
# SELECT name, age 
# FROM employee
# WHERE age > (
#   SELECT AVG(age)
#   FROM employee
# );
query("""
      SELECT name, age
      FROM employee
      WHERE age > (
        SELECT AVG(age)
        FROM employee
      );
      """)

# 题2:
# 位于4楼及以上部门的员工
# SELECT name 
# FROM employee
# WHERE department IN (
#   SELECT dept_name
#   FROM department
#   WHERE floor >= 4
# );
query("""
      SELECT name
      FROM employee
      WHERE department IN (
        SELECT dept_name 
        FROM department
        WHERE floor >= 4
      );
      """)

# 题3:
# 平均薪资 > 12000 的部门的员工人数
# SELECT department, COUNT(*) AS 'cnt'
# FROM employee
# WHERE department IN (
#   SELECT department 
#   FROM employee
#   GROUP BY department
#   HAVING AVG(salary) > 12000
# )
# GROUP BY department;
query("""
      SELECT department, COUNT(*) AS 'cnt'
      FROM employee
      WHERE department IN (
        SELECT department
        FROM employee
        GROUP BY department 
        HAVING AVG(salary) > 12000
      );
      """)

# 题4:
# EXISTS: 有员工薪资 > 20000 的部门
# SELECT * 
# FROM department d
# WHERE EXISTS (
#   SELECT 1 
#   FROM employee e
#   WHERE e.department = d.dept_name AND e.salary > 20000
# );
query("""
      SELECT * 
      FROM department d
      WHERE EXISTS (
        SELECT 1
        FROM employee e
        WHERE e.department = d.dept_name AND e.salary > 20000
      );
      """)

# 题5: 
# UNION ALL: 展示最高薪和最小龄
# SELECT name, salary, '最高薪' AS 'type'
# FROM employee 
# WHERE salary = (
#   SELECT MAX(salary) 
#   FROM employee
# )
# UNION ALL
# SELECT name, age, '最小龄'
# FROM employee
# WHERE age = (
#   SELECT MIN(age)
#   FROM employee
# );
query("""
      SELECT name, salary, '最高薪' AS type
      FROM employee
      WHERE salary = (
        SELECT MAX(salary)
        FROM employee
      )
      UNION ALL
      SELECT name, age, '最小龄'
      FROM employee
      WHERE age = (
        SELECT MIN(age)
        FROM employee
      );
      """)

# 题6: 
# 窗口函数: 每个部门内薪资排名
# SELECT name, department, salary,
#       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS 'dept_rank'
# FROM employee;
query("""
      SELECT name, department, salary,
            RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS 'dept_rank'
      FROM employee;
      """)