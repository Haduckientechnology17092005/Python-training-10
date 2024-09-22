def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))
def find_automorphic(n):
    automorphic_number = []
    for i in range(1, n+1):
        automorphic_number.append(i)
    return automorphic_number
limit = int(input("Enter the limit: "))
automorphic_number = find_automorphic(limit)
print("Automorphic numbers between 1 and", limit, "are:")
for i in automorphic_number:
    if is_automorphic(i):
        print(i,"^2 =",i**2)