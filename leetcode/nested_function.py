from typing import List


def outer_function(t: str):
    text: str = t

    def inner_function():
        print(text)

    inner_function()


# outer_function('Hello!')


def outer_function2(a: List[int]):
    b: List[int] = a
    print(id(b), b)

    def inner_function1():
        b.append(4)
        print(id(b), b)

    def inner_function2():
        print(id(b), b)

    def inner_function3():
        b = [4, 5, 6]
        print(id(b), b)


    inner_function1()
    inner_function2()
    inner_function3()


outer_function2([1, 2, 3])


def outer_function3(a: str):
    text: str = a
    print(id(text), text)

    def inner_function1():
        text = 'World!'
        print(id(text), text)

    def inner_function2():
        print(id(text), text)

    inner_function1()
    inner_function2()


outer_function3('Hello!')