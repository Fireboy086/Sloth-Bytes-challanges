import time

def is_happy_year(year):
    year_str = str(year)
    return len(year_str) == len(set(year_str))


def next_happy(current):
    print(f"finding next happy year after =>{current}<=")
    current = int(current) if isinstance(current, str) else current
    year = current 
    while True:
        if is_happy_year(year):
            return year
        year += 1

#This is really un optimized and can be extremely slof for large numbers but it works
#===============TESTS===============
import random
start_time = time.time()
num = 100000
numbers = [random.randint(1,20000) for _ in range(num)]
corrects = 0
incorrects = 0
for i in numbers:
    if is_happy_year(next_happy(i)):
        corrects +=1
    else:
        incorrects +=1
        print(f"year{i}, next_happy: {next_happy(i)}")


end_time = time.time()
execution_time = end_time - start_time
print("=============================================================")
print(f"   |\\\|Happy years count: {corrects},  Sad Years count: {incorrects}|//|")
print("=============================================================")
print(f"\n\n found solutions to {num} years after {execution_time}s")