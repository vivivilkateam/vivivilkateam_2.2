class BankAccount:# класс

    def __init__(self, balance):#функция
        self.__balance = balance# приватная переменная

    def deposit(self, amount):# функция
        if amount > 0:# если amount больше 0, то прибавляем amount к __balance
            self.__balance += amount

    def withdraw(self, amount):# функция
        if 0 < amount <= self.__balance:# если amount больше 0, но меньше __balance, то вычетаем  из __balance amount
            self.__balance -= amount
        else: # в противном случие будет вы водиться недостаточно средств
            print('недостаточно средств')

    def get_balance(self):# функция
        return self.__balance# возвращение  к __balance



account = BankAccount(1000)# balance
account.deposit(500)# сколько добавляем к __balance
print(account.get_balance())# 1500
# account.__balance # вызовет ожибку, так как __balance приватная переменная