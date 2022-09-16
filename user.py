class User:
    def __init__(self, acc_num, f_name, l_name, seat_num, overdraft, balance):
        self.acc_num = acc_num
        self.f_name = f_name
        self.l_name = l_name
        self.seat_num = seat_num
        self.overdraft = overdraft
        self.token_bal = balance

    def __repr__(self):
        repr = (f"{str(self.acc_num).ljust(20)} {self.f_name.ljust(20)}")
        repr = repr + (f"{self.seat_num.ljust(20)} {self.l_name.ljust(20)}")
        repr = repr + (f"{self.overdraft.ljust(20)} {self.token_bal:.2f}")
        return repr


testUser = User(5, "emma", "c", "5", "yes", 5)
print(testUser)


