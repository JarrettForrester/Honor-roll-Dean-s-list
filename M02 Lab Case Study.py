#Jarrett Forrester
#Lab Case Study Dean's list or Honor roll
#In this code, the user will start the program and be asked to enter their last name and first name. The program will then ask for the user to enter their gpa. 
#The program will then decide wether the users gpa will put them on the deans list or the honor roll. Then user can continue to input as many names and gpa's as possible until they enter ZZZ to exit.
while True:
    last_name = input("Enter last name: ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter first name: ")
    gpa = float(input("Enter GPA: "))
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")

        