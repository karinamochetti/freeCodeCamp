def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    temp = current_f - target_f
    if current_f < target_f:
        return f"Heat: {abs(temp):.1f} degrees Fahrenheit"
    if current_f > target_f:
        return f"Cool: {abs(temp):.1f} degrees Fahrenheit"
    if current_f == target_f:
        return f"Hold"


print(adjust_thermostat(32, 0))
print(adjust_thermostat(70, 25))
print(adjust_thermostat(72, 18))
print(adjust_thermostat(212, 100))
print(adjust_thermostat(59, 22))
