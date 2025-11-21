def howManyMissing(orderLine):
    minLine = min(orderLine)
    maxLine = max(orderLine)
    missing = 0
    for i in range(minLine, maxLine + 1):
        if i not in orderLine:
            missing += 1
    return missing

output = 4
print(howManyMissing([1, 2, 3, 8, 9])==output)
# The numbers missing from this line are 4, 5, 6, and 7.
# 4 numbers are missing.
output = 1
print(howManyMissing([1, 3])==output)

output = 2
print(howManyMissing([7, 10, 11, 12])==output)

output = 5
print(howManyMissing([1, 3, 5, 7, 9, 11])==output)

output = 0
print(howManyMissing([5, 6, 7, 8])==output)