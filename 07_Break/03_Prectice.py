# 1. write a program with five examples of break statements.
'''Example 1'''

for i in range(1,10):
    if i == 5:
        break
    print(i)
'''Example 2 '''


for i in range(1,99):
    # print(i)
    if i == 80:
        break
    print(i)


'''Exsmple 3'''

for i in range(1,100):
    if i == 50:
        break
    print(i)

'''Example 4'''

for i in range (1,20):
    if i > 10:
        break
    print(i)

'''Example 5'''
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Number Found")
        break
    print(num)

# 1. write a program with five examples of Continue statements.


'''Example 1'''
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

'''Example 2'''

i = 0

while i < 10:
    i += 1

    if i == 5:
        continue

    print(i)
'''Example 3'''

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

'''Example 4'''
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

'''Example 5'''
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
