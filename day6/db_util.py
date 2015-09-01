# _*_coding:utf-8_*_
import MySQLdb


class DBConn:
    conn = None

    # 建立和数据库系统的连接
    def connect(self):
        self.conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="aarongo", db="python_linux")

    # 获取操作游标
    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()


    # 提交
    def commit(self):
        return self.conn.commit()

    # 关闭连接
    def close(self):
        return self.conn.close()
