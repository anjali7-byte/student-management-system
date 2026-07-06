# studenr management system
student={}
def calculate_grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"
def add_student():
        roll=input("enter roll number:")
        if roll in student:
            print("student alredy exist!")
            return
        name=input("enter the student name:")
        marks=[]
        for i in range(3):
            mark=float(input(f"enter marks of the subject(i+1):"))
            marks.append(mark)
            total=sum(marks)
            average=total/len(marks)
            grade=calculate_grade(average)
            student[roll]={
                "name":name,
                "marks":marks,
                "total":total,
                "average":average,
                "grade":grade
                }
            print("student record dded succesfully!")
def search_student():
            roll=input("enter roll number to search:")
            if roll in student:
                s=student[roll]
                print("\n student details")
                print("------------------")
                print("roll number:",roll)
                print("name:",s["name"])
                print("total:",s["total"])
                print("average:",round(s["average"],2))
                print("grade:",s["grade"])
            else:
                print("student not found")
def display_student():
            if not student:
                print("no student record found")
                return
            print("\n all student records")
            print("-"*60)
            for roll ,s in student.items():
                print("roll number:",roll)
                print("name:",s["name"])
                print("total:",s["total"])
                print("average:",round(s["average"],2))
                print("grade:",s["grade"])
                print("-"*60)
#main menu
while True:
    print("\n======student record management system======")
    print("1.add student record")
    print("2.search student details")
    print("3.Display all student details")
    print("4.exit")
    choice=input("enter your choice:")
    if choice=="1":
       add_student()
    elif choice=="2":
        search_student()
    elif choice=="3":
        display_student()
    elif choice=="4":
       print("thank you!")
       break
    else:
        print("invalid choice please try again")
