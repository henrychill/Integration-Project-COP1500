# Integration Project Sprint 2
# A calculator with selectable operations
# Henry Hill
# Tylor Krafjack (input on functionality)
import math


# definition of functions
def circumferencecircle(radius):
    circ = math.pi * 2 * radius
    print("The approximate circumference of the circle with radius:", radius, "=", format(circ, ".2f"))


def areacircle(radius):
    area = math.pi * radius ** 2
    print("The approximate area of the circle with radius:", radius, "=", format(area, ".2f"))


def volumesphere(radius):
    volume = 4 / 3 * (math.pi * radius ** 3)
    print("The approximate volume of the sphere with the radius", radius, "=", format(volume, ".2f"))


# definition of main
def main():

    # greeting messages and prompting user
    nameinput = input("Good day to you, user! What's your name? ")
    userprompt = input(
        "Great! Nice to meet you " + nameinput + "! If you wish to calculate with the program, "
                                                 "type 'yes', if not, type anything else: ")
    # goodbye message and insulting user
    if not userprompt == 'yes':
        print("Wow. Really fun at parties, aren't you", nameinput, end=". ")

    # query about calculator choice
    if userprompt == 'yes':
        calculatorchoice = input(
            "Great! If you want to select the geometry calculator, type 'geo', "
            "if you'd like to select the arithmetic calculator, type 'arit' ")

        # geometry calculator block
        if calculatorchoice == 'geo':
            while True:
                print(
                    "Geometry, great choice. Select which function you'd like to use:")

                # function options
                for choicerange in range(1, 4):
                    vols = "Volume of a Sphere"
                    arec = "Area of a Circle"
                    circc = "Circumference of a Circle"
                    strlist = [arec, circc, vols]

                    print(choicerange, ".", strlist[choicerange - 1])

                # user choice of function input
                geochoice = input(": ")

                # function calls based on "geochoice" input
                if geochoice == '1':
                    r = int(input("Enter your radius: "))
                    areacircle(r)
                elif geochoice == '2':
                    r = int(input("Enter your radius: "))
                    circumferencecircle(r)
                elif geochoice == '3':
                    r = int(input("Enter your radius: "))
                    volumesphere(r)
                elif geochoice != ('1' or '2' or '3'):
                    print("Invalid Input")
                # prompting the user for another geometry problem
                nextcalculationgeo = input(
                    "If you want to solve another problem using the program, type anything. If no, type 'no': ")
                if nextcalculationgeo == "no":
                    break

        # arithmetic calculator block
        # calculation options display
        elif calculatorchoice == 'arit':
            print("Sounds great! Let's crunch some numbers. Select mathematical operation. ")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponent")
            print("6. Floor Division")
            print("7. Modulus (Finding Remainder)")

            while True:

                # operator AND number input
                ans = input("Enter here: 1, 2, 3, 4, 5, 6, or 7 ")
                if ans in ('1', '2', '3', '4', '5', '6', '7'):
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))

                    # calculation and mathematical display of operations and answer
                    if ans == '1':
                        print(a, "+", b, "=", a + b, sep="  ")

                    elif ans == '2':
                        print(a, "-", b, "=", a - b, sep="  ")

                    elif ans == '3':
                        print(a, "*", b, "=", a * b, sep="  ")

                    elif ans == '4':
                        print(a, "/", b, "=", a / b, sep="  ")

                    elif ans == '5':
                        print(a, "^", b, "=", a ** b, sep="  ")

                    elif ans == '6':
                        print(a, "//", b, "=", a // b, "I'm suprised you found a use for this.", sep="  ")

                    elif ans == '7':
                        print(a, "%", b, "=", a % b, "Again, I'm suprised you needed this.", sep="  ")

                    # prompting the user to answer another problem
                    nextcalculationarit = input(
                        "If you want to solve another problem using the program, press 1. If no, press 0: ")
                    if nextcalculationarit == "0":
                        break

                # allowing the user to re-enter the selection for operation
                else:
                    print("Not Valid Input")


# **** MAIN *****
main()
