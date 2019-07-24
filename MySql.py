import mysql.connector
import json
import datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="noxus",
    auth_plugin='mysql_native_password'
)
myCursor = mydb.cursor()

myCursor.execute("SELECT * FROM sys_tm_user")
# myResult = myCursor.fetchall()  # fetchall() 获取所有记录
myResult = myCursor.fetchone()
json_str = json.dumps(myResult, cls=DateEncoder)
print(json_str)
