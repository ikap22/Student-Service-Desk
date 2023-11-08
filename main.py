import pandas as pd
import matplotlib.pyplot as plt

class Student:
    def __init__(self, SID, firstName, lastName, classes):
        self.SID = SID
        self.firstName = firstName
        self.lastName = lastName
        self.classes = classes

    def getSID(self):
        return self.SID

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getClasses(self):
        return self.classes

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def __str__(self):
        return f"{self.lastName}, {self.firstName} (SID={self.SID})\nClasses:\n\t" + "\n\t".join(self.classes)

nextSID = 22
studentInfo = {}
studentInfo[21] = Student(21, "Zog", "TheDestroyer", ["BIT 143", "MATH 411", "ENG 120"])
studentInfo[20] = Student(20, "Mary", "Sue", ["BIT 142", "MATH 142", "ENG 100"])
studentInfo[1] = Student(1, "Joe", "Bloggs", ["BIT 115", "MATH 141", "ENG 101"])

def plot_student_distribution(data):
    student_data = []
    for student in data.values():
        student_data.append({
            'SID': student.getSID(),
            'FirstName': student.getFirstName(),
            'LastName': student.getLastName(),
            'NumClasses': len(student.getClasses())
        })
    df = pd.DataFrame(student_data)
    plt.bar(df['SID'], df['NumClasses'])
    plt.xlabel('Student ID')
    plt.ylabel('Number of Classes')
    plt.title('Student Class Distribution')
    plt.show()

choice = 'L'
while choice != 'q':
    print("\nWhat would you like to do next? ")
    print("F - Find a specific student")
    print("L - List all the students (for debugging purposes)")
    print("A - Add a new student")
    print("D - Delete an existing student")
    print("M - Modify an existing student")
    print("Q - Quit (exit) the program")
    choice = input("What is your choice?\n(type in the letter & then the enter/return key) ").strip().lower()
    print()
    if choice == 'f':
        print("Find a student (based on their ID number):\n")
        SIDnum = int(input("What is the ID number of the student to find? "))
        print()
        student = studentInfo.get(SIDnum)
        if student != None:
            print(f"{student.getLastName()}, {student.getFirstName()} (SID={student.getSID()})\nClasses:")
            for className in student.getClasses():
                print("\t" + className)
        else:
            studentExists = False
            for s in studentInfo.values():
                if s.getSID() == SIDnum:
                    studentExists = True
                    break
            if not studentExists:
                print("Didn't find a student with ID #" + str(SIDnum))
    elif choice == 'l':
        print("The following students are registered:")
        for stu in studentInfo.values():
            print(stu)
        plot_student_distribution(studentInfo)  # Added data visualization
    elif choice == 'a':
        print("Adding a new student\n")
        print("Please provide the following information:")
        firstName = input("Student's first name? ")
        lastName = input("Student's last name? ")
        newClasses = []
        className = None
        print("Type the name of class, or leave empty to stop. Press enter/return regardless")
        while True:
            className = input().strip()
            if className == "":
                break
            newClasses.append(className)
        newSID = nextSID
        nextSID += 1
        newStudent = Student(newSID, firstName, lastName, newClasses)
        studentInfo[newSID] = newStudent
        print("\nNew student added successfully!")
        print("Student ID:", newSID)
        print("Name:", firstName, lastName)
        print("Classes:", newClasses)
    elif choice == 'd':
        print("Deleting an existing student\n")
        deleteSID = int(input("What is the ID number of the student to delete? "))
        deleteStudent = studentInfo.pop(deleteSID, None)
        if deleteStudent != None:
            print("Student account found and removed from the system!")
        else:
            print("Didn't find a student with ID #" + str(deleteSID))
    elif choice == 'm':
        print("Modifying an existing student\n")
        modifySID = int(input("What is the ID number of the student to modify? "))
        modifyStudent = studentInfo.get(modifySID)
        if modifyStudent != None:
            print("Student account found!")
            newFirstName = input("Student's first name (" + modifyStudent.getFirstName() + "): ")
            if newFirstName != "":
                modifyStudent.setFirstName(newFirstName)
            newLastName = input("Student's last name (" + modifyStudent.getLastName() + "): ")
            if newLastName != "":
                modifyStudent.setLastName(newLastName)
            print("Updating class list")
            currentClasses = modifyStudent.getClasses()
            print("Here are the current classes:", currentClasses)
            print("This program will go through all the current classes.")
            classIterator = iter(currentClasses)
            while True:
                try:
                    nameofClass = next(classIterator)
                    option = input(nameofClass + "\nType d<enter/return> to remove, or just <enter/return> to keep: ").strip()
                    if option.lower() == "d":
                        classIterator.remove()
                        print("Removing", nameofClass)
                    else:
                        print("Keeping", nameofClass)
                except StopIteration:
                    break
            print("Type the name of the class you'd like to add, or leave empty to stop. Press enter/return regardless")
            while True:
                newClassName = input().strip()
                if newClassName == "":
                    break
                currentClasses.append(newClassName)
            print("Here's the student's new, updated info:", modifyStudent)
        else:
            print("Didn't find a student with ID #" + str(modifySID))
    elif choice == 'q':
        print("Thanks for using the program - goodbye!\n")
        break
    else:
        print("Sorry, but I didn't recognize the option", choice)
