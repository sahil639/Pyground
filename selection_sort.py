def sel_sort(num):
# entire array
  for i in range(5):
      #setting the first position as minimum by default
     minpos = i
     #skipping sorted indexes
     for j in range(i,6):
         #comparing indexes of unsorted sub array
           if num[j] < num[minpos]:
               minpos = j
    #temp value will be used for swapping ut of the j loop
     temp = num[i]
     num[i] = num[minpos]
     num[minpos] = temp


num = [1, 2, 13, 14, 5, 9]      
sel_sort(num)

print(num)