#print("hello world")
#a,b,c=map(int,input().split())
#print("first lesson")
#单行注释
"""
py中变量没有类型,但变量存的数据有类型
"""
#print("hello world",1,2,3,'final')
# print(type(1))
# print(type(2.0))
# print(type([1,2,3]))
# print(type(('a',1,"sdsa")))
# print(type("string"))
#a,b=map(int,input('asdfasd').split())
# 年龄='www'
# print(年龄)
# print("'sring'") 
# print('"string')
# print("""string""")
# abc="""string"""
# # print("\'string\'")转义字符可将特殊字符转义为普通字符,
# #                    反之亦可以将无特殊功能字符转换为特殊字符
# print("''hello world''")
# print("hello",'年龄')
""" 不用加号会有空格"""
# print("hello"*50)
# money=1000
# print('我真牛逼'+str(money))
# name=('a','b')
# print("wo zhen liu bi %s %s"%name)
# message="我是%s,今年%d"%('1',2)
# print(message)
# for i in range(0,100,10):
#     print('%10d'%i)
if __name__ =="__main__":
    print('-'*20)
    for i in range(5):
     print()
    member='abc'
    age=18.333
    print(f"wo de dai hao shi {member},jian lian yi jing {age:5.2f} shui le")#格式化输出,也有精度度控制5.2f表示保留5位小数,2f表示保留2位小数
    print('-'*20)
else:
   print("this is not main file")

print("hello world%s"%(12*20+0.001))
print(1<2<3>2)
    
 