
student1 = {"Student": "Alice Jonson", "Age": 20, "Email": "alice@school.edu", "grades": {"math":85, "science":92, "english":78}}


print("Initial student records:\n ----------------------------")
print("student: ",student1["Student"])
print("age: ",student1["Age"])
print("email: ",student1["Email"])
print("grades: ",student1["grades"])
avarage1 = sum(student1["grades"].values()) / len(student1["grades"])
print("avarage: ",avarage1)

student2 = {"Student": "Carol Davic", "Age": 21, "Email": "carol@school.edu", "grades": {"math":95, "science":89, "english":88}}

print("Initial student records:\n ----------------------------")
print("student: ",student2["Student"])
print("age: ",student2["Age"])
print("email: ",student2["Email"])
print(f"grades: math: {student2["grades"]["math"]}, science: {student2["grades"]["science"]}, english: {student2["grades"]["english"]}")
avarage2 = sum(student2["grades"].values()) / len(student2["grades"])
print(f"avarage: {avarage2:.2f}")

student3 = {"Student": "Bob Smith", "Age": 19, "Email": "bob@school.edu", "grades": {"math":78, "science":85, "english":88, "history":82}}


print("Initial student records:\n ----------------------------")
print("student: ",student3["Student"])
print("age: ",student3["Age"])
print("email: ",student3["Email"])
print(f"grades: math: {student3["grades"]["math"]}, science: {student3["grades"]["science"]}, english: {student3["grades"]["english"]}, history: {student3["grades"]["history"]}")
avarage3 = sum(student3["grades"].values()) / len(student3["grades"])
print(f"avarage: {avarage3:.2f}")

print("top performing student:")
print("----------------------------")
if avarage1 > avarage2 and avarage1 > avarage3:
    print(f"{student1['Student']} with an average of {avarage1:.2f}")
elif avarage2 > avarage1 and avarage2 > avarage3:
    print(f"{student2['Student']} with an average of {avarage2:.2f}")
else:
    print(f"{student3['Student']} with an average of {avarage3:.2f}")

print("avarages:")
print("----------------------------")

print("math: ", (student1["grades"]["math"] + student2["grades"]["math"] + student3["grades"]["math"]) / 3 )
print("science: ", (student1["grades"]["science"] + student2["grades"]["science"] + student3["grades"]["science"]) / 3 )
print("english: ", (student1["grades"]["english"] + student2["grades"]["english"] + student3["grades"]["english"]) / 3 )


update_student_record = input("Do you want to update a student record? (yes/no): ").strip().lower()
if update_student_record == "yes":
    student_name = input("Enter the student's name to update: ").strip()
    if student_name == student1["Student"]:
        field_to_update = input("Which field do you want to update? (Age/Email/grades): ").strip().lower()
        if field_to_update == "age":
            new_age = int(input("Enter the new age: ").strip())
            student1["Age"] = new_age
        elif field_to_update == "email":
            new_email = input("Enter the new email: ").strip()
            student1["Email"] = new_email
        elif field_to_update == "grades":
            subject = input("Enter the subject to update (math/science/english/history): ").strip().lower()
            if subject in student1["grades"]:
                new_grade = int(input(f"Enter the new grade for {subject}: ").strip())
                student1["grades"][subject] = new_grade
            else:
                print(f"Subject {subject} not found in records.")
        else:
            print(f"Field {field_to_update} not recognized.")
    elif student_name == student2["Student"]:
        field_to_update = input("Which field do you want to update? (Age/Email/grades): ").strip().lower()
        if field_to_update == "age":
            new_age = int(input("Enter the new age: ").strip())
            student2["Age"] = new_age
        elif field_to_update == "email":
            new_email = input("Enter the new email: ").strip()
            student2["Email"] = new_email
        elif field_to_update == "grades":
            subject = input("Enter the subject to update (math/science/english/history): ").strip().lower()
            if subject in student2["grades"]:
                new_grade = int(input(f"Enter the new grade for {subject}: ").strip())
                student2["grades"][subject] = new_grade
            else:
                print(f"Subject {subject} not found in records.")
        else:
            print(f"Field {field_to_update} not recognized.")
    elif student_name == student3["Student"]:
        field_to_update = input("Which field do you want to update? (Age/Email/grades): ").strip().lower()
        if field_to_update == "age":
            new_age = int(input("Enter the new age: ").strip())
            student3["Age"] = new_age
        elif field_to_update == "email":
            new_email = input("Enter the new email: ").strip()
            student3["Email"] = new_email
        elif field_to_update == "grades":
            subject = input("Enter the subject to update (math/science/english/history): ").strip().lower()
            if subject in student3["grades"]:
                new_grade = int(input(f"Enter the new grade for {subject}: ").strip())
                student3["grades"][subject] = new_grade
            else:
                print(f"Subject {subject} not found in records.")
        else:
            print(f"Field {field_to_update} not recognized.")
    else:
        print(f"Student {student_name} not found.")

        
    print("Record updated successfully.")
    print("Updated student records:\n ----------------------------")
    print("student: ",student1["Student"])
    print("age: ",student1["Age"])
    print("email: ",student1["Email"])
    print("grades: ",student1["grades"])
    avarage1 = sum(student1["grades"].values()) / len(student1["grades"])
    print("avarage: ",avarage1)
    print("student: ",student2["Student"])
    print("age: ",student2["Age"])
    print("email: ",student2["Email"])
    print(f"grades: math: {student2["grades"]["math"]}, science: {student2["grades"]["science"]}, english: {student2["grades"]["english"]}")
    avarage2 = sum(student2["grades"].values()) / len(student2["grades"])
    print(f"avarage: {avarage2:.2f}")
    print("student: ",student3["Student"])
    print("age: ",student3["Age"])
    print("email: ",student3["Email"])
    print(f"grades: math: {student3["grades"]["math"]}, science: {student3["grades"]["science"]}, english: {student3["grades"]["english"]}, history: {student3["grades"]["history"]}")
    avarage3 = sum(student3["grades"].values()) / len(student3["grades"])
    print(f"avarage: {avarage3:.2f}")
else:
    print("No updates made to student records.")    

print("top performing student:")
print("----------------------------")
if avarage1 > avarage2 and avarage1 > avarage3:
    print(f"{student1['Student']} with an average of {avarage1:.2f}")
elif avarage2 > avarage1 and avarage2 > avarage3:
    print(f"{student2['Student']} with an average of {avarage2:.2f}")
else:
    print(f"{student3['Student']} with an average of {avarage3:.2f}")

print("\nUpdated student\n----------------------------")
if student_name == student1["Student"]:
    print("student: ",student1["Student"])
    print("age: ",student1["Age"])
    print("email: ",student1["Email"])
    print("grades: ",student1["grades"])
    avarage1 = sum(student1["grades"].values()) / len(student1["grades"])
    print("avarage: ",avarage1)
elif student_name == student2["Student"]:
    print("student: ",student1["Student"])
    print("age: ",student2["Age"])
    print("email: ",student2["Email"])
    print("grades: ",student2["grades"])
    avarage1 = sum(student2["grades"].values()) / len(student2["grades"])
elif student_name == student3["Student"]:
    print("student: ",student3["Student"])
    print("age: ",student3["Age"])
    print("email: ",student3["Email"])
    print("grades: ",student3["grades"])
    avarage3 = sum(student3["grades"].values()) / len(student3["grades"])
    print("avarage: ",avarage3) 