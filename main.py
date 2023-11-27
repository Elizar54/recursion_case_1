import turtle as t


# Running square
def square(size):
    for side in range(4):
        t.fd(size)
        t.lt(90)


def running_square(size):
    if size <= 1:
        return None
    square(size)
    t.fd(size*0.2)
    t.lt(4)
    return running_square(0.7*size)


def main_square():
    t.up()
    t.goto(-100, 0)
    t.down()
    size = int(input('Введите длину стороны квадрата: '))
    running_square(size)
    t.mainloop()


# Binary tree
def binary_tree(depth, size, angle):
    if depth == 0:
        t.forward(size)
        t.backward(size)
    else:
        t.forward(size)
        t.right(angle/2)
        binary_tree(depth - 1, size / 2, angle)
        t.left(angle)
        binary_tree(depth - 1, size / 2, angle)
        t.right(angle/2)
        t.backward(size)


def main_branch():
    t.up()
    t.lt(90)
    t.goto(-100, 0)
    t.down()
    depth = int(input('Введите высоту дерева'))
    angle = int(input('Введите величину угла между ветками: '))
    binary_tree(depth, 100, angle)
    t.done()


# Koch curve
def koch_curve(depth, size):
    if depth == 0:
        t.fd(size)
    else:
        koch_curve(depth-1, size/3)
        t.lt(60)
        koch_curve(depth-1, size/3)
        t.rt(120)
        koch_curve(depth-1, size/3)
        t.lt(60)
        koch_curve(depth-1, size/3)


def main_koch_curve():
    t.up()
    t.goto(-200, 0)
    t.down()
    depth = int(input('Введите порядок кривой: '))
    size = int(input('Введите размер кривой: '))
    koch_curve(depth, size)
    t.done()


def koch_snowflake():
    t.up()
    t.goto(-200, 0)
    t.down()
    depth = int(input('Введите глубину рекурсии: '))
    size = int(input('Введите размер кривой: '))
    koch_curve(depth, size)
    t.rt(120)
    koch_curve(depth, size)
    t.rt(120)
    koch_curve(depth, size)
    t.rt(120)
    t.done()
