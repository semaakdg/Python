import random

randomInteger = random.randint(1,100)
print(randomInteger)

randomFloat = random.random()
print(randomFloat)

randomFloat = random.random() * 5 # 0 ile 5 arasında random ondalıklı sayı üretecek
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}") # her çalıştırdığımda random love score verecek
