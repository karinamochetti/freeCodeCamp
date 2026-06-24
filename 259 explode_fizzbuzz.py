def explode_fizzbuzz(target_z_count):
    result = "fizzbuzz"
    num_steps = 0
    while result.count("z") < target_z_count:
        new_result = ""
        for i, c in enumerate(list(result)):
            if (i+1) % 15 == 0:
                new_result += "fizzbuzz"
            elif (i+1) % 5 == 0:
                new_result += "buzz"
            elif (i+1) % 3 == 0:
                new_result += "fizz"
            else:
                new_result += c
        result = new_result
        num_steps += 1
    return num_steps

print(explode_fizzbuzz(9))
print(explode_fizzbuzz(15))
print(explode_fizzbuzz(51))
print(explode_fizzbuzz(52))
print(explode_fizzbuzz(359))
print(explode_fizzbuzz(789))
print(explode_fizzbuzz(54482))
print(explode_fizzbuzz(1000000))

