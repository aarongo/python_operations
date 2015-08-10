#coding=utf-8
zidian = {
    'china':{
        'beijing':{
            'chaoyang':{
               'chaoshi': ['jialefu','woerma']
            },
            'haidian':{
                 'chaoshi':['letianmate','hualian']
            },
        'shanghai':{
            'putuo':{
                'chaoshi':['7tian','dazhong']
            },
            'pudong':{
                'chaoshi':['sunin','chutian']
            }
        }
        }
    }
}
addiress = raw_input("Please city:")
addiress1 = raw_input("Please area:")
tuichu = False
while addiress == 'beijing':
    while addiress1 == 'chaoyang':
        for i in range(3):
            c1 = zidian.get('china').get('beijing').get('chaoyang').get('chaoshi')[0]
            c2 = zidian.get('china').get('beijing').get('chaoyang').get('chaoshi')[1]
            slect =  raw_input("""Please select chaoshi:
                    1.   %s
                    2.  %s
                    3.返回
                """ %(c1,c2))
            if slect == '1':
                print "欢迎来到 %s" %c1
            if slect == '2':
                print "欢迎来到 %s" %c2
            if slect == 3:
                tuichu  = True
                break
        break
    if tuichu == True:break