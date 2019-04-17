#coding:utf-8
import xlrd,os,sys
import itertools
import pandas as pd
from prettytable import PrettyTable

class Ordering_system:
    """
    背景：为解决广大同胞点菜时的选择困难症，利用大数据分析为您提供最优选的点菜方案！
    Parameters：
    -----------
    bud:int
        预算（budget），default 50
    nog:int
        人数（Number of Guests），default 3
    dishes:int
        菜品数量（dishes），default 3
    coe:float
        价格浮动系数（coefficient），default 0.2
    n:int
        推荐输出菜品方案数，default 5
    **kwargs:dict
        弃选菜品配置项，Optional；
        配置方式举例：a='白菜',b='芹菜'；配置后，将不推荐包含任何配置项的推荐结果
        
    Examples
    --------
    >>> plan = Ordering_system(70,3,3,0.2,3,a='白菜',b='鸡',c='青菜')
    >>> plan.recommend_f('/Users/enniu/Desktop/menu.xlsx')
    +--------------------------------------------+--------------------+----------+
    |                    方案                    |      菜品价格      | 菜品总价 |
    +--------------------------------------------+--------------------+----------+
    |   ['湘味月牙骨', '外婆小炒', '葱爆二样']   | [28.0, 28.0, 28.0] |   84.0   |
    | ['雪菜蘑菇肉片', '湘味月牙骨', '葱爆二样'] | [28.0, 28.0, 28.0] |   84.0   |
    |    ['想吃土豆', '香酥排腩', '美味猪手']    | [16.0, 32.0, 36.0] |   84.0   |
    +--------------------------------------------+--------------------+----------+
    """
    def __init__(self, bud =50, nog=3, dishes=3, coe=0.2, n=5,**kwargs):
        self.bud = bud
        self.nog = nog
        self.dishes = dishes
        self.coe = coe
        self.n = n
        self.kwargs = list(kwargs.values())
    def recommend_f(self,url):
        menu_sheet=xlrd.open_workbook(url).sheet_by_name('Sheet1')
        dish=menu_sheet.col_values(0)[1:] #菜品
        price=menu_sheet.col_values(1)[1:] #价格
        if self.kwargs:
            dish = pd.Series(dish);price = pd.Series(price)
            label =dish.str.contains('|'.join(self.kwargs),regex = True)
            dish = dish[-label].tolist()
            price = price[-label].tolist()
            a = list(itertools.combinations(range(len(dish)), self.dishes))#输出所有的组合，即从总数量中无放回抽取3个的组合方案
        else:
            a = list(itertools.combinations(range(len(dish)), self.dishes))
        a1 = list(map(lambda x:sum(x),map(lambda x:[price[i] for i in x],a)))#输出每种组合方案的用餐金额总价
        a2 = pd.Series(a)[list(map(lambda x:True if x>=self.bud*(1-self.coe) and x<=self.bud*(1+self.coe) else False,a1))]#筛选出符合条件的搭配方案
        a3 = a2.apply(lambda x:[price[i] for i in x]) #输出菜品价格方案
        a4 = a2.apply(lambda x:[dish[i] for i in x]) #输出菜品方案
        a5 = list(filter(lambda x:x>=self.bud*(1-self.coe) and x<=self.bud*(1+self.coe),a1))#输出菜品方案的总价钱
        info = pd.DataFrame({"dishes":a4.tolist(),
                    "dish_price":a3.tolist(),
                     "total_price":a5
                    })
        info = info.sort_values(by = 'total_price',ascending = False).head(self.n) #输出前五种方案
        t = PrettyTable([])
        t.add_column("方案",info.dishes.tolist())
        t.add_column("菜品价格",info.dish_price.tolist())
        t.add_column("菜品总价",info.total_price.tolist())
        print(t)