# 旧的python版本必须安装PySQLite才能使用SQLite数据库
# python数据所使用的API为python DB API

# SQLite是一个小型的数据库引擎 ，它不需要独立的服务器运行，可以直接使用本地文件
# lite--精简版
# 要使用python的数据库首先需要导入sqlite3模块




#以下面一行的格式为例
#~01001~^~0100~^~Butter, salted~^~BUTTER,WITH SALT~^~~^~~^~Y~^~~^0^~~^6.38^4.27^8.79^3.87
#字段之间用脱字符分离
#数字字段直接用数字，而文本字段用~ ~包括
#1.要分离字段需要line.split('^')
#2.如果一个字段以~打头，你就知道它是一个字符串，因为可使用field.strip('~')来获取其内容
#3.对于数字字段，使用float(field)就能获取其内容

import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)

conn = sqlite3.connect('food.db')  # 要使用底层的数据库系统，必须先连接到它，并返回一个连接对象，如果文件不存在，将自动创建
# 从连接获得游标
curs = conn.cursor()  # 游标可以用来执行SQL查询，如果修改了数据，务必提交所做的修改，这样才会将其保存在文件中
curs.execute('''
CREATE TABLE food(

id TEXT PRIMARY KEY,
desc  TEXT,
water  FLOAT,
kcal   FLOAT,
protein  FLOAT,
fat  FLOAT,
ash  FLOAT,
carbs  FLOAT,
fiber  FLOAT,
sugar  FLOAT
) 
''')

query='INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count=10
for line in open('ABBREV.txt'):
    fields=line.split('^')
    vals=[convert(f) for f in fields[:field_count]]
    curs.execute(query,vals)#来执行一条SQL insert语句
conn.commit()  # 提交
conn.close()  # 关闭连接
