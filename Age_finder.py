print ("\n\t\t\t\t\t!!!!!!!!!! Welcome to age finder game !!!!!!!!!!\t\t\t\t\t ")

print ("\nWhat you want to chek\n\t1.To check when you will your age is 100 year\n\t2.Check your age at particular year")

choise = input("Enter the number what you want to check : ")
presentYear  =  2021
if choise == "1":
    age = input("Enter your age or your Birthday year : ")
    if int(age) > presentYear:
        print("You are not born yet but ")
    if len(age) == 4 :
        age100 = int(age) + 100
        print (f"Your age will 100 year at year {age100}")

    elif len(age) > 4 :
        print ("Invalid age or age year")

    elif 0 < len(age) < 4 :
        if int(age) > 150:
            print ("You are the oldest person who play this find age game")
        elif int(age) == 150:
            lucky = presentYear - 50
            print (f'You were 100 year old at {lucky}')
        elif int(age) < 100:
            findYear = 100 - int(age)
            yearIs = findYear + presentYear
            print (f"You will 100 year at year {yearIs}")


elif choise == "2":
    age = input("Enter you age or Birthday year : ")
    if int(age) > presentYear:
        print("You are not born yet ")
    ageYear = input("In which year you want to check you age : ")
    if len(age) == 4 and int(ageYear) >= presentYear:
        presentAge = presentYear - int(age)
        remainingAge = int(ageYear) - presentYear
        Age = presentAge + remainingAge
        print (f"Your age in year {ageYear} is {Age}")

    elif len(age) > 4:
        print ("Invalid age or age year")

    elif 0 < len(age) == 4 and int(ageYear) < presentYear:
        print ("You were not born when you want to check")

    elif 0 < len(age) < 4:
        Age = (int(ageYear) - presentYear) + int(age)
        print  (f"Your age in year {ageYear} is {Age}")

else:
    print ("Invalid Syntax")
