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

    @property
    def acc_num(self):
        print("getting value")
        return self._acc_num

    @acc_num.setter
    def acc_num(self, value):
        print("setting value")
        self._acc_num = value

    @property
    def f_name(self):
        print("getting value")
        return self._f_name

    @f_name.setter
    def f_name(self, value):
        print("setting value")
        self._f_name = value

    @property
    def l_name(self):
        print("getting value")
        return self._l_name

    @l_name.setter
    def l_name(self, value):
        print("setting value")
        self._l_name = value

    @property
    def seat_num(self):
        print("getting value")
        return self._seat_num

    @seat_num.setter
    def seat_num(self, value):
        print("setting value")
        self._seat_num = value


testUser = User(5, "emma", "c", "5", "yes", 5)
print(testUser.acc_num)


