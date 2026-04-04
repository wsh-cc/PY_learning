"""
https://blog.csdn.net/m0_74091159/article/details/144321721

"""
numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers) # 将列表转化为迭代器

# 使用 next() 访问元素

print(next(iterator)) # 输出: 1
print(next(iterator)) # 输出: 2
print(next(iterator)) # 输出: 3
