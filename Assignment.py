studentNames = ["Sandra", "Patricia", "Phionah", "Anitah"] 
studentMarks = [80,56,78,90]
# QUESTIONS
#a) Print a list that excludes the first and the last student.
#SOLUTION
excluded_list = studentNames[1:-1]
print(excluded_list)

#b) Print a list from Patricia,Faith,Phiona and Anitah.
#SOLUTION
selected_list = studentNames[1:]
print(selected_list)


#c) Add Masha to the 4th position
#SOLUTION
studentNames.insert(3, "Masha")
print(studentNames)

#d) Update the name Phionah to Aladina
#SOLUTION
studentNames[2] = "Aladina"
print(studentNames)

#e) Display the length of the students' list
length_of_students_list = len(studentNames)
print(length_of_students_list)

#f) Print all the students' names using a for loop.
#SOLUTION
for name in studentNames:
    print(name)

#g) Calculate the total mark for the students' mark  variable.
total_mark = sum(studentMarks)
print(total_mark)


