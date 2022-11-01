# Integration Project Sprint 1
# A calculator with selectable operations
# Henry Hill
# Tylor Krafjack (input on functionality)

#greeting message
name_input=input("Good day to you, user! What's your name? ")

#prompting the user
user_prompt=input("Great! Nice to meet you "+name_input+"! If you wish to continue with the program, press 1. If no, press 0: ")
user_prompt_int=int(user_prompt)
if user_prompt_int == 0:
    print("Wow. Really fun at parties, aren't you",name_input, end=". :(")
    
#intial operation query
if user_prompt_int > 0:
    print("Sounds great! Let's crunch some numbers. Select mathematical operation. ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Floor Division")
    print("7. Modulus (Finding Remainder)")

#while loop for allowing the user to do multiple calculations
while True:

#operator AND number input
    ans=input("Enter here: 1, 2, 3, 4, 5, 6, or 7 ")
    if ans in ('1','2','3','4','5','6','7'):
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))
        
#calculation and mathematical display of operations and answer
        if ans == '1':
             print(a,"+",b, "=", a+b,sep="  ")

        elif ans == '2':
            print(a,"-",b, "=", a-b,sep="  ")

        elif ans == '3':
            print(a,"*",b, "=", a*b,sep="  ")

        elif ans == '4':
            print(a,"/",b, "=", a/b,sep="  ")

        elif ans == '5':
            print(a,"^",b, "=", a**b,sep="  ")

        elif ans == '6':
            print(a,"//",b, "=", a//b, "I'm suprised you found a use for this.",sep="  ")

        elif ans == '7':
            print(a,"%",b, "=", a%b, "Again, I'm suprised you needed this.",sep="  ")

#prompting the user to answer another problem
        next_calculation = input("If you want to solve another problem using the program, press 1. If no, press 0: ")
        if next_calculation == "0":
            break
        
#allowing the user to re-enter the selection for operation
    else:
        print("Not Valid Input")
        
