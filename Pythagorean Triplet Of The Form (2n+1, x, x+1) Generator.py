import random
triplets = []
for i in range (1,50):
    a = 2*i + 1
    b = 2*i**2 + 2*i
    c = 2*i**2 + 2*i + 1
    triplets.append((a,b,c))
print(triplets)