def number_of_files(file_size, file_unit, drive_size_gb):
    convert_GB = {"B": 1, "KB": 1000, "MB": 1000000, "GB": 1000000000}
    return (drive_size_gb*convert_GB["GB"])//(file_size*convert_GB[file_unit])

print(number_of_files(500, "KB", 1))    
print(number_of_files(50000, "B", 1))    
print(number_of_files(5, "MB", 1))    
print(number_of_files(4096, "B", 1.5))    
print(number_of_files(220.5, "KB", 100))    
print(number_of_files(4.5, "MB", 750))    


