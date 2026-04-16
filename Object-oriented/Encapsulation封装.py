class BankAccount:
    def __init__(self, owner, balance,leiyi):
        self.owner = owner  # 公有属性
        self._password = "123456"  # 受保护属性
        self.__balance = balance  # 私有属性
        self.__leiyi=leiyi

    # 对外暴露的接口：查询余额
    def get_balance(self, password):
        if password == self._password:
            return self.__balance
        else:
            return "密码错误"
    def check_leiyi(self,password):
        if self._password==password:
            return self.__leiyi
        else:
            return "密码错误"
    # 对外暴露的接口：存款
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款成功，当前余额：",end='')
            return self.__balance
        else:
            print("存款金额必须为正数")

if __name__ == "__main__":
    account = BankAccount("张三", 1000,"red")
    print(account.owner)  # 张三（公有属性可直接访问）
    print(account._password)  # 123456（受保护属性仍可直接访问，但不建议）
    #print(account.__balance)  # 报错：AttributeError，私有属性无法直接访问
    print(account.check_leiyi('123456'))
    # 通过接口访问和修改私有属性
    print(account.get_balance("123456"))  # 1000
    account.deposit(500)  # 存款成功，当前余额：1500