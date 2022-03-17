class Account:
    def __init__(self,name,balence,min_balence):
        self.balence = balence
        self.name= name
        self.min_balence =min_balence
    def deposit(self,amount):
        self.balence +=amount
    def withdraw(self,amount):
        if self.balence-amount >=self.min_balence:
            self.balence -= amount
        else:
            print("not sufficient balence")

    def statments(self):
        print("account balence is {}".format(self.balence))
class Current(Account):
    def __init__(self,name,balence):
        super.__init__(name,balence,min_balence=-1000)

        

