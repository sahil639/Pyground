
#compares consecutive numbers until bigger nmbers gets pushed to the end of the list
#swapping in taken place at each iteration after one fixed position that position is ignored

def bub_sort(num):
    # if num is 7 then the range is from 6 to 0 at interval of -1 
    for i in range(len(num)-1,0,-1):
    # traverses through whats left of i
        for j in range(i): 
           if num[j] > num[j+1]:
               #swap time
               temp = num[j]
               num[j] = num[j+1]
               num[j+1] = temp

# num = [5, 3, 8, 6, 7, 2]
n = int(input('Enter the size of the list:'))
num = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print(f"your unsorted list is : {num}")
bub_sort(num)
print(f"your sorted list is : {num}")


# bubble sort ---> len-1 to 0 at -1 and swapping 