class Dog:
    def make_sound(self):
        print("汪汪汪")

class Cat:
    def make_sound(self):
        print("喵喵喵")

# 统一的接口函数
def animal_sound(animal):
    animal.make_sound()
    #多态就是函数的调用，但要保证有这个方法，否则会报错

# 不同对象调用同一个接口，产生不同结果
dog = Dog()
cat = Cat()
animal_sound(dog)  # 汪汪汪
animal_sound(cat)  # 喵喵喵

