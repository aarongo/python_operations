# _*_coding:utf-8_*_
__author__ = 'Lonny.Liu'
import account
import getpass
import sys
class Login(object):
    def login(self):
        name = raw_input("Please Input Your Name:")
        if name in account.user1_password:
            password = getpass.getpass("Please Input Your Password:")
        elif name in account.user2_password:
            print "----user2--->",account.user2_password[name]
run = Login()
run.login()