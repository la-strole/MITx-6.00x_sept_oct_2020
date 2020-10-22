class Foo:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def __repr__(self):
        return str(self.x)

menu = [Foo(x) for x in range(10)]

print(sorted(menu, key=Foo.get_x, reverse=True))
