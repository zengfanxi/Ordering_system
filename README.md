# Ordering_system（点菜推荐系统）
* 一个解决大家中午吃什么的Python脚本，对选择困难症人群有特效
* 可迭代的点
  * 商家的菜品信息如何获取（菜品&价格），是不是可以通过外卖平台或者点餐二维码入口爬取
  * 为了实现更好的交互体验，是不是可以局域网简单构建一套web框架
* 参数、调用方式、推荐结果如下：
  ```
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
    >>> plan.recommend_f('/.../menu.xlsx')
+------------------------------------------+--------------------+----------+
|                   方案                   |      菜品价格      | 菜品总价 |
+------------------------------------------+--------------------+----------+
|   ['葱爆二样', '香酥排腩', '美味猪手']   | [28.0, 32.0, 36.0] |   96.0   |
|   ['外婆小炒', '香酥排腩', '美味猪手']   | [28.0, 32.0, 36.0] |   96.0   |
|  ['湘味月牙骨', '香酥排腩', '美味猪手']  | [28.0, 32.0, 36.0] |   96.0   |
| ['雪菜蘑菇肉片', '香酥排腩', '美味猪手'] | [28.0, 32.0, 36.0] |   96.0   |
|  ['精品小炒肉', '香酥排腩', '美味猪手']  | [28.0, 32.0, 36.0] |   96.0   |
+------------------------------------------+--------------------+----------+

```
