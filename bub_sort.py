
#compares consecutive numbers until bigger nmbers gets pushed to the end of the list
#swapping in taken place at each iteration after one fixed position that position is ignored

def bub_sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i): 
           if num[j] > num[j+1]:
               temp = num[j]
               num[j] = num[j+1]
               num[j+1] = temp

num = [5, 3, 8, 6, 7, 2]
bub_sort(num)

print(num)