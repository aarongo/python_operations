# _*_coding:utf-8_*_


# 定义人的类
class Proson(object):
    def __init__(self, name, ages, sex, job, nationality):
        self.name = name
        self.ages = ages
        self.sex = sex
        self.job = job
        self.nationality = nationality

    # 定义方法
    def info(self):
        print '''                   ----角色介绍---
                    name: %s
                    age : %s
                    sex : %s
                    job : %s
            nationality :%s
        ''' % (self.name, self.ages, self.sex,self.job,self.nationality)
