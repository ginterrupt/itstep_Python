student1 = ("Alice Jonson", 12345, 85, 92, 78)
student2 = ("Bruce Wane", 12346, 88, 98, 82)
student3 = ("David Webb", 12347, 85, 89, 98)

print("Student Name: ",student1[0],"\nStudent ID: ", student1[1])
print("Student Name: ",student2[0],"\nStudent ID: ", student2[1])
print("Student Name: ",student3[0],"\nStudent ID: ", student3[1])

average1 = (student1[2] + student1[3] + student1[4]) / 3
print("Average Score of", student1[0], f"is: {average1:.2f}", )

average2 = (student2[2] + student2[3] + student2[4]) / 3
print("Average Score of", student2[0], f"is: {average2:.2f}", )
average3 = (student3[2] + student3[3] + student3[4]) / 3
print("Average Score of", student3[0], f"is: {average2:.2f}", ) 

all_students = (student1, student2, student3)
print(all_students)

name, student_id, *scores = student2
print("Unpacked Name:", name)
print("Unpacked ID:", student_id)


student1_updated = (student1[0], student1[1], 100, student1[3], student1[4])
print("Original student1:", student1)
print("Updated student1:", student1_updated)

average1_updated = (student1_updated[2] + student1_updated[3] + student1_updated[4]) / 3
print("Average Score of", student1_updated[0], f"is: {average1_updated:.2f}")

print("Total number of students:", len(all_students))

print("Is 12345 ID in student one's ID? ",12345 in student1)

