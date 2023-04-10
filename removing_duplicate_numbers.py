numbers = [1,1,2,3,55,6,78,3,25,8,54,3,2,5,43,4]
new =[]
for number in numbers:
    if number not in new:
        new.append(number)
print(new)            