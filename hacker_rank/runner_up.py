
#optimized solution

#input
arr_size= int(input())
arr = list(map(int, input().strip().split()))[:arr_size]

#setting the type as set to not repeat values
arr2 = set(arr)
#removing the maximum of second array
arr2.remove(max(arr2))
#printing the array with second number as now maximum
print(max(arr2))

  