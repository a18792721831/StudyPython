import sqlite3

# 数据库存储实例
# 也就是数据库文件名
linkUrl = 'hello.db'

# 获取连接
conn = sqlite3.connect(linkUrl)
# print(dir(conn))

# 获取操作游标
cur = conn.cursor()
# print(dir(cur))

# 创建表的SQL
# sqlCreate = 'create table user(name text,id number,sex text)'

# 执行
# cur.execute(sqlCreate)

# 创建插入SQL
# sqlInsert = "insert into user values('test1', 001, '男')"

# 执行SQL
# cur.execute(sqlInsert)

# 提交事务
# conn.commit()

# 创建查询SQL
sqlSelect = 'select * from user'

# 执行查询SQL
# data = cur.execute(sqlSelect)

# 获取所有结果
# print(data.fetchall())

# 创建批量插入SQL
# batchInsertSql = 'insert into user values (?,?,?)'

# 创建批量数据
# batchInsertData = [('batch1', 2, '男'), ('batch2', 3, '女'), ('batch3', 4, '人妖')]

# 执行批量的SQL
# data = cur.executemany(batchInsertSql,batchInsertData)

# 提交批量的事物
# conn.commit()

# 执行查询批量结果SQL
# batch_data = cur.execute(sqlSelect)

# 获取所有的结果
# print(batch_data.fetchall())

# 创建更新SQL
# sqlUpdate = "update user set name = 'tst' where id = 001"

# 执行更新SQL
# data = cur.execute(sqlUpdate)

# 提交更新
# conn.commit()

# 执行查询更新结果SQL
# update_data = cur.execute(sqlSelect)

# 获取所有的结果
# print(update_data.fetchall())

# 创建删除SQL
# deleteSql = 'delete from user where id = 1'

# 执行删除SQL
# data = cur.execute(deleteSql)

# 提交删除事物
# conn.commit()

# 执行查询删除结果SQL
delete_data = cur.execute(sqlSelect)

# 获取所有的结果
print(delete_data.fetchall())

# 关闭操作游标
cur.close()

# 关闭连接
conn.close()
