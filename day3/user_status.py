#_*_coding:utf-8_*_
import os
import lock
import card
def userstatus():
    if os.path.exists("lock.txt"):
        print "用户已经被锁定"
    else:
        for user in range(3):
            card_unmuber = raw_input("Please input card number:").strip()
            if card_unmuber == card.card_number:
                lock.locked()
                break
if __name__ in '__main__':
    userstatus()
