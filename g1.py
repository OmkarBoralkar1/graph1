import matplotlib.pyplot as plt
import numpy as np
print(" 1 for slope form")
print(" 2 for point form")
print(" 3 for circle")
print(" 4 for Triangle")
print(" 5 for Parabola ")
print("6. for substraction")
print("7. for addition")
print("8. for multiplication")
p=int(input("Enter the operation"))
if p>8:
    print("Invalid")
match p:
    case 1 :
        m=float(input("Ener the slope"))
        c=float(input("Enter the constant"))
        x=np.linspace(-5,5,100)
        y=m*x+c
        plt.plot(x,y,linestyle='dashed')
        plt.xlabel("plot the values of x")
        plt.ylabel("plot the values of y")
        plt.title("Slope  form")
        plt.show()
    case 2:
        x1=float(input("Enter the 1st point"))
        x2=float(input("Enter the 2nd point"))
        y1=float(input("Enter the 1st point"))
        y2=float(input("Enter the 2nd point"))
        z=(x2-x1)/(y2-y1)
        print("The slope is=",z)
        q=y1-z*x1
        print("The constant is =",q)
        plt.plot(x1,y1,linestyle='dashed',marker='D')
        plt.plot(x2,y2,linestyle='dashed',marker='D')
        plt.xlabel("x axis")
        plt.ylabel(" y axis")
        plt.title("Two point form")
        plt.show()
    case 3:
        print("For only radius put x and y as 0")
        g=int(input("ENTER THE CENTER of x axis "))
        f=int(input("ENTER THE CENTER of y axis"))
        b=int(input("Enter the radius of circle"))
        if b<=0:
            print("Invalid")
        else:
            angle=np.linspace( 0 ,2 *np.pi)
            x=b*np.cos(angle)+g
            y=b*np.sin(angle)+f
            Area= pi*b*b
            circumference=2*pi*b
            print(("The areaof the circle as"),Area,("And circumference as"),circumference)
            plt.plot(x,y)
            plt.title("Circle with centre and radius")
            plt.show()
    case 4:
        def triangle():
            n1=int(input("Enter the 1s side of triangle"))
            n2=int(input("Enter the 2s side of triangle"))
            n3=int(input("Enter the 3s side of triangle"))
            if n1==n2 and n2==n3 :
                print("it is an equilateral triangle")
                plt.scatter(n1,n2)
                plt.scatter(n2,n3)
                plt.scatter(n1,n3)
                plt.xlabel("x axis")
                plt.ylabel(" y axis")
                plt.title(" Equilateral Triangle")
                plt.show()
            if n1!=n2 and n2==n3 or n1==n2 and n2!=n3 or n1==n3 and n2!=n1:
                print("it is an isosceles triangle")
                plt.scatter(n1,n2)
                plt.scatter(n2,n3)
                plt.scatter(n1,n3)
                plt.xlabel("x axis")
                plt.ylabel(" y axis")
                plt.title(" isosceles triangle")
                plt.show()
            if n1!=n2 and n2!=n3 and n1!=n3:
                print("it is an scalene triangle") 
                plt.scatter(n1,n2)
                plt.scatter(n2,n3)
                plt.scatter(n1,n3)
                plt.xlabel("x axis")
                plt.ylabel(" y axis")
                plt.title(" scalene triangle")
                plt.show()
        triangle()
    case 5:
        print("1. for x axis")
        print("2. for y axis")
        r=int(input("Enter the operation"))
        if r>2 :
            print("Invalid")
        match r:
            case 1:
                a=float(input("Enter the value of a"))
                c=float(input("Enter the value of x intercept"))
                p=float(input("Enter the value of y intercept"))
                y=np.linspace(-2,10,20)
                if c>0:
                    (x)=((y-p)**2)/(4*a)+c
                    plt.plot(x,y)
                    plt.title("Parabola along +ve X axis")
                    plt.show()
                if c<0:
                    (x)=-((y-p)**2)/(4*a)+c
                    plt.plot(x,y)
                    plt.title("Parabola along +ve X axis")
                    plt.show()
                if c==0:
                    print("1. +ve along x axis")
                    print("2. -ve along x axis")
                    j=int(input("Enter the operation"))
                    if j>2 :
                        print("Invalid")
                    match j:
                        case 1:
                            (x)=((y-p)**2)/(4*a)+c
                            plt.plot(x,y)
                            plt.title("Parabola along +ve X axis")
                            plt.show()
                        case 2:
                            (x)=-((y-p)**2)/(4*a)+c
                            plt.plot(x,y)
                            plt.title("Parabola along -ve X axis")
                            plt.show()
            case 2:
                a=float(input("Enter the value of a"))
                c=float(input("Enter the value of x intercept"))
                p=float(input("Enter the value of y intercept"))
                x=np.linspace(-2,0,20)
                if p>0:
                    (y)=(((x-c)**2)/(4*a))+p
                    plt.plot(x,y)
                    plt.title("Parabola along +ve Y axis")
                    plt.show()
                if p<0:
                    (y)=-((x-c)**2)/(4*a)+p
                    plt.plot(x,y)
                    plt.title("Parabola along +ve Y axis")
                    plt.show()
                if p==0:
                    print("1. +ve along y axis")
                    print("2. -ve along y axis")
                    j=int(input("Enter the operation"))
                if j>2 :
                    print("Invalid")
                match j:
                    case 1:
                        (y)=((x-c)**2)/(4*a)+p
                        plt.plot(x,y)
                        plt.title("Parabola along +ve Y axis")
                        plt.show()
                    case 2:
                        (y)=-((x-c)**2)/(4*a)+p
                        plt.plot(x,y)
                        plt.title("Parabola along +ve Y axis")
                        plt.show()
    case 6:
        q=int(input("Enter the number of inputs you want"))
        a=[]
        b=[]
        v=0
        f=0
        r=0
        for t in range(q):
            t=float(input("Enter the first element"))
            a.append(t)
            r=r+t
        print(r)
        for u in range(q):
            u=float(input("Enter the second element"))
            b.append(u)
            f=f+u
        print(f)
        for g,w in zip(a,b):
            q=float(g)-float(w)
            v=v+q
            print(q,',',end="") 
        print('\n',v)
        c=r-f
        print(c)
    case 7:
        q=int(input("Enter the number of inputs you want"))
        a=[]
        b=[]
        v=0
        f=0
        r=0
        for t in range(q):
            t=float(input("Enter the first element"))
            a.append(t)
            r=r+t
        print(r)
        for u in range(q):
            u=float(input("Enter the second element"))
            b.append(u)
            f=f+u
        print(f)
        for g,w in zip(a,b):
            q=float(g)+float(w)
            v=v+q
            print(q,',',end="") 
        print('\n',v)
        c=r+f
        print(c)
    case 8:
        q=int(input("Enter the number of inputs you want"))
        a=[]
        b=[]
        v=0
        f=0
        r=0
        for t in range(q):
            t=float(input("Enter the first element"))
            a.append(t)
            r=r+t
        print(r)
        for u in range(q):
            u=float(input("Enter the second element"))
            b.append(u)
            f=f+u
        print(f)
        for g,w in zip(a,b):
            q=float(g)*float(w)
            v=v+q
            print(q,',',end="") 
        print('\n',v)
        c=r*f
        print(c)
