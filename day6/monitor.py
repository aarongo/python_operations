# -*- coding: utf-8 -*-

__author__ = 'yulong'
import MySQLdb
import paramiko
import time

node_group = []
node_host_list = []
host_user = []
chose_ip = None
# 数据库连接
conn = MySQLdb.connect(host="localhost", user="root", passwd="aarongo", db="python_linux", charset="utf8")
cursor = conn.cursor()


class Login(object):
    def login(self):
        user = raw_input("输入用户名：")
        # 查询运维人员账户
        sqltext = "select name from t_user WHERE name = '%s'" % user
        # 运行查询
        n = cursor.execute(sqltext)
        # 判断用户存在否
        if n == 0:
            print "用户不存在！！！"
        else:
            print "你能操作的节点组"
            # 查询运维用户存在的运维组，以及运维组存在的node节点组，
            sql_nodegroup = """select n.id,n.node_group_name from t_user u join t_user_group g on u.user_group = g.id
               join t_node_group n on g.node_group = n.id where u.name = '%s'""" % user
            # 运行查询
            n = cursor.execute(sql_nodegroup)
            # 将查询结果复制给data
            data = cursor.fetchall()
            # 遍历结果将结果添加到你node_group列表中
            for i in data:
                node_group.append(i, )
            # 遍历节点组列表（索引与值）
            for index, v in enumerate(node_group):
                print index, v
            chose = raw_input("你要操作的节点组：")
            # 判断用户输入在node_group列表中选取
            if chose.isdigit():
                chose = int(chose)
                print "--------组内主机--------"
                # 查询数据库列表中的主机，因为数据库查出来的是元组
                sql_host = """ select * from t_host t WHERE t.node_id='%s'""" % node_group[0][0]
                # 运行查询
                n = cursor.execute(sql_host)
                data = cursor.fetchall()
                # 将查询到的结果添加到主机列表中
                for i in data:
                    node_host_list.append(i, )
                # 遍历主机列表
                for index, k in enumerate(node_host_list):
                    print index, k
                chose_host = raw_input("你要操作的主机：")
                if chose_host.isdigit():
                    chose_host = int(chose_host)
                    # 查询主机用户名
                    sql_user = """select u_name from host_user t WHERE t.host_id='%s' """ % node_host_list[0][0]
                    # 运行查询
                    n = cursor.execute(sql_user)
                    data = cursor.fetchall()
                    # 获取主机IP地址
                    sql_ip = """ select ip from t_host WHERE id = '%s'""" % node_host_list[0][0]
                    ip = cursor.execute(sql_ip)
                    # 将ip地址存放到以选择变量中
                    for row in cursor.fetchall():
                        for r in row:
                            chose_ip = r
                            # 将以选择Ip  地址的用户存放到列表中
                    for i in data:
                        host_user.append(i, )
                    for index, u in enumerate(host_user):
                        print index, u
                    chose_user = raw_input("选择用户：")
                    if chose_user.isdigit():
                        # 获取该用户名的密码
                        sql_password = """ select password from host_user WHERE u_name = '%s'""" % host_user[0][0]
                        n = cursor.execute(sql_password)
                        # 将获取到的密码存放到变量中
                        for row in cursor.fetchall():
                            for r in row:
                                passwd = r
                        # 链接服务器执行命令
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(chose_ip, 22, host_user[0][0], passwd)
                        command = raw_input("输入你的命令：")
                        stdin, stdout, stderr = ssh.exec_command(command)
                        # 记录信息到数据库
                        chan = [user, host_user[0][0], command]
                        sqli = """insert into yw_t_logs (yw_user,time,log,host_user) values('%s','%s','%s','%s')""" % (
                            chan[0], time.strftime("%Y-%m-%d %H:%M:%S"), chan[2], chan[1])
                        cursor.execute(sqli)
                        conn.commit()
                        print stdout.readlines()
                        ssh.close()


run = Login()
run.login()
