# _*_coding:utf-8_*_
from proson import Proson


class RoleOne(Proson):
    def __init__(self, name, ages, sex, job, nationality, school, company, salary):
        super(RoleOne, self).__init__(name, ages, sex, job, nationality)
        self.school = school
        self.company = company
        self.salary = salary

    def info(self):
        Proson.info(self)
        print '''
                school: %s
        ''' % (self.school)


class RoleTwo(Proson):
    def __init__(self, name, ages, sex, job, nationality, company, salary):
        super(RoleTwo, self).__init__(name, ages, sex, job, nationality)
        self.company = company
        self.salary = salary

    def info(self):
        Proson.info(self)
        print '''
                 company :%s
                 salary  :%s''' % (self.company, self.salary)


class RoleThree(Proson):
    def __init__(self, name, ages, sex, job, nationality, school, company, post, skill, salary):
        super(RoleThree, self).__init__(name, ages, sex, job, nationality)
        self.school = school
        self.company = company
        self.post = post
        self.skill = skill
        self.salary = salary

    def info(self):
        Proson.info(self)
        print  '''
                 school : %s
                company : %s
                   psot : %s
                  skill : %s
                  salary: %s
        ''' % (self.school, self.company, self.post, self.skill, self.salary)


class Chose(object):
    def chose(self):
        while True:
            try:
                role_list = ['John Berry', "Liz", "Peter"]
                for index, role in enumerate(role_list):
                    print index, role
                chose = raw_input("选择你的游戏角色").strip()
                if chose.isdigit():
                    chose = int(chose)

                    if role_list[chose] == "Liz":
                        people1 = RoleOne("Liz", 24, "女", " ", "美国人", "北京城市学院", " ", " ")
                        people1.info()
                        break
                    elif role_list[chose] == "John Berry":
                        people1 = RoleThree("John Berry", 27, "男", "运维工程师", "美国人", "OldBoy", "google", "首席运维工程师",
                                            "python",
                                            "1000000")
                        people1.info()
                        break
                    elif role_list[chose] == "Peter":
                        people1 = RoleTwo("Peter", 28, "男", "Java工程师", "英国人", "腾讯", 10000)
                        people1.info()
                        break
                    else:
                        print "请选择角色"
            except IndexError, err:
                print err


run = Chose()
run.chose()
