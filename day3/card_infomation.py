#_*_coding:utf-8_*_
import card
import pickle
#信用卡信息
def info():
    print "你的信用卡额度为 \033[31m %s \033[0m 取现额度为 \033[31m %s \033[0m 取现的手续费是 \033[31m %s \033[0m" %(card.card_credits,card.cash_amount,card.poundage)
#取现函数
def cash():
    #用户取现钱数
    cash_qx = int(raw_input("Please Input cash money：").strip())
    #判断是否超过取现额度
    if cash_qx < card.cash_amount:
        #计算手续费
        cash_sxf = cash_qx * card.poundage
        #计算剩余额度
        card.card_credits -= (cash_qx + cash_sxf)
        #将剩余额度写入文件用pickle模块进行持久化，方便查询
        f1 = file("temp.pkl","w")
        pickle.dump(card.card_credits,f1,True)
        f1.close()
        print "您取出的钱是 \033[31m %s \033[0m 需要的手续费是 \033[31m %s \033[0m" %(cash_qx,cash_sxf)
    else:
        print "您取现的额度超过了限定额度\033[31m %s \033[0m"%card.cash_amount
#查询函数
def inquiry():
    #查询剩余额度，用pickle模块的load方法读取文件中的持久化数据
    f2 = file('temp.pkl',"r")
    card_syed = pickle.load(f2)
    print "你的剩余额度为 \033[31m %s \033[0m" %card_syed
#还款函数
def repayment():
    #读取剩余额度，确定需要还款
    f3  = file ("temp.pkl","r")
    card_syed = int(pickle.load(f3))
    f3.close()
    #print "您需要还款",(card.card_lines-card_syed)
    repayment_num = raw_input("输入你的还款：")

#转账函数
def transferred():
    print "--------transferred--------"
if __name__ in "__main__":
    info()
    cash()
    inquiry()
    repayment()
    transferred()