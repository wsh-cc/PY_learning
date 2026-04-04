"""
class 类名：
    def __init__(self,参数列表)：
        self.属性名=参数1
        self.属性名=参数2
        self.属性名=参数3

    def 方法(self,参数列表)：

    def 方法(self,参数列表)：
    
    def 方法(self,参数列表)：
    

"""
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
        
    def run(self):
        print(f"{self.brand}{self.name}is running.")
    
    def rating(self,price,quality,service):#方法
        print(f"您的汽车的综合评分为{price+quality+service}")
        return price+quality+service
    
c1=Car("奔驰","奔驰S类",1000000)
print(c1.__dict__)
c1.run()
print(c1.rating(100,90,80))
