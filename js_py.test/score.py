A = [70, 60, 55, 75, 95, 90, 80, 70, 85, 100]

sum = 0
for score in A:
    sum += score

avg = sum/len(A)
print("평균 :", avg)