def get_longest_chain(dominoes):
    best_chain = []
    
    def dfs(current_chain, used_indices):
        nonlocal best_chain

        if len(current_chain) > len(best_chain):
            best_chain = list(current_chain)
            
        last_val = current_chain[-1][1] if current_chain else None
        
        for i, dom in enumerate(dominoes):
            if i in used_indices:
                continue
            
            if last_val is None or dom[0] == last_val:
                current_chain.append(dom)
                used_indices.add(i)
                dfs(current_chain, used_indices)
                used_indices.remove(i)
                current_chain.pop()
                
            if dom[0] != dom[1]:
                if last_val is None or dom[1] == last_val:
                    current_chain.append([dom[1], dom[0]])
                    used_indices.add(i)
                    dfs(current_chain, used_indices)
                    used_indices.remove(i)
                    current_chain.pop()

    dfs([], set())
    return best_chain


print(get_longest_chain([[1, 2], [4, 5], [2, 3]]))
print(get_longest_chain([[2, 1], [4, 3], [5, 3]]))
print(get_longest_chain([[1, 2], [3, 4], [2, 3], [4, 0]]))
print(get_longest_chain([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]]))
print(get_longest_chain([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]]))
