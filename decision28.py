
a = [10, -2, 34, 45, -5, 0, -5, 14]
    
next = []
for item in a:
    if item > 0:
        next.append(1)
    elif item < 0:
        next.append(-1)
    else:
        next.append(0)

print(a)
print(next)





#Напишите функцию где дан список целых чисел. Заменить отрицательные на -1,
#положительные - на число 1, ноль оставить без изменений.