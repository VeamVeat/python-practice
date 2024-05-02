class A:
    def __init__(self):
        self.__f = 2

    def get(self):
        return self.__f


class B(A):
    def __init__(self):
        self.__f = 1
        super().__init__()

    def cget(self):
        return self.__f


instance_b = B()
result = instance_b.cget()
print(result)
