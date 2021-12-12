def add(*args):
    num = 0
    for i in args:
        print(f"Value is : {i} at position {args[i-1]}")
        num += i

    print(num)

add(1,2,3,4)


def calculate(n, **kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k)
        print(v)
    n += kwargs['add']
    print(n)
    n *= kwargs['mutiply']
    print(n)

calculate(2, add=3, mutiply=5)


class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")

my_car = Car(model = 'TATA')
print(my_car.model)
print(my_car.make)