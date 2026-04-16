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
    
c1=Car("奔驰","奔驰S类",1000000)
print(c1.__dict__)
