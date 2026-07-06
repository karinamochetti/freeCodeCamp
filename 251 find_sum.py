def find_sum(arr, target):
    n = len(arr)
    found_subset = None

    def dfs(start_idx, current_indices, current_sum):

        nonlocal found_subset
        if found_subset is not None:
            return
        
        if len(current_indices) >= 2 and current_sum == target:
            found_subset = [arr[i] for i in current_indices]
            return
            
        for i in range(start_idx, n):
            dfs(i + 1, current_indices + [i], current_sum + arr[i])
            if found_subset is not None:
                return

    dfs(0, [], 0)
    return found_subset if found_subset is not None else "Sum not found"
    
print(find_sum([1, 3, 5, 7], 6))
print(find_sum([1, 2, 3, 4, 5], 5) )
print(find_sum([1, 2, 3, 4, 5], 6))
print(find_sum([-1, -2, 3, 4], 1))
print(find_sum([3, 1, 4, 1, 5, 9, 2, 6], 10))
print(find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 20))
print(find_sum([7, 9, 4, 2, 5], 10))
