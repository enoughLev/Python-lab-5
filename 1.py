spiso4ek = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 36, 45]
print("1.", *filter(lambda x: x > 5, spiso4ek))
print("2.", *map(lambda  x: x/2, spiso4ek))
print("3.", *map(lambda y: y / 2, filter(lambda x: x > 17, spiso4ek)))
print("4.", sum(map(lambda y: y**2, filter(lambda x: x % 9 == 0 and x > 10, spiso4ek))))
