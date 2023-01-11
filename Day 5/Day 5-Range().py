"""
#For Loop with Range
for number in range(1, 11): # 10'u da dahil edebilmek için 1 to 11 yazdıkk.
    print(number)
"""
total = 0
for number in range(2, 101, 2): # 1 ile 100 arasındaki (1 ile 100 dahil) sayıların toplamını bulmak için..
    total += number
    print(number)
print(total)

#both of run


total = 0
for number in range(2, 101):
    if number % 2 == 0:
        total += number
print(total)





