# _*_coding:utf-8_*_
import db_util

dbconn = db_util.DBConn()


def query(sql):
    conn = dbconn.cursor()
    rows = conn.execute(sql)
    for row in conn.fetchall():
        for r in row:
            print r,
    return rows


def query1(sql):
    conn = dbconn.cursor()
    rows = conn.execute(sql)
    return rows


if __name__ in "__main__":
    flag = True
    while flag:
        user = raw_input("Please user:")
        sql_user = """select NAME from t_user WHERE name ='%s'""" % user
        if query1(sql_user) != 0:
            sql = """ select n.node_group_name from t_user u
                join t_user_group g
                on u.user_group = g.id
                join t_node_group n
                on g.node_group = n.id
                where u.`name`='%s'""" % user
            query(sql)
            node = raw_input("\n输入你要操作的节点组：")
            sql_node = """select * from t_node t where t.node_group = '%s'""" % node
            query(sql_node)
            flag = False
        else:
            print "不存在"
