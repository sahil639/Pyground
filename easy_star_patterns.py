
# #square
n = 5
for i in range(n):
    for j in range(n):
       print("*", end=" ")
    print()

# #sincreasing triangle
for i in range(n):
    for j in range(i+1):
       print("*", end=" ")
    print()

# #decreaing traingle
for i in range(n):
    for j in range(i, n):
       print("*", end=" ")
    print()

# # right side of triangle
for i in range(n):
     for j in range(i, n):
         print('', end=" ")
     for j in range(i, n):
       print("*", end=" ")
     print()

# #right side decreasing

for i in range(n):
    for j in range(i+1):
         print(' ', end=" ")
    for j in range(i, n):
       print("*", end=" ")
    print()

#hil pattern
n=5

for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i+1):
       print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")

    print()

#reverse hills
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n-1):
       print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")

    print()

#emoji reverse hill!!!!!

for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n-1):
       print("🍑", end=" ")
    for j in range(i,n):
        print("🍑", end=" ")

    print()

