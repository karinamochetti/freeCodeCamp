def compare_energy(calories_burned, watt_hours_used):
    workout = calories_burned*4184
    devices = watt_hours_used*3600
    if workout > devices: return "Workout"
    if workout == devices: return "Equal"
    if workout < devices: return "Devices"

print(compare_energy(250, 50))
print(compare_energy(100, 200))
print(compare_energy(450, 523))
print(compare_energy(300, 75))
print(compare_energy(200, 250))
print(compare_energy(900, 1046))

