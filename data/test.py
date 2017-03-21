
def plus(a, b):
    sum = a + (a * b)
    for i in range(a):
        if i > 2:
            sum += i
        elif i == 0:
            pass
        else:
            sum -= i

    return a + b


def none():
    return 1



a = 5
b = 10
# target = name binOp (name binOp name)
c = a + (b + b)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 1, 2, 3]

d=a+a


sub_lisb = list[:10:2]
print(c)

# target = name binOp func(name,name)
c = c + a * plus(a, b)

"""
try:{
    name = Num
    pass
    except:{
        pass
    }
    finally:{
        pass
    }
}
"""
try:
    ast = 5
    pass
except:
    pass
