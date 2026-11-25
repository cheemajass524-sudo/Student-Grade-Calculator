print("Student Grade Calculator")

#get the marks for each subject
m1 = float(input("marks for subject1: "))
m2 = float(input("marks for subject2: "))
m3 = float(input("marks for subject3: "))

#calculate the average
average = (m1 + m2 + m3)/3

print("Average Grade: ", average)

if average >= 90:
	grade = "A"
elif average >=80:
	grade = "B"
elif average >=70:
	grade = "C"
elif average >= 60:
	grade = "D"
else:
	grade = "F"

print("Letter Grade: ", grade)

