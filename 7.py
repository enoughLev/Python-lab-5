def same_by(characteristic, objects):
    if not objects:
        return True
    first_value = characteristic(objects[0])
    return all(characteristic(obj) == first_value for obj in objects)

values = [1, 3, 11, 7]
val_1 = [2, 4, 6, 10, 0]

print(same_by(lambda x: x % 2, values))
print(same_by(lambda x: x % 2, val_1))