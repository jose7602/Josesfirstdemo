## Jose Mestre

grades = int(input("How many grades would you like to input in?: "))

grades_list = []

for i in range(0,grades):
    grade = int(input("Enter grade: "))
    grades_list.append(grade)
avg=sum(grades_list)/grades
print("Your average grade",round(avg,2))

if avg > 90 and avg <= 100:
    print ("You have an A!")
elif avg > 80 and avg <= 89:
    print ("You have a B!")
elif avg > 70 and avg <= 79:
    print ("You have a C!")
elif avg > 60 and avg <= 69:
    print ("You have a D!")
elif avg < 59 and avg > 0:
    print ("You have a U")
    
