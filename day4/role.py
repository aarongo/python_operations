# _*_coding:utf-8_*_
import people


class Role(people.People):
    def __init__(self, name, age, sex, job, race, feature, features, speciality, nationality):
        # people.People.__init__(self, name, age, sex, job, race, feature, features, speciality, nationality)
        super(Role, self).__init__(name, age, sex, job, race, feature, features, speciality, nationality)

    def test(self):
        print "\33[;5m 姓名：%s 年龄：%s 性别：%s 职业：%s 人种：%s 特征：%s 功能：%s 角色： %s 国家：%s \33[0m" % (
            self.name, self.age, self.sex, self.job, self.race, self.feature, self.features, self.speciality,
            self.nationality)


p = Role("tom", 22, "男", "it", "heizhongren", "heipifu", "tiaowu", "kongzhiyuan", "US")
p1 = Role("张三",33,"男","销售","黄种人","黄皮肤","吹牛逼","调酒师","中国")
p.test()
p1.test()
