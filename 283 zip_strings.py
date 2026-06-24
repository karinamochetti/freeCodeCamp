def zip_strings(a, b):
    n = min(len(a),len(b))
    zip_str = [c1+c2 for c1, c2 in zip(a[:n],b[:n])]
    return "".join(zip_str) + a[n:] + b[n:]

print(zip_strings("abc", "123"))
print(zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz"))
print(zip_strings("day", "night"))
print(zip_strings("python", "javascript"))
print(zip_strings("feCdCm", "reoeap"))
