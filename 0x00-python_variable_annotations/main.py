#!/usr/bin/env python3

# matrix = []

# for i in range(5):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(j)
# for k in matrix:
#     print(k)

# matrix= [[j for j in range(5)]  for i in range(5) ]
# for k in matrix:
#     print(k)

n = int(input("Enter a number: "))

matrix =[]
for i in range(n):
    matrix.append([i])
    temp_list = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp_list.append(1)
        print(temp_list)