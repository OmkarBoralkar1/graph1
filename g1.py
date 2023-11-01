import matplotlib.pyplot as plt
import numpy as np
from cmath import pi



class OperationHandler:
    def process(self):
        pass

    def plot(self):
        pass

class SlopeForm(OperationHandler):
    def process(self):
        m = float(input("Enter the slope: "))
        c = float(input("Enter the constant: "))
        x = np.linspace(-5, 5, 100)
        y = m * x + c
        self.x_values = x
        self.y_values = y

    def plot(self):
        plt.plot(self.x_values, self.y_values, linestyle='dashed')
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("Slope Form")
        plt.show()

class PointForm(OperationHandler):
    def process(self):
        x1 = float(input("Enter the x-coordinate of the 1st point: "))
        x2 = float(input("Enter the x-coordinate of the 2nd point: "))
        y1 = float(input("Enter the y-coordinate of the 1st point: "))
        y2 = float(input("Enter the y-coordinate of the 2nd point: "))
        if x2 - x1 == 0:
            print("Vertical line, slope is undefined.")
            return
        z = (y2 - y1) / (x2 - x1)
        q = y1 - z * x1
        self.x_values = [x1, x2]
        self.y_values = [y1, y2]
        self.slope = z
        self.constant = q

    def plot(self):
        plt.plot(self.x_values, self.y_values, linestyle='dashed', marker='D')
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("Two Point Form")
        plt.show()
        print("The slope is =", self.slope)
        print("The constant is =", self.constant)

class Triangle(OperationHandler):
    def process(self):
        n1 = float(input("Enter the 1st side of the triangle: "))
        n2 = float(input("Enter the 2nd side of the triangle: "))
        n3 = float(input("Enter the 3rd side of the triangle: "))
        self.sides = [n1, n2, n3]

    def plot(self):
        for side in self.sides:
            plt.scatter(side, side)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        if len(set(self.sides)) == 1:
            print("It is an equilateral triangle")
            plt.title("Equilateral Triangle")
        elif len(set(self.sides)) == 2:
            print("It is an isosceles triangle")
            plt.title("Isosceles Triangle")
        else:
            print("It is a scalene triangle")
            plt.title("Scalene Triangle")
        plt.show()

class Circle(OperationHandler):
    def process(self):
        print("For only radius, put x and y as 0")
        g = float(input("Enter the center of x-axis: "))
        f = float(input("Enter the center of y-axis: "))
        b = float(input("Enter the radius of the circle: "))
        if b <= 0:
            print("Invalid")
            return
        angle = np.linspace(0, 2 * pi)
        x = b * np.cos(angle) + g
        y = b * np.sin(angle) + f
        self.x_values = x
        self.y_values = y
        self.area = pi * b * b
        self.circumference = 2 * pi * b

    def plot(self):
        plt.plot(self.x_values, self.y_values)
        plt.title("Circle with center and radius")
        plt.show()
        print("The area of the circle is", self.area)
        print("The circumference is", self.circumference)

    def handle_additional_info(self):
        choice = input("Do you want to calculate the tangent? (yes/no): ").lower()
        if choice == "yes":
            self.tangent()
        else:
            print("Tangent calculation skipped.")

    def tangent(self):
        x1 = float(input("Enter the x-coordinate of the point for the tangent: "))
        y1 = float(input("Enter the y-coordinate of the point for the tangent: "))
        if (x1 - self.x_values[0])**2 + (y1 - self.y_values[0])**2 == self.x_values[0]**2 + self.y_values[0]**2:
            plt.plot(x1, y1, 'ro', label="Tangent Point")
            plt.title("Circle with Tangent")
            plt.legend()
            plt.show()
        else:
            print("The point is not on the circle.")

class Parabola(OperationHandler):
    def process(self):
        print("1. For x-axis")
        print("2. For y-axis")
        r = int(input("Enter the operation: "))
        if r not in [1, 2]:
            print("Invalid")
            return

        a = float(input("Enter the value of a: "))
        c = float(input("Enter the value of x intercept: "))
        p = float(input("Enter the value of y intercept:"))
        self.r=r
        self.a = a  # Store 'a' as an instance variable
        self.c = c  # Store 'c' as an instance variable
        self.p = p  # Store 'p' as an instance variable

        if r == 1:
            y = np.linspace(-2, 10, 20)
            if c > 0:
                x = ((y - p) ** 2) / (4 * a) + c
                plt.plot(x, y)
                plt.title("Parabola along +ve X axis")
                plt.show()
            if c < 0:
                x = (-(y - p) ** 2) / (4 * a) + c
                plt.plot(x, y)
                plt.title("Parabola along -ve X axis")
                plt.show()
            if c == 0:
                print("1. +ve along x axis")
                print("2. -ve along x axis")
                j = int(input("Enter the operation: "))
                if j not in [1, 2]:
                    print("Invalid")
                    return
                if j == 1:
                    x = ((y - p) ** 2) / (4 * a) + c
                    plt.plot(x, y)
                    plt.title("Parabola along +ve X axis")
                    plt.show()
                if j == 2:
                    x = (-(y - p) ** 2) / (4 * a) + c
                    plt.plot(x, y)
                    plt.title("Parabola along -ve X axis")
                    plt.show()
        elif r == 2:
            x = np.linspace(-2, 10, 20)
            if p > 0:
                y = (((x - c) ** 2) / (4 * a)) + p
                plt.plot(x, y)
                plt.title("Parabola along +ve Y axis")
                plt.show()
            if p < 0:
                y = -((x - c) ** 2) / (4 * a) + p
                plt.plot(x, y)
                plt.title("Parabola along -ve Y axis")
                plt.show()
            if p == 0:
                print("1. +ve along y axis")
                print("2. -ve along y axis")
                j = int(input("Enter the operation: "))
                if j not in [1, 2]:
                    print("Invalid")
                    return
                if j == 1:
                    y = ((x - c) ** 2) / (4 * a) + p
                    plt.plot(x, y)
                    plt.title("Parabola along +ve Y axis")
                    plt.show()
                if j == 2:
                    y = -((x - c) ** 2) / (4 * a) + p
                    plt.plot(x, y)
                    plt.title("Parabola along -ve Y axis")
                    plt.show()

    def plot(self):
        pass

    def handle_additional_info(self):
        choice = input("Do you want to calculate the tangent? (yes/no): ").lower()
        if choice == "yes":
            self.tangent()
        else:
            plt.legend()
            plt.title("Parabola")
            plt.show()

    def tangent(self):
        if (self.r==1):
            y1 = float(input("Enter the y-coordinate of the point for the tangent: "))
            x1 = self.a * (y1 - self.c) ** 2 + self.p  # Calculate the corresponding y-coordinate on the parabola
            slope = 2 * self.a * (y1 - self.c)  # Calculate the slope of the tangent line
            tangent_y = np.linspace(y1 - 2, y1 + 2, 100)
            tangent_x = slope * (tangent_y - y1) + x1

            # Retrieve the parabola coordinates
            y = np.linspace(-2, 10, 100)
            x = self.a * (y - self.c) ** 2 + self.p

            # Plot the parabola
            plt.plot(x, y, label="Parabola")

            # Plot the tangent line and tangent point on the parabola
            plt.plot(tangent_x, tangent_y, linestyle='--', label="Tangent Line")
            plt.plot(x1, y1, 'ro', label="Tangent Point")

            plt.legend()
            plt.title("Parabola with Tangent")
            plt.show()
        if (self.r==2):
            x1 = float(input("Enter the x-coordinate of the point for the tangent: "))
            y1 = self.a * (x1 - self.c) ** 2 + self.p  # Calculate the corresponding y-coordinate on the parabola
            slope = 2 * self.a * (x1 - self.c)  # Calculate the slope of the tangent line
            tangent_x = np.linspace(x1 - 2, x1 + 2, 100)
            tangent_y = slope * (tangent_x - x1) + y1

            # Retrieve the parabola coordinates
            x = np.linspace(-2, 10, 100)
            y = self.a * (x - self.c) ** 2 + self.p

            # Plot the parabola
            plt.plot(x, y, label="Parabola")

            # Plot the tangent line and tangent point on the parabola
            plt.plot(tangent_x, tangent_y, linestyle='--', label="Tangent Line")
            plt.plot(x1, y1, 'ro', label="Tangent Point")

            plt.legend()
            plt.title("Parabola with Tangent")
            plt.show()
            
class Ellipse(OperationHandler):
    def process(self):
        a = float(input("Enter the length of the semi-major axis (a): "))
        b = float(input("Enter the length of the semi-minor axis (b): "))
        h = float(input("Enter the x-coordinate of the center (h): "))
        k = float(input("Enter the y-coordinate of the center (k): "))
        angle = np.linspace(0, 2 * np.pi, 100)
        x = a * np.cos(angle) + h
        y = b * np.sin(angle) + k
        self.a = a  # Store 'a' as an instance variable
        self.b = b  # Store 'b' as an instance variable
        self.h = h  # Store 'h' as an instance variable
        self.k = k  # Store 'k' as an instance variable
        self.x_values = x
        self.y_values = y

    def plot(self):
        plt.plot(self.x_values, self.y_values)
        plt.title("Ellipse")
        plt.show()

    def handle_additional_info(self):
        choice = input("Do you want to calculate the tangent? (yes/no): ").lower()
        if choice == "yes":
            self.tangent()
        else:
            print("Tangent calculation skipped.")

    def tangent(self):
        x1 = float(input("Enter the x-coordinate of the point for the tangent: "))
        y1 = float(input("Enter the y-coordinate of the point for the tangent: "))
        h = self.h  # Retrieve 'h' from instance variable
        k = self.k  # Retrieve 'k' from instance variable
        a = self.a  # Retrieve 'a' from instance variable
        b = self.b  # Retrieve 'b' from instance variable
        
        # Check if the point is on the ellipse
        if ((x1 - h) ** 2 / a ** 2) + ((y1 - k) ** 2 / b ** 2) == 1:
            plt.plot(x1, y1, 'ro', label="Tangent Point")
            
            # Calculate the slope of the tangent at the given point
            slope = (-a ** 2 * (x1 - h)) / (b ** 2 * (y1 - k))
            
            if y1 - k >= 0:
                tangent_x = np.linspace(h - a, h + a, 100)
                tangent_y = slope * (tangent_x - h) + k
                plt.plot(tangent_x, tangent_y, linestyle='--', label="Tangent Line (along +ve Y axis)")
            else:
                tangent_x = np.linspace(h - a, h + a, 100)
                tangent_y = slope * (tangent_x - h) + k
                plt.plot(tangent_x, tangent_y, linestyle='--', label="Tangent Line (along -ve Y axis)")
            
            plt.legend()
            plt.title("Ellipse with Tangent")
            plt.show()
        else:
            print("The point is not on the ellipse.")

class Hyperbola(OperationHandler):
    def process(self):
        a = float(input("Enter the value of the semi-major axis (a): "))
        b = float(input("Enter the value of the semi-minor axis (b): "))
        h = float(input("Enter the x-coordinate of the center (h): "))
        k = float(input("Enter the y-coordinate of the center (k): "))
        angle = np.linspace(0, 2 * np.pi, 100)
        x = a / np.cos(angle) + h
        y = b * np.tan(angle) + k
        self.a = a  # Store 'a' as an instance variable
        self.b = b  # Store 'b' as an instance variable
        self.h = h  # Store 'h' as an instance variable
        self.k = k  # Store 'k' as an instance variable
        self.x_values = x
        self.y_values = y

    def plot(self):
        plt.plot(self.x_values, self.y_values, marker='o', markersize=1, linestyle='-')
        plt.title("Hyperbola")
        plt.show()

    def handle_additional_info(self):
        choice = input("Do you want to calculate the tangent? (yes/no): ").lower()
        if choice == "yes":
            self.tangent()
        else:
            print("Tangent calculation skipped.")

    def tangent(self):
        x1 = float(input("Enter the x-coordinate of the point for the tangent: "))
        y1 = float(input("Enter the y-coordinate of the point for the tangent: "))
        h = self.h  # Retrieve 'h' from instance variable
        k = self.k  # Retrieve 'k' from instance variable
        a = self.a  # Retrieve 'a' from instance variable
        b = self.b  # Retrieve 'b' from instance variable
        if x1 - h != 0 and (y1 - k) / (x1 - h) != 0:
            # Calculate the slope of the tangent at the given point
            slope = (a ** 2 * (x1 - h)) / (b ** 2 * (y1 - k))
            if x1 - h >= 0:
                plt.plot(np.linspace(h, x1 + 2, 20), slope * (np.linspace(h, x1 + 2, 20) - h) + k, linestyle='--', label="Tangent Line")
                plt.title("Hyperbola with Tangent (along +ve X axis)")
            else:
                plt.plot(np.linspace(x1 - 2, h, 20), slope * (np.linspace(x1 - 2, h, 20) - h) + k, linestyle='--', label="Tangent Line")
                plt.title("Hyperbola with Tangent (along -ve X axis)")
            plt.legend()
            plt.show()
        else:
            print("The point is not on the hyperbola.")



class Subtraction(OperationHandler):
    def process(self):
        q = int(input("Enter the number of inputs you want: "))
        a = []
        b = []
        v = 0
        f = 0
        r = 0
        for t in range(q):
            t = float(input("Enter the first element: "))
            a.append(t)
            r = r + t
        print(r)
        for u in range(q):
            u = float(input("Enter the second element: "))
            b.append(u)
            f = f + u
        print(f)
        for g, w in zip(a, b):
            q = float(g) - float(w)
            v = v + q
            print(q, ',', end="")
        print('\n', v)
        c = r - f
        print(c)

    def plot(self):
        # Add code to display the result of the Subtraction
        pass

class Addition(OperationHandler):
    def process(self):
        q = int(input("Enter the number of inputs you want: "))
        a = []
        b = []
        v = 0
        f = 0
        r = 0
        for t in range(q):
            t = float(input("Enter the first element: "))
            a.append(t)
            r = r + t
        print(r)
        for u in range(q):
            u = float(input("Enter the second element: "))
            b.append(u)
            f = f + u
        print(f)
        for g, w in zip(a, b):
            q = float(g) + float(w)
            v = v + q
            print(q, ',', end="")
        print('\n', v)
        c = r + f
        print(c)

    def plot(self):
        # Add code to display the result of the Addition
        pass

class Multiplication(OperationHandler):
    def process(self):
        q = int(input("Enter the number of inputs you want: "))
        a = []
        b = []
        v = 0
        f = 0
        r = 0
        for t in range(q):
            t = float(input("Enter the first element: "))
            a.append(t)
            r = r + t
        print(r)
        for u in range(q):
            u = float(input("Enter the second element: "))
            b.append(u)
            f = f + u
        print(f)
        for g, w in zip(a, b):
            q = float(g) * float(w)
            v = v + q
            print(q, ',', end="")
        print('\n', v)
        c = r * f
        print(c)

    def plot(self):
        # Add code to display the result of the Multiplication
        pass

class Division(OperationHandler):
    def process(self):
        q = int(input("Enter the number of inputs you want: "))
        a = []
        b = []
        v = 0
        f = 0
        r = 0
        for t in range(q):
            t = float(input("Enter the first element: "))
            a.append(t)
            r = r + t
        print(r)
        for u in range(q):
            u = float(input("Enter the second element: "))
            b.append(u)
            f = f + u
        print(f)
        for g, w in zip(a, b):
            if w == 0:
                print("Division by zero is not allowed")
                return
            q = float(g) / float(w)
            v = v + q
            print(q, ',', end="")
        print('\n', v)
        if f == 0:
            print("Division by zero is not allowed")
            return
        c = r / f
        print(c)

    def plot(self):
        # Add code to display the result of the Division
        pass

# Create a dictionary mapping operation numbers to their respective classes
operation_classes = {
    1: SlopeForm,
    2: PointForm,
    3: Circle,
    4: Triangle,
    5: Parabola,
    6: Ellipse,  # Add Ellipse class
    7: Hyperbola,  # Add Hyperbola class
    8: Subtraction,
    9: Addition,
    10: Multiplication,
    11: Division,
}

# Display menu options
while True:
        # Display menu options
        for operation_num, operation_class in operation_classes.items():
            print(f"{operation_num} for {operation_class.__name__}")

        # Get user's choice
        operation_num = int(input("Enter the operation: "))

        # Check if the chosen operation exists
        if operation_num in operation_classes:
            operation = operation_classes[operation_num]()
            operation.process()
            operation.plot()
            operation.handle_additional_info()
        else:
            print("Invalid operation number")

        # Ask the user if they want to continue
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != "yes":
            break


