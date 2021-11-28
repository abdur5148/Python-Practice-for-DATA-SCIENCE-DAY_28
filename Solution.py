def generate_dictionary(a, b):
    d = {}
    for i in range(a, b+1):
        d[i] = i**2
    return d


var1 = generate_dictionary(1, 20)

print(var1.values())
