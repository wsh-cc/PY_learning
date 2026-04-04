"""
魔法方法
__init__//初始化运算符

__str__//字符串运算符

__eq__//比较两个对象是否相等

__lt__,__le__,__gt__,__ge__//对象比较运算符

分别是less than,less than or equal to,greater than,greater than or equal to
"""
# __init__
"""

class 类名：
    def __init__(self,参数列表)：
        self.属性名=参数1
        self.属性名=参数2
        self.属性名=参数3
"""
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
    def __eq__(self, other_car):
        return self.brand==other_car.brand and self.name==other_car.name and self.price==other_car.price
    def __str__(self):
        return f"{self.brand}{self.name}is running."#当print(c1)时，输出结果为‘奔驰奔驰S类is running.’
    def __lt__(self, other_car):
        return self.price<other_car.price
c1=Car("奔驰","奔驰S类",1000000)
c2=Car("奔驰","奔驰S类",1000000)
print(c1==c2)#如果没有__eq__方法,输出结果为false,因为这里比较的是地址

print(c1<c2)#如果没有__lt__方法,输出结果为false,正确    
#但是如果没写__lt__,就不能比较

print(c1)#有了__str__方法,输出时会调用__str__方法,输出结果为‘奔驰奔驰S类is running.’

