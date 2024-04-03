class A:
    def do_thing(self):
        print('From A')


class B(A):
    def do_thing(self):
        print('From B')
        super().do_thing()


class C(A):
    def do_thing(self):
        print('From C')
        super().do_thing()


class D(B, C):
    def do_thing(self):
        print('From D')
        super().do_thing()


d = D()
d.do_thing()

#Что выведется и почему?


# From D
# From B
# From C
# From A

# Вершина вызывается в самом конце

