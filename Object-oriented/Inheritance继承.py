class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}是一只动物"#__str__魔法方法会在直接被print的时候调用
    def animal_move(self):
        return f"{self.name}会移动"
    def speak(self):
        print(f"{self.name}会说话")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类 Animal 的 __init__ 方法
        self.breed = breed

class Person(Animal):
    zhiye=''
    def __init__(self,name,zhandouli):
        super().__init__(name)
        self.zhandouli=zhandouli
    

# def animal_speak(Animal):
#     Animal.speak()

def animal_speak(animal):
    animal.speak()  # 传入任何Animal类型的对象，它都会调用speak方法 
   


# 创建 Dog 对象
dog = Dog("Buddy", "Golden Retriever")
p=Person("张三",1000)
print(dog.name)  # 输出: Buddy
print(dog.breed)  # 输出: Golden Retriever
print(dog)  
print(p.animal_move())

animal_speak(p)
