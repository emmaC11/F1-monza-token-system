class User:
    def __init__(self, acc_num, f_name, l_name, seat_num, overdraft, balance):
        self.acc_num = acc_num
        self.f_name = f_name
        self.l_name = l_name
        self.seat_num = seat_num
        self.overdraft = overdraft
        self.token_bal = balance


# testUser = User(5, "emma", "c", "5", "yes", 5)
# print(testUser.acc_num)
