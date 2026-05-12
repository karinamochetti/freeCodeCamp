def format_date(date_string):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    m, d, y = date_string.replace(",", "").split()
    m_idx = months.index(m) + 1
    
    return f"{int(y)}-{m_idx:02d}-{int(d):02d}"

print(format_date("December 6, 2025"))
print(format_date("January 1, 2000"))
print(format_date("November 11, 1111"))
print(format_date("September 7, 512"))
print(format_date("May 4, 1950"))
print(format_date("February 29, 1992"))
