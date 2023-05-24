def odd_count(n):
    counter = 0
    for i in range(n):
        if i % 2 == 1:
            counter += 1
    return counter

print(odd_count(11))