#_*_coding:utf-8_*_
import card
import pickle
#信用卡信息
def info():
    print "你的信用卡额度为 \033[31m %s \033[0m 你的可用额度 \033[31m %s \033[0m取现额度为 \033[31m %s \033[0m 取现的手续费是 \033[31m %s \033[0m" %(card.card_credits,card.card_available,card.cash_amount,card.poundage)
#取现函数
def cash():
    #用户取现钱数
    cash_qx = int(raw_input("Please Input cash money：").strip())
    #判断是否超过取现额度
    if cash_qx < card.cash_amount:
        #计算手续费
        cash_sxf = cash_qx * card.poundage
        #计算剩余额度
        card.card_shuyu = card.card_credits-(cash_qx + cash_sxf)
        #可用额度
        card.card_available -= (cash_qx + cash_sxf)
        #将剩余额度写入文件用pickle模块进行持久化，交易记录
        f1 = file("temp.pkl","w")
        pickle.dump(cash_qx,f1,True)
        pickle.dump(cash_sxf,f1,True)
        f1.close()
        print "您取出的钱是 \033[31m %s \033[0m 需要的手续费是 \033[31m %s \033[0m" %(cash_qx,cash_sxf)
    else:
        print "您取现的额度超过了限定额度\033[31m %s \033[0m"%card.cash_amount
#查询函数
def inquiry():
    #查询剩余额度，用pickle模块的load方法读取文件中的持久化数据
    f1 = file('temp.pkl',"r")
    card_qk = pickle.load(f1)
    card_sxf = pickle.load(f1)
    print "你的剩余额度为 \033[31m %s \033[0m 你的可用额度 \033[31m %s \033[0m \n----交易列表----\n取现%s 手续费%s" %(card.card_shuyu,card.card_available,card_qk,card_sxf)
#还款函数
def repayment():
    #读取剩余额度，确定需要还款
    card_huankuan = card.card_credits-card.card_shuyu
    print "您需要还款",card_huankuan
    repayment_num = int(raw_input("输入你的还款："))
    #判断换款数是否大于需要还款数
    if repayment_num > card_huankuan:
        #如果大于还款数,剩余额度与信用卡额度相等
        card.card_shuyu = card.card_credits
        #可用额度换款数加上元可用额度
        card.card_available += repayment_num
    else:
        #如果小于需要的还款数,剩余额度与可用额度都等于原额度加上还款数
         card.card_shuyu += repayment_num
         card.card_available += repayment_num
    print "你的信用卡额度为: \033[31m %s \033[0m \n你的可用额度: \033[31m %s \033[0m \n剩余额度为:\033[31m %s \033[0m"%(card.card_credits,card.card_available,card.card_shuyu)
#转账函数
def transferred():
    #循环输入对方卡号3次
    for i in range(3):
        zhuangzhan_number = raw_input("请输入转账卡号:")
        #判断输入对方卡号是否正确
        if zhuangzhan_number == card.card_number_two:
            zhuangzhang_jine = int(raw_input("转账金额:"))
            #判断自己卡内是否足够
            if zhuangzhang_jine < card.card_available:
                #给对方可用额度加上转入金额
                card.card_available_new += zhuangzhang_jine
                #减掉自己账户可用额度
                card.card_available -= zhuangzhang_jine
                print "你转出 %s 卡内可用余额:%s "%(zhuangzhang_jine,card.card_available)
            else:
                print "你的余额不足"
        else:
            print "卡号输入错误"
    print "输入卡号错误-----退出"
if __name__ in "__main__":
    transferred()