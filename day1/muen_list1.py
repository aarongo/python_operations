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
print zidian.get('china').get('beijing').fromkeys()