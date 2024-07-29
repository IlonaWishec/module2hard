import random

list_random = random.randrange(3, 21)
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
print(f'Случайное число: {list_random}')
for i in list_:
    for j in range(i + 1, 21):
        if list_random % (i + j) == 0:
            result.append(i)
            result.append(j)
print(result)