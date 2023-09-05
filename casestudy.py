#Nooreddin Hellalat
#Main case study
#App accepts student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
lastname = input("Enter students lastname or enter ZZZ to end: ")
while lastname != "ZZZ":
    
    firstname = input("Enter Student First Name: ")
    gpa = float(input("Enter Student GPA: "))
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(firstname, lastname))
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname)) 
    lastname = input("\nEnter Student Last Name: ")