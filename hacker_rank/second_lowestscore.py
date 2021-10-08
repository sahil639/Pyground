n = int(input()) #number of students
d = {}  #initialized empty dict for key and values
for i in range(n):
    keys = input() # here i have taken keys as strings
    values = int(input()) # here i have taken values as integers
    d[keys] = values
print(d)