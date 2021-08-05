class sheep:
    sheep = 0
    def __init__(self,arg1):
        self.arg1 = arg1
    def rt(self):
        self.sheep += self.arg1
        return self.sheep
    def __add__(self, other):
        if isinstance(other, rabbit):
            other = stk2.rt()
            if (self.arg1)/1.5 >= (other)/3:
                return print ('порций супа: ', int(other/3))
            if (self.arg1)/1.5 <= (other)/3:
                return print ('порций супа: ', int((self.arg1)/1.5))
class rabbit:
    rabbit = 0
    def __init__(self, arg):
        self.arg = arg

    def rt(self):
        self.rabbit += self.arg
        return self.arg

    def __add__(self, other):
        if isinstance(other, sheep):
            other = stk.rt()
            if ((self.arg)/3) >= ((other) / 1.5):
                return print('порций супа: ', int(other / 1.5))
            if ((self.arg)/3) <= ((other) / 1.5):
                return print('порций супа: ', int((self.arg) / 3))

stk = sheep(100)
stk2 = rabbit(180)
stk.rt()
stk2.rt()
print(stk2+ stk)