def count_perfect_cubes(a, b):
    min_num, max_num = min(a,b), max(a,b)

    isPerfectCube = []
    for i in range(-max_num, max_num+1):
        isPerfectCube.append(i*i*i)

    perfect_cubes = 0
    for i in range(min_num, max_num+1):
        if i in isPerfectCube: 
            perfect_cubes += 1
    return perfect_cubes

print(count_perfect_cubes(3, 30))
print(count_perfect_cubes(1, 30))
print(count_perfect_cubes(30, 0))
print(count_perfect_cubes(-64, 64))
print(count_perfect_cubes(9214, -8127))
