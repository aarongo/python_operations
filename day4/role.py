# _*_coding:utf-8_*_
from proson import Proson


class RoleOne(Proson):
    def __init__(self, name, ages, sex, job, nationality, school, company, salary):
        super(RoleOne, self).__init__(name, ages, sex, job, nationality)
        self.school = school
        self.company = company
        self.salary = salary

    def info(self):
        print '''               ----Proson_list----
                    姓名: %s
                    年龄: %s
                    性别: %s
                    工作: %s
                    国籍:%s
                    学校：%s
                    公司：%s
                    工资：%s
        ''' % (self.name, self.ages, self.sex, self.job, self.nationality, self.school, self.company, self.salary)


class RoleTwo(Proson):
    def __init__(self, name, ages, sex, job, nationality, company, salary):
        super(RoleTwo, self).__init__(name, ages, sex, job, nationality)
        self.company = company
        self.salary = salary

    def info(self):
        print '''               ----Proson_list----
                    姓名: %s
                    年龄: %s
                    性别: %s
                    工作: %s
                    国籍:%s
                    公司：%s
                    工资：%s
        ''' % (self.name, self.ages, self.sex, self.job, self.nationality, self.company, self.salary)


class RoleThree(Proson):
    def __init__(self, name, ages, sex, job, nationality, school, company, post, skill, salary):
        super(RoleThree, self).__init__(name, ages, sex, job, nationality)
        self.school = school
        self.company = company
        self.post = post
        self.skill = skill
        self.salary = salary

    def info(self):
        print '''               ----Proson_list----
                    姓名: %s  年龄 : %s
                    性别: %s  工作 : %s
                    国籍:%s   学校 : %s
                    公司:%s   职位 : %s
                    技能:%s   工资 :%s
        ''' % (
            self.name, self.ages, self.sex, self.job, self.nationality, self.school, self.company, self.post,
            self.skill,
            self.salary)

    def stroy(self):
        people1 = RoleThree("John Berry", 27, "男", "运维工程师", "美国人", "OldBoy", "google", "首席运维工程师",
                            "python",
                            "1000000")
        people2 = RoleOne("Liz", 24, "女", " ", "美国人", "北京城市学院", " ", " ")
        people3 = RoleTwo("Peter", 28, "男", "Java工程师", "英国人", "腾讯", 10000)
        print "-------------------角色故事------------------"
        print '''
            \033[31m %s \033[0m and \033[31m %s \033[0m 是高中同学时的恋人，
            后来\033[31m %s \033[0m考上了\033[31m %s \033[0m，\033[31m %s \033[0m没有，为了跟女朋友在一起，他来到了北京打工（一家网吧当网管）
            挣钱为\033[31m %s \033[0m交学费，后来\033[31m %s \033[0ms毕业后工作了，遇到了\033[31m %s \033[0m的高富帅\033[31m %s \033[0m,然后两人就苟且在了一起，
            \033[31m %s \033[0m发现后非常伤心，发誓要把\033[31m %s \033[0m夺回来,然后他发粪学习，增加自身能力，参加\033[31m %s \033[0m 学习\033[31m %s \033[0m，
            若干年后，当上了\033[31m %s \033[0m \033[31m %s \033[0m月薪\033[31m %s \033[0m，
            北京买了车和房，偶然又见到了\033[31m %s \033[0m,此时她已被高富\033[31m %s \033[0m甩了,\033[31m %s \033[0m提出再回到\033[31m %s \033[0m身边时，\033[31m %s \033[0m优雅的说\033[31m滚犊子 \033[0m
            ''' % (people2.name, people1.name, people2.name, people2.school, people1.name, people2.name, people2.name,
                   people3.company, people3.name, people1.name, people2.name,
                   people1.school, people1.skill, people1.company, people1.post, people1.salary, people2.name,
                   people3.name, people2.name, people1.name, people1.name)


class Chose(object):
    def chose(self):
        while True:
            try:
                role_list = ['John Berry', "Liz", "Peter"]
                for index, role in enumerate(role_list):
                    print index, role
                people1 = RoleOne("Liz", 24, "女", " ", "美国人", "北京城市学院", " ", " ")
                people2 = RoleThree("John Berry", 27, "男", "运维工程师", "美国人", "OldBoy", "google", "首席运维工程师",
                                    "python",
                                    "1000000")
                people3 = RoleTwo("Peter", 28, "男", "Java工程师", "英国人", "腾讯", 10000)
                people2.stroy()
                chose = raw_input("选择你的游戏角色").strip()
                if chose.isdigit():
                    chose = int(chose)

                    if role_list[chose] == "Liz":
                        people1 = RoleOne("Liz", 24, "女", " ", "美国人", "北京城市学院", " ", " ")
                        people1.info()
                        print "--------Welcome Login Game--------"
                        break
                    elif role_list[chose] == "John Berry":
                        people1 = RoleThree("John Berry", 27, "男", "运维工程师", "美国人", "OldBoy", "google", "首席运维工程师",
                                            "python",
                                            "1000000")
                        people1.info()
                        print "--------Welcome Login Game--------"
                        break
                    elif role_list[chose] == "Peter":
                        people1 = RoleTwo("Peter", 28, "男", "Java工程师", "英国人", "腾讯", 10000)
                        people1.info()
                        print "--------Welcome Login Game--------"
                        break
                    else:
                        print "请选择角色"
            except IndexError, err:
                print err
run = Chose()
run.chose()
