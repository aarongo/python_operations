#coding=utf-8
user = 'test'
password = '123456'
log_success = False
passwd_erro = 0
'''                                 当用户输入正确的用户名后才可输入密码
                                    输入3次用户名错误后直接退出
                                    当用户输入正确的用户名后进行密码的输入
                                    输入正确后显示登录成功，错误3次后直接跳出
                                    -----------------介绍------------------
                                    是不是可以在输错密码3次后重新调回到输入用户名过程？？？
'''
for i in range(3):
    name = raw_input("Please your name:").strip()
    f = open("E:\pythonworks\works\day1\lockuser.txt")
    file_content = f.readline()
    f.close()
    status = 'locked'
    if file_content != status :
        if name == user:
            for i in range(3):
                passwd = raw_input("Please your password:").strip()
                if passwd == password:
                    print "Weclome Login"
                    log_success = True
                    break
                else:
                    print "Password error Please Rewrite Password"
                    passwd_erro += 1
            if passwd_erro == 3:
                # 输入错误3次错误时创建文件并追加内容
                f = open("E:\pythonworks\works\day1\lockuser.txt", 'w')
                f.write('locked')
                f.close()
                break
            if log_success == True:
                break
        else:
            print "Sorry,user is error"
    else:
        print "user is Locked"
        break