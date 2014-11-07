
multiples3or5 = [x for x in range(1000) if x%3 == 0 or x%5 == 0]
product = sum(multiples3or5)

print product