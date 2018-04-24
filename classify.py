#encoding:UTF-8
gyms= ['Cristiano Ronaldo', 'Carter', 'Lionel Messi', 'Timo Boll', 'na Ivanovic', 'liuguozheng', 'wangnan', 'wangzhizhi', "O'Neal", 'baochunlai', 'luoxuejuan', 'wangliqin', 'Bryant', 'dingjunhui', 'malin', 'tianliang', 'Marbury', 'lixiaopeng', 'zhangyining', 'liuguoliang', 'zhuting', 'wanghao', 'konglinghui']
idols=['yiyangqianxi', 'huge', 'dengziqi', 'dimaxi', 'huangzitao', 'Leonardo', 'wangkai', 'huyitian', 'shuchang', 'linjunjie', 'guanxiaotong', 'liminhao', 'gulinazha', 'liqin', 'ouhao', 'pengyuyan', 'wangjunkai', 'TaylorSwift', 'wangyuan', 'huangzhilie', 'panweibo', 'chenqiaoen', 'wangjiaer', 'zhaoliyin', 'tangyan', 'jindong', 'caixukun', 'liutao', 'zhangshaohan', 'baibaihe', 'ouyangnana', 'JessieJ', 'zhaoyouting', 'wangdalu', 'masichun', 'zhanggenshuo', 'zhangyixing', 'xuezhiqian', 'guobiting', 'chenweiting', 'zhenshuang', 'liushishi','zhongxintong', 'wuqilong']
policys=['xijinping', 'xucaihou', 'fanchanglong', 'zhouyongkang', 'chenxi', 'yuzhengsheng', 'zengqinghong', 'zhanggaoli', 'guoshengkun', 'liuqibao', 'lizhanshu', 'jiangzemin', 'mengjianzhu', 'lixi', 'huchunhua', 'liqiang', 'zhangdejiang', 'makai', 'liuyandong', 'lingjihua', 'yangjiechi', 'huangkunming', 'likeqiang', 'wanghuning', 'liyuanchao', 'dengxiaoping', 'lijianguo', 'chenminer', 'dingxuexiang', 'maozedong', 'wangchen', 'sunzhengcai', 'hanzheng', 'zhangchunxian', 'lihongzhong', 'yingyong', 'chenquanguo', 'guojinlong', 'sunchunlan', 'liuhe', 'xuqiliang', 'boxilai', 'yangxiaodu', 'hujintao', 'wangqishan', 'zhaoleji', 'zhangyouxia', 'wenjiabao', 'zhurongji', 'wangyang', 'zhaoziyang', 'guoboxiong', 'liuyunshan', 'caiqi', 'lipeng']


def classify(predict):
    if predict in gyms:
        return "体育"
    elif predict in idols:
        return "娱乐"
    elif predict in policys:
        return "政治"
    else:
        return "其他"
