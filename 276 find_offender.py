def find_offender(arr):
    for i, (a1, a2) in enumerate(zip(arr[:-1], arr[1:])):
        if a2-a1 < 0: 
            index = i
            break
    if arr[index-1] <= arr[index+1]:
        return index
    else:
        return index+1

print(find_offender([1, 6, 2, 3, 4, 5]))
print(find_offender([1, 2, 3, 5, 4, 5]))
print(find_offender([2, 1]))
print(find_offender([2, 4, 1, 6, 8]))
print(find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]))
