def tire_status(pressures_psi, range_bar):
    min_psi = range_bar[0]*14.5038
    max_psi = range_bar[1]*14.5038

    def get_status(psi):
        if psi < min_psi: return "Low"
        if psi > max_psi: return "High"
        return "Good"
        
    return [get_status(psi) for psi in pressures_psi]

print(tire_status([32, 28, 35, 29], [2, 3]))
print(tire_status([32, 28, 35, 30], [2, 2.3]))
print(tire_status([29, 26, 31, 28], [2.1, 2.5]))
print(tire_status([31, 31, 30, 29], [1.5, 2]))
print(tire_status([30, 28, 30, 29], [1.9, 2.1]))
