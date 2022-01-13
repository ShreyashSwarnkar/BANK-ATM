class Atm(object):
    
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        print("\nYour card number is",self.card_number)
        self.pin_number = pin_number
        print("Your pin number is",self.pin_number)

    def Withdrawl(self):
        print("\nCash Withdrawl is 20M")

    def BalanceEnquiry(self):
        print("\nBalance is 200M")

atms = Atm(554628456,736565955)
atms.Withdrawl()
atms.BalanceEnquiry()
