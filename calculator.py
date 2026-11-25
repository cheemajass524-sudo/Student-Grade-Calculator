print("Student Result Calculator")

#get the marks for each subject
m1 = float(input("marks for subject1: "))
m2 = float(input("marks for subject2: "))
m3 = float(input("marks for subject3: "))

#validation input for the marks
if not(0<=m1<=100 and 0<=m2<=100 and 0<=m3<=100):
	print("Invalid Input: The grade must be between 0 and 100)
	exit()

#calculate the average
average = (m1 + m2 + m3)/3

print("Average Grade: ",round(average,2))

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

if grade >=60:
	print("Status: Pass")
else:
	print(Status: Fail")

