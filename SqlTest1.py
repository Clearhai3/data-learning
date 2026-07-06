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

# 测试一下
query("SELECT * FROM employee")

# SELECT 列名1, 列名2, ... FROM 表名;

# --查所有列 (* 是通配符, 代表全部列)
# SELECT * FROM employee;
query("SELECT * FROM employee")

# --查指定列
# SELECT name, salary FROM employee;
query("SELECT name, salary FROM employee")

# --列的顺序可以任意
# SELECT department, name, age FROM employee;
query("SELECT department, name, age FROM employee")

# 列别名AS
# --AS 给列起一个临时名字 (原名不改，只影响本次查询结果的显示)
# SELECT name AS 姓名, salary AS 月薪 FROM employee;
query("SELECT name AS 姓名, salary AS 月薪 FROM employee")

# --AS 可以省略
# SELECT name 姓名, salary 月薪 FROM employee;
query("SELECT name 姓名, salary 月薪 FROM employee")

# 注意: 别名中如果有空格或特殊字符，需要用双引号包裹:
# SELECT name AS "员工 姓名" FROM employee;
query("SELECT name AS '员工 姓名' FROM employee")

# 去重DISTINCT
# --查看公司有哪些部门(重复的只保留一个)
# SELECT DISTINCT department FROM employee;
query("SELECT DISTINCT department FROM employee")

# --结果: 技术部、市场部、人事部
# --DISTINCT 对后面所有列组合去重
# SELECT DISTINCT department, gender FROM employee;
query("SELECT DISTINCT department, gender FROM employee")

# WHERE — 按条件筛选行
# WHERE 在 FROM 之后，对每一行进行过滤。
# 比较运算符
# | 运算符 | 含义 |
# |--------|------|
# | `=` | 等于 |
# | `!=` 或 `<>` | 不等于 |
# | `>` | 大于 |
# | `<` | 小于 |
# | `>=` | 大于等于 |
# | `<=` | 小于等于 |

# --薪资大于15000的员工
# SELECT name, salary FROM employee WHERE salary > 15000;
query("SELECT name, salary FROM employee WHERE salary > 15000")

# --不是技术部的员工
# SELECT name, department FROM employee WHERE department != '技术部';
query("SELECT name, department FROM employee WHERE department != '技术部'")

# --年龄小于等于28的员工
# SELECT name, age FROM employee WHERE age <= 28;
query("SELECT name, age FROM employee WHERE age <= 28")

# 字符串用单引号包裹，且比较时是大小写敏感的(SQLite默认不敏感，但MySQL不敏感，PostgreSQL敏感，养成加单引号的习惯就行)。

# 逻辑运算符 AND/OR/NOT
# --AND: 两个条件同时满足
# SELECT name, age, salary FROM employee WHERE age > 25 AND salary > 10000;
query("SELECT name, age, salary FROM employee WHERE age > 25 AND salary > 10000")

# --OR: 满足其中任意一个
# SELECT name, department FROM employee WHERE department = '技术部' OR department = '人事部';
query("SELECT name, department FROM employee WHERE department = '技术部' OR department = '人事部'")

# --NOT: 取反
# SELECT name, department FROM employee WHERE NOT department = '技术部';
query("SELECT name, department FROM employee WHERE NOT department = '技术部'")

# --组合使用: 括号控制优先级 (和Python 一样，有括号更清晰)
# SELECT name, age, salary, department FROM employee WHERE (department = '技术部' OR department = '市场部') AND salary > 10000;
query("SELECT name, age, salary, department FROM employee WHERE (department = '技术部' OR department = '人事部') AND salary > 10000")

# AND 优先级高于 OR。不确定顺序就加括号，不会出错:
# --这两个不一样!
# --不加括号(AND 先执行):
# WHERE department = '技术部' OR department = '市场部' AND salary > 10000
# --等价于: 技术部的所有人 OR (市场部且薪资>10000的人)
query("SELECT name, department, salary FROM employee WHERE department = '技术部' OR department = '市场部' AND salary > 10000")

# 加括号
# WHERE (department = '技术部' OR department = '市场部') AND salary > 10000
# --技术和市场两个部门中，薪资>10000的人
query("SELECT name, department, salary FROM employee WHERE (department = '技术部' OR department = '市场部') AND salary > 10000")

# IN--在某个集合中
# --等价于多个OR
# SELECT name, department FROM employee WHERE department IN ('技术部', '人事部');
# 等价于: 
# SELECT name, department FROM employee WHERE department = '技术部' OR department = '人事部';
query("SELECT name, department FROM employee WHERE department IN ('人事部', '技术部')")

# NOT IN: 不在集合中
# SELECT name, department FROM employee WHERE department NOT IN ('技术部');
query("SELECT name, department FROM employee WHERE department NOT IN ('技术部')")

# BETWEEN--在某个范围内(包含边界)
# --薪资在10000到20000之间(包含10000和20000)
# SELECT name, salary FROM employee WHERE salary BETWEEN 10000 AND 20000;
query("SELECT name, salary FROM employee WHERE salary BETWEEN 10000 AND 20000")
# 等价于:
# SELECT name, salary FROM employee WHERE salary >= 10000 AND salary <= 20000;

# NOT BETWEEN
# SELECT name, salary FROM employee WHERE salary NOT BETWEEN 10000 AND 20000;
query("SELECT name, salary FROM employee WHERE salary NOT BETWEEN 10000 AND 20000")

# BETWEEN 也可以用于日期和文本:
# --日期范围
# SELECT name, hire_date FROM employee WHERE hire_data BETWEEN '2020-01-01' AND '2022-12-31';
# query("SELECT name, hire_date FROM employee WHERE hire_data BETWEEN '2020-01-01' AND '2022-12-31'")

# LIKE--模糊匹配
# | 通配符 | 含义 |
# |--------|------|
# | `%` | 匹配任意多个字符（包括 0 个） |
# | `_` | 匹配恰好 1 个字符 |

# --名字以"张"开头
# SELECT name FROM employee WHERE name LIKE '张%';
query("SELECT name FROM employee WHERE name LIKE '张%'")
# --张三、张（任何长度）

# --名字以"八"结尾
# SELECT name FROM employee WHERE name LIKE '%八';
query("SELECT name FROM employee WHERE name LIKE '%八'")

# --名字中包含"十"
# SELECT name FROM employee WHERE name LIKE "%十%";
query("SELECT name FROM employee WHERE name LIKE '%十%'")

# --名字恰好三个字，且以"冯"开头
# SELECT name FROM employee WHERE name LIKE '冯__';
query("SELECT name FROM employee WHERE name LIKE '冯__'")

# --NOT LIKE
# SELECT name FROM employee WHERE name NOT LIKE '张%';
query("SELECT name FROM employee WHERE name NOT LIKE '张%'")

# IS NULL / IS NOT NULL -- 判空
# --我们的表中暂时没有NULL值，但语法要记住:
# --查找某列为空的记录
# SELECT * FROM employee WHERE department IS NULL;
query("SELECT * FROM employee WHERE department IS NULL")

# -- 查找某列不为空的记录
# SELECT * FROM employee WHERE department IS NOT NULL;
query("SELECT * FROM employee WHERE department IS NOT NULL")

# -- x 错误写法 (这个不起作用或者结果不对):
# SELECT * FROM employee WHERE department = NULL;
# query("SELECT * FROM employee WHERE department = NULL")

# NULL是一个特殊值，表示"不知道/不存在"。拿任何东西和NULL比较，结果都是NULL（既不是True也不是False）。所以判断NULL必须用IS NULL

# ORDER BY -- 排序
# --按薪资升序 (默认 ASC, 从小到大)
# SELECT name, salary FROM employee ORDER BY salary;
query("SELECT name, salary FROM employee ORDER BY salary")
# SELECT name, salary FROM employee ORDER BY salary ASC;        --等价
query("SELECT name, salary FROM employee ORDER BY salary ASC") #--等价 

# -- 按薪资降序 (DESC, 从大到小)
# SELECT name, salary FROM employee ORDER BY salary DESC;
query("SELECT name, salary FROM employee ORDER BY salary DESC")

# --多列排序: 先按部门升序，同一部门内按薪资降序
# SELECT name, department, salary FROM employee ORDER BY department ASC, salary DESC;
query("SELECT name, department, salary FROM employee ORDER BY department ASC, salary DESC")

# --可以用列别名或列位置(不推荐用位置，可读性差)
# SELECT name, salary * 12 AS 年薪 FROM employee ORDER BY 年薪 DESC;
query("SELECT name, salary * 12 AS '年薪' FROM employee ORDER BY '年薪' DESC")

# ORDER BY 必须是SELECT 语句的最后一条字句(除了LIMIT)
# --正确顺序:
# SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ...;

# LIMIT - 限制返回行数
# --只返回前3行
# SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3;
query("SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3")
# -- 结果：郑十一(25000) > 钱七(22000) > 李四(18000)

# -- LIMIT + OFFSET: 跳过前N行，取M行(分页查询的基础)
# -- LIMIT 数量 OFFSET 跳过数量
# SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3 OFFSET 3;  --跳过前3名，拿第4-6名
query("SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3 OFFSET 3")

# MySQL 中可以用逗号简写(SQLite 也支持):
# SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3, 3;    --跳过3行，取3行(OFFSET 在前，LIMIT在后)
query("SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3, 3")

# SQL书写规范(养成习惯)
# --推荐写法: 关键字大写，每个子句换行
# SELECT name, salary, department
# FROM employee
# WHERE salary > 10000
# AND department = '技术部'
# ORDER BY salary DESC
# LIMIT 5;
query("""
      SELECT name, salary, department 
      FROM employee
      WHERE salary > 10000
      AND department = '技术部'
      ORDER BY salary DESC
      LIMIT 5
      """)

# SQL 不区分大小写（select 和 SELECT 一样），但：
# SQL 关键字建议大写（SELECT、FROM、WHERE）
# 表名、列名建议小写，单词间用下划线
# 字符串值用单引号

# 题 1：查全部
# 查出 employee 表中所有列、所有行。
print("题1：查全部，查出employee表中所有列、所有行")
query("""
      SELECT * 
      FROM employee
      """)

# 题 2：选列
# 只查所有员工的 name（姓名）和 salary（薪资）两列。
print("题2：选列，只查所有员工的 name （姓名）和 salary （薪资）两列。")
query("""
      SELECT name AS '姓名', salary AS '薪资'
      FROM employee  
      """)

# 题 3：去重
# 公司有哪些部门？（列出所有不重复的部门名称）
print("题3：公司有哪些部门？（列出所有不重复的部门名称）")
query("""
      SELECT DISTINCT department
      FROM employee
      """)

# 题 4：条件过滤
# 查出所有薪资大于等于 15000 的员工姓名和薪资。
print("题4：查出所有薪资大于等于15000的员工姓名和薪资。")
query("""
      SELECT name AS '姓名', salary AS '薪资'
      FROM employee
      WHERE salary >= 15000
      """)

# 题 5：多条件 AND
# 查出技术部中薪资大于 15000 的员工姓名、年龄、薪资。
print("题5：查出技术部中薪资大于15000的员工姓名、年龄、薪资。")
query("""
      SELECT name AS '姓名', age AS '年龄', salary AS '薪资'
      FROM employee
      WHERE salary > 15000
      AND department = '技术部'
      """)

# 题 6：IN 操作符
# 查出市场部和人事部的所有员工姓名和部门。
print("题 6：查出市场部和人事部的所有员工姓名和部门。")
query("""
      SELECT name AS '姓名', department AS '部门'
      FROM employee
      WHERE department IN ('市场部', '人事部')
      """)

# 题 7：BETWEEN
# 查出年龄在25到30岁之间(包含边界)的员工姓名和年龄。
print("题 7：查出年龄在25到30岁之间(包含边界)的员工姓名和年龄。")
query("""
      SELECT name AS '姓名', age AS '年龄'
      FROM employee
      WHERE age BETWEEN 25 AND 30
      """)

# 题 8：LIKE 模糊查询
# 查出所有姓"张"或姓"王"的员工姓名。(提示：可以用 OR 组合两个 LIKE)
print("题 8：查出所有姓\"张\"或姓\"王\"的员工姓名。(提示：可以用 OR 组合两个 LIKE)")
query("""
      SELECT name AS '姓名'
      FROM employee
      WHERE name LIKE '张%' OR name LIKE '王%'
      """)

# 题 9：排序 + 限制
# 查出薪资最高的 3 个人的姓名和薪资。
print("题 9：查出薪资最高的 3 个人的姓名和薪资。")
query("""
      SELECT name AS '姓名', salary AS '薪资'
      FROM employee
      ORDER BY salary DESC
      LIMIT 3
      """)

# 题 10：综合
# 查出技术部中年龄小于 35 岁的员工，按薪资从高到低排列，只显示前 2 名。显示姓名、年龄、薪资三列。
print("题 10：查出技术部中年龄小于 35 岁的员工，按薪资从高到低排列，只显示前 2 名。显示姓名、年龄、薪资三列。")
query("""
      SELECT name AS '姓名', age AS '年龄', salary AS '薪资'
      FROM employee
      WHERE age < 35
      AND department = '技术部'
      ORDER BY salary DESC
      LIMIT 2
      """)