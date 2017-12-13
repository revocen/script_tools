import sqlite3
import pyperclip
import time

def generate(target,number):
    result = target + time.strftime('_%Y%m%d_' + str(number).zfill(2), time.localtime()) + '_revocen'
    return result

target = pyperclip.paste()

conn = sqlite3.connect('logger.db')
cur = conn.cursor()

# 创建表
sql_create = 'create table if not exists memory (name char(200), usetime datetime, res char(200),code char(2))'
cur.execute(sql_create)

# 查询是否已存在
sql_select = "select * from memory where name = ? order by usetime desc limit 1"
cursor_select = cur.execute(sql_select, (str(target),))
count_select = cursor_select.fetchall()
s = len(count_select)
print('count_select ->' + str(s))

code = 1
r = ''

if s <= 0:
    # 不存在，从1开始
    print('no row')
    r = generate(target,code)
else:
    print('from row')
    row = count_select[0]
    code = int(row[3]) + 1
    r = generate(target,code)

print('code -> ' + str(code))
print('r ->' + str(r))

sql_insert = "insert into memory (name,usetime,res,code) values(?,CURRENT_TIMESTAMP,?,?)"
cur.execute(sql_insert, (target,r,code))
conn.commit()

print('result ->' + r)
print('done')

pyperclip.copy(r)
conn.close()