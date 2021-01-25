import math as algebra


def Quadratic():
    print("ax2+bx+c=0")
    a = float(input(print("co-efficient of x2 = ")))
    b = float(input(print("co-efficient of x =")))
    c = float(input(print("constant term= ")))
    delta = algebra.sqrt(pow(b, 2) - 4 * a * c)
    print(delta)
    if delta == 0:
        print(f"x1 = {-b / 2}")
        print(f"x2 = {-b / 2}")
    elif delta > 0:
        print(f"x1 = {(-b + delta) / 2}")
        print(f"x2 = {(-b - delta) / 2}")
    elif delta < 0:
        print(f"x1 = {-b / 2}+i{delta / 2}")
        print(f"x2 = {-b / 2}-i{delta / 2}")


def Cubic():
    print("ax3+bx2+cx+d=0")
    a = float(input(print("co-efficient of x3 = ")))
    b = float(input(print("co-efficient of x2 =")))
    c = float(input(print("co-efficient of x =")))
    d = float(input(print("constant term =")))


def Linear(flag):
    if flag == 2:
        matA = []
        matB = []
        a1 = float(input(print("co-effeicient of x1= ")))
        b1 = float(input(print("co-effeicient of y1= ")))
        c1 = float(input(print("constant term1= ")))
        a2 = float(input(print("co-effeicient of x2= ")))
        b2 = float(input(print("co-effeicient of y2= ")))
        c2 = float(input(print("constant term2= ")))
        matA = [[a1, a2], [b1, b2]]
        matB = [[c1], [c2]]


def main():
    choice = input("Select the operation:\n1. Linear Equation\n2. Quadratic Equation\n3. Cubic Equation\n ")
    if choice == '1':
        select = input("Select:\n1. ax+b=0\n2. ax+by=c\n3. ax+by+cz=d")
        if select == '1':
            Linear(1)
        elif select == '2':
            Linear(2)
        elif select == '3':
            Linear(3)
    elif choice == '2':
        Quadratic()
    elif choice == '3':
        Cubic()


main()
