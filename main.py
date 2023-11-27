'''
Elizarev Yaroslav -
Leonov Kirill - 50
'''

import turtle as t
t.speed(10)


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


def ice_fractal_one(order, length):
    if order == 0:
        t.fd(length)
    else:
        ice_fractal_one(order - 1, length / 2)
        t.lt(90)
        ice_fractal_one(order - 1, length / 4)
        t.lt(180)
        ice_fractal_one(order - 1, length / 4)
        t.lt(90)
        ice_fractal_one(order - 1, length / 2)


def main_ice_fractal_one():
    t.up()
    t.goto(-200, 0)
    t.down()
    order = int(input('Введите глубину рекурсии: '))
    length = int(input('Введите размер кривой: '))
    ice_fractal_one(order, length)
    t.done()


def ice_fractal_two(order, length):
    if order == 0:
        t.fd(length)
    else:
        ice_fractal_two(order - 1, length / 2)
        t.lt(120)
        ice_fractal_two(order - 1, length / 4)
        t.lt(180)
        ice_fractal_two(order - 1, length / 4)
        t.lt(120)
        ice_fractal_two(order - 1, length / 4)
        t.lt(180)
        ice_fractal_two(order - 1, length / 4)
        t.lt(120)
        ice_fractal_two(order - 1, length / 2)


def main_ice_fractal_two():
    t.up()
    t.goto(-200, 0)
    t.down()
    order = int(input('Введите глубину рекурсии: '))
    length = int(input('Введите размер кривой: '))
    ice_fractal_two(order, length)
    t.done()


def levy_curve(order, length):
    if order == 0:
        t.fd(length)
    else:
        t.lt(45)
        levy_curve(order - 1, length / 2)
        t.rt(90)
        levy_curve(order - 1, length / 2)
        t.lt(45)


def main_levy_curve():
    t.up()
    t.goto(-200, 0)
    t.down()
    order = int(input('Введите глубину рекурсии: '))
    length = int(input('Введите размер кривой: '))
    levy_curve(order, length)
    t.done()

#Branch fractal
def branch(n, size):
    if n == 0:
        t.left(180)
        return

    x = size/(n+1)
    
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)

def main_branch():
  n = int(input('Введите глубину рекурсии: '))
  size = int(input('Введите размер ветки: '))
  t.up()
  t.goto(-100, 0)
  t.down()
  t.left(90)
  branch(n, size)
  t.done()

#Minkovsiy curve

def minkovskiy_curve(depth, size):
  t.speed(100)
  if depth == 0:
    t.forward(size)
    return
    
  else:
    minkovskiy_curve(depth-1, size*0.5)
    t.lt(90)
    minkovskiy_curve(depth-1, size*0.5)
    t.rt(90)
    minkovskiy_curve(depth-1, size*0.5)
    t.rt(90)
    minkovskiy_curve(depth-1, size*0.5)
    minkovskiy_curve(depth-1, size*0.5)
    t.lt(90)
    minkovskiy_curve(depth-1, size*0.5)
    t.lt(90)
    minkovskiy_curve(depth-1, size*0.5)
    t.rt(90)
    minkovskiy_curve(depth-1, size*0.5)

def main_minkovskiy_curve():
    size = int(input('Введите размер кривой'))
    depth = int(input('Введите глубину рекурссии: '))
    t.up()
    t.goto(-500, 0)
    t.down()
    minkovskiy_curve(depth, size)
    t.done()

#Yaroslav's fractal

def Elizarev_curve(depth, size):
    if depth == 0:
        t.fd(size)
    else:
        t.lt(60)
        Elizarev_curve(depth-1, size*0.5)
        t.rt(120)
        Elizarev_curve(depth-1, size*0.5)
        t.lt(60)
        Elizarev_curve(depth-1, size*0.5)
        t.lt(60)
        Elizarev_curve(depth-1, size*0.5)
        t.rt(120)
        Elizarev_curve(depth-1, size*0.5)
        t.lt(60)

t.up()
t.goto(-300, 0)
t.down()
Elizarev_curve(2, 200)
t.done()