# _*_coding:utf-8_*_
import people


# class Role(people.People):
#     def __init__(self, name, age, sex, job, race, feature, features, speciality, nationality):
#         # people.People.__init__(self, name, age, sex, job, race, feature, features, speciality, nationality)
#         super(Role, self).__init__(name, age, sex, job, race, feature, features, speciality, nationality)
#
#     def test(self):
#         print "\33[;5m 姓名：%s 年龄：%s 性别：%s 职业：%s 人种：%s 特征：%s 功能：%s 角色： %s 国家：%s \33[0m" % (
#             self.name, self.age, self.sex, self.job, self.race, self.feature, self.features, self.speciality,
#             self.nationality)
#
# p1 = Role("tom", 22, "男", "it", "heizhongren", "heipifu", "tiaowu", "kongzhiyuan", "US")
# p2 = Role("张三",33,"男","销售","黄种人","黄皮肤","吹牛逼","调酒师","中国")
# p3 = Role("lisi",44,"男","销售","白种人","白皮肤","吹牛逼","调酒师","中国")
# Role.story()

class Role1(people.Proson):
    def __init__(self, name, age, sex, job,role2, role3):
        super(Role1, self).__init__(name, age, sex)
        self.job = job
        self.role2 = role2
        self.role3 = role3

    def Story(self):
        print """%s 和 %s 是高中同学时的恋人，\n
              后来 %s 考上了北京城市学院，%s 没有，为了跟女朋友在一起， \n
              他来到了北京打工（一家网吧当网管），挣钱为%s交学费，后来%s毕业后工作了， \n
              遇到了公司的高富帅%s,然后两人就苟且在了一起，%s发现后非常伤心，发誓要把%s夺回来\n
              ，然后他发粪学习，增加自身能力，参加自考，学习老男孩PYTHON，若干年后， \n
              当上了某大型互联网公司的%s总监，月薪%s，北京买了车和房， \n
              偶然又见到了%s,此时她已被高富%s甩了，%s提出再回到%s身边时，%s优雅的说。。。""" % (
            self.name, self.role3.name, self.name, self.role3.name, self.name, self.name, self.role2.name,
            self.role3.name,
            self.name, self.role3.job, self.role3.gongneng, self.name, self.role2.name, self.name, self.role3.name,
            self.role3.name)


class Role2(people.Proson):
    def __init__(self, name, age, sex, job, renzhong):
        super(Role2, self).__init__(name, age, sex)
        self.job = job
        self.renzhong = renzhong


class Role3(people.Proson):
    def __init__(self, name, age, sex, job, renzhong, gongneng):
        super(Role3, self).__init__(name, age, sex)
        self.job = job
        self.renzhong = renzhong
        self.gongneng = gongneng


role2 = Role2("Peter", 25, "男", "xiaoshou", "hongzhongren")
role3 = Role3("John Berry", 27, "男", "gognchengshi", "baizhongren", "wan")

role1 = Role1("Liz", 20, "女", "IT", role2, role3)

role1.Story()
