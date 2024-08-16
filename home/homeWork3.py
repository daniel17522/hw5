class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    def moneyX(self):
        count = int(input('добавьте на свой счет деньги!'))
        if count > 0:
            self._balance += count
            print(f'новый баланс: {self._balance}')
        else:
            'введите положительное число'
    def _kill(self):
        self._balance = 0
        print('ваш баланс сброшен до 0')
    def __jackpot(self):
        self._balance *= 10
        print(f'ваш баланс после джекпота:{self._balance}')
    def demo_jackpot(self):
        self.__jackpot()
    def _double(self, newbalance):
        self._balance += newbalance._balance
        print(f"баланс после комбинации с {newbalance._name}: {self._balance}")

bank1 = Bank('mbank', 1000)
bank2 = Bank('optima', 2000)


bank1.moneyX()
bank1._kill()
bank1._double(bank2)
bank1.demo_jackpot()