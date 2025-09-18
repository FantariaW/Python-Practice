# Lesson 10 Training: global
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Lesson 10 Training
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n


def main():
    acc = Account()
    print("Balance: ", acc.balance)
    acc.deposit(100)
    print("New Balance: ", acc.balance)


if __name__ == "__main__":
    main()


# -----------------------------------------------------------------------------


# balance = 0
#
#
# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("New Balance", balance)
#
#
# def deposit(n):
#     global balance
#     balance += n
#
#
# def withdraw(n):
#     global balance
#     balance -= n
#
#
# if __name__ == "__main__":
#     main()
