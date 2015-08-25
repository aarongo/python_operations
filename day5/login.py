# _*_coding:utf-8_*_
__author__ = 'Lonny.Liu'
import account


class Login(object):
    def login(self):
        name = raw_input("Please Input Your Name:")
        if name in account.user_password.keys():
            password = raw_input("Please Input Password:")
            if password == account.user_password[name]:
                print "--------Welcome Login ftpserver-------"
        else:
            print "--------User does not exist------"

if __name__ == "__main__":
    Login().login()
