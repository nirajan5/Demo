def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def simple():
    print("I am simple")

simple()
# let's decorate this ordinary function
pretty = make_pretty(simple)
pretty()



