count = 0
sumnum = 0

print("before", count, sumnum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sumnum = sumnum + value
    print(count, sumnum, value)
print("after", count, sumnum, sumnum / count)