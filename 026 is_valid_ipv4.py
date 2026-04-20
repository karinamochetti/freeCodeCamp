def is_valid_ipv4(ipv4):
    values = ipv4.split(".")
    if len(values) != 4: 
        return False
    for value in values:
        if not value.isdigit():
            return False
        if value != "0" and value.startswith('0'):
            return False
        if not (0 <= int(value) <= 255):
            return False
    return True

print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("0.0.0.0"))
print(is_valid_ipv4("255.01.50.111"))
print(is_valid_ipv4("255.00.50.111"))
print(is_valid_ipv4("256.101.50.115"))
print(is_valid_ipv4("192.168.101."))
print(is_valid_ipv4("192168145213"))

