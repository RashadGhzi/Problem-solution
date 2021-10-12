"""def first(msg):
    print(msg)

first("hello")
second = first
second("hello")
"""

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")

        return func()
    return inner(1,0)


@smart_divide
def divide():
    print("not good")
