student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
height = round(sum(student_heights) / len(student_heights))
print(height)


# Both of run



student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height # total_height = total_height + height
print(f"Total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1 # her döndüğünde 1 ekleyecek, listenin sonuna kadar.(Yani 5 farklı öğrencinin boy uzunluğunu girersem 5. öğrenciye geldiğinde duracak, döngüyü bitirecek. 6 öğrenci olsaydı 6'da, 123 öğrenci olsaydı 123'de duracaktı!)
print(f"Number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height)















