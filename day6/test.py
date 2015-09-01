import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="aarongo", db="python_linux",
                       charset="utf8")
cursor = conn.cursor()



n = cursor.execute(""" select n.id,n.node_group_name from t_user u
                                    join t_user_group g
                                    on u.user_group = g.id
                                    join t_node_group n
                                    on g.node_group = n.id
                                    where u.`name`='user2'""")
for row in cursor.fetchall():
    for r in row:
        print r
