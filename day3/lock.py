#_*_coding:utf-8_*_
import card
def locked():
    for passwd in range(3):
        card_passwd = raw_input("Please input card passworld:").strip()
        if card_passwd == card.card_passwd:
            print "\033[32m--------welcome Login--------\033[0m"
            break
        else:
            card.error += 1
            print "密码输入错误\033[31m%s\033[0m次" %card.error
    if card.error == 3:
        lock = file("E:\pythonworks\works\day3\lock.txt","w")
        lock.write("locked")
        lock.close()
        print "密码输入错误 %s 次 帐号锁定" %card.error
if __name__  == "__main__":
    locked()
