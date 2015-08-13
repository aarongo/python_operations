# _*_coding:utf-8_*_
import card
import card_infomation
import shopping


def locked():
    for passwd in range(3):
        card_passwd = raw_input("Please input card passworld:").strip()
        if card_passwd == card.card_passwd:
            print "\033[32m--------welcome Login--------\033[0m"
            print "1---->\033[31m 查询 \033[0m 2---->\033[32m 还款 \033[0m 3---->\033[33m 转账 \033[0m 4---->\033[34m 取现 \033[0m 5---->\033[35m 购物 \033[0m 6---->\033[36m 退出 \033[0m"
            caozuo = int(raw_input("请输入要做什么?"))
            if caozuo == 1:
                card_infomation.inquiry()
            elif caozuo == 2:
                card_infomation.repayment()
            elif caozuo == 3:
                card_infomation.transferred()
            elif caozuo == 4:
                card_infomation.cash()
            elif caozuo == 5:
                shopping.merchandise()
            elif caozuo == 6:
                break
            break
        else:
            card.error += 1
            print "密码输入错误\033[31m%s\033[0m次" % card.error
    if card.error == 3:
        lock = file("E:\python_operations\day3\lock.txt", "w")
        lock.write("locked")
        lock.close()
        print "密码输入错误 %s 次 帐号锁定" % card.error


if __name__ == "__main__":
    locked()
