#
# main program file for fictitious bank account management system
#

BANK_NAME = "Excellent Bank"


def main():
    welcome()
    myaccount = Account("Brian", 1000)
    print(myaccount.balance, myaccount.owner)
    myaccount.deposit(500)
    myaccount.withdrawal(250)
    myaccount.withdrawal(myaccount.balance)
    myaccount.withdrawal(1)


# object class for each bank account in the system
class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("\nnew balance is ${}".format(self.balance))

    def withdrawal(self,amount):
        if amount <= self.balance:
            # process the withdrawal
            self.balance -= amount
            print("\nnew balance is ${}".format(self.balance))
        else:
            print("\ninsufficient funds in account")
            print("\ncurrent balance is ${}".format(self.balance))


class Member:
    pass


def welcome():
    welcome_string = "*  Welcome to {}'s account management system. *".format(BANK_NAME)
    print("*" * len(welcome_string))
    print(welcome_string)
    print("*" * len(welcome_string))


main()
exit()
