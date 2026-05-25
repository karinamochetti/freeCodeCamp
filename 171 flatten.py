def flatten(arr):
    stack = arr
    result = []
    
    while stack:
        elem = stack.pop()        
        if isinstance(elem, list):
            stack.extend(elem)
        else:
            result.append(elem)

    return result[::-1]

print(flatten([1, [2, 3], 4]))
print(flatten([5, [4, [3, 2]], 1]))
print(flatten(["A", [[[["B"]]]], "C"]))
print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))