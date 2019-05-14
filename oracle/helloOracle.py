import cx_Oracle

# 10.0.250.19:1521/starbass
# tj_20160217

# 用户名
username = 'tj_20160217'
# 密码
password = 'tj_20160217'
# IP
ip = '10.0.250.19'
# 端口
port = '1521'
# 数据库实例名
servername = 'starbass'
# 获取连接
conn = cx_Oracle.connect(username + '/' + password + '@' + ip + ':' + port + '/' + servername)
# 获取操作游标
cursor = conn.cursor()
# 执行SQL
result = cursor.execute('select * from sysconfigen')
# 获取一个结果
one_data = cursor.fetchone()
# 获取所有结果
all_data = cursor.fetchall()
# 获取指定结果
any_data = cursor.fetchmany(4)
# 关闭操作游标
cursor.close()
# 关闭数据库
conn.close()

# print(one_data)
# print(all_data)
# print(any_data)

print(len(all_data))
for i in all_data.__iter__():
    print(i)

# https://cx-oracle.readthedocs.io/en/latest/