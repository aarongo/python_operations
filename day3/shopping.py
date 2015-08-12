#_*_coding:utf-8_*_
import card
import login_interface
import lock
#购物网站
def merchandise():
    while True:
        for index,shop in enumerate(card.shop_list):
            print index,shop[0],shop[1]
        choose_shop = raw_input("输入购买的商品编号:")
        #判断输入是否为数字
        if choose_shop.isdigit():
            #取商品
            choose_shop = int(choose_shop)
            #加入购物车
            card.shop_car.append(card.shop_list[choose_shop])
            #计算需要支付的钱
            card.shop_money += card.shop_list[choose_shop][1]
        elif choose_shop == "quit":
            print "--------购物车列表--------"
            for index,shop in enumerate(card.shop_car):
                print index,shop[0],shop[1]
            print "你需要支付的金额为:%s"%card.shop_money
            login_interface.shoppay()
            lock.locked()
            break
if __name__ in '__main__':
    merchandise()