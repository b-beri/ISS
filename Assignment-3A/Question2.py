import os


def display_details(i, rank):
    if i not in d.keys():
        print("No Student with this Roll Number.")
        return
    print("Student Details =>")
    print("Name:", d[i][0])
    print("Roll Number:", i)
    print("Marks -> \tMaths:", d[i][1][0], "; CS:",
          d[i][1][1], "; Science:", d[i][1][2])
    print("Mean Marks:", d[i][2])
    print("Median Marks:", d[i][3])
    print("Rank in Class:", rank.index(d[i][1][3])+1)
    print("----------------")


# MAIN CODE
d = dict()  # FORMAT - [ROLL : [NAME,[MATH,CS,SCIENCE,TOTAL],MEAN,MEDIAN]]
rank = list()
n = int(input("Enter number of Students -> "))
for i in range(n):
    print("Student", i+1, "Details =>")
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name of Student: ")
    marks = [int(input("Maths: ")), int(
        input("CS: ")), int(input("Science: "))]
    marks += [(marks[0]+marks[1]+marks[2]), ]

    avg = (marks[3])/3
    median_list = list(marks)
    median_list.sort()
    rank += [marks[3], ]

    d[roll] = [name, marks, avg, median_list[1]]

rank.sort(reverse=True)

# Clearing the Screen
# posix is os name for linux or mac
if(os.name == 'posix'):
    os.system('clear')
# else screen will be cleared for windows
else:
    os.system('cls')

print("HELLO")

while(True):
    print("\nMENU (Enter Choice Number below) ->\n1. Display list of users")
    print("2. Display student details from Roll number")
    print("3. Display student details from Name")
    print("0. Exit")
    choice = int(input("-> "))
    if choice == 0:
        print("BYE BYE !!")
        break
    elif choice == 1:
        print("Roll Number - Name")
        for i in d:
            print(i, d[i][0], sep="\t- ")
        print("----------------")

    elif choice == 2:
        i = int(input("Enter Roll Number: "))
        display_details(i, rank)

    elif choice == 3:
        name = input("Enter Name: ")
        found = False
        for i in d.keys():
            if d[i][0].lower() == name.lower():
                display_details(i, rank)
                found = True
                break
        if not found:
            print("Student not present with this Name.")
