"""
属性分为两种：
类属性：所有的对象都有且相同
实例属性：需要输入，允许不同
"""

class Car:
#类属性
    Car_wheel=4

    def __init__(self,c_brand,c_name="",c_price=0):#实例属性
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
    def __eq__(self, other_car):
        return self.brand==other_car.brand and self.name==other_car.name and self.price==other_car.price
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}'s {self.Car_wheel} wheel is running."#当print(c1)时，输出结果为‘奔驰奔驰S类is running.’
    def __lt__(self, other_car):
        return self.price<other_car.price
    
brand,name,price=input().split()
print(Car(brand,name,int(price)))
