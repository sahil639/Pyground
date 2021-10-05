#The Quick Sort algorithm takes an item from the unsorted list and uses it as the 'pivot' or the item to compare the remainder of the items in the list. 
# We do comparisons placing the items in lists according to if they are larger or smaller than the pivot value.


def quick_sort(sequence):

    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        #removes last item as the 'pivot' or the item to compare the remainder of the items
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

n = int(input("Enter the number of items in list :\n"))
sequence = list(map(int, input("Enter the list you want to sort:\n").strip().split()))[:n]
print(f"your unsorted list is: {sequence}")
a= quick_sort(sequence)
print(f"your sorted list using quick sort is: {a}")