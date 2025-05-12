def print_operation_table(operation, num_rows=9, num_columns=9):
    for r in range(1, num_rows+1):
        for c in range(1, num_columns+1):
            print(operation(r, c), end="\t")
        print()

print_operation_table(lambda x,y: x * y)
print()
print_operation_table(lambda x,y: x**y, 10, 10)
print()
print_operation_table(lambda x,y: x-y)