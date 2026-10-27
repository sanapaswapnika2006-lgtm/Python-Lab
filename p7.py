
# Functional Data Filtering and Matrix Transformation Suite

def remove_negative(matrix):
    return list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))


def sort_rows(matrix):
    return list(map(lambda row: sorted(row), matrix))


def sort_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


def transform_matrix(matrix):
    return list(map(
        lambda row: list(map(lambda x: x * 2, row)),
        matrix
    ))


# Main program
matrix = [
    [3, -2, 5],
    [8, 1, -4],
    [-6, 7, 2]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# Remove negative numbers
cleaned = remove_negative(matrix)
print("\nMatrix after removing negative numbers:")
for row in cleaned:
    print(row)

# Sort each row
sorted_matrix = sort_rows(cleaned)
print("\nMatrix after sorting each row:")
for row in sorted_matrix:
    print(row)

# Sort rows by their sum
sum_sorted = sort_by_sum(sorted_matrix)
print("\nRows sorted by sum:")
for row in sum_sorted:
    print(row)

# Double every element
doubled = transform_matrix(cleaned)
print("\nMatrix after doubling elements:")
for row in doubled:
    print(row)

# Tuple transformation using map()
numbers = (1, 2, 3, 4, 5)
squares = tuple(map(lambda x: x * x, numbers))

print("\nOriginal Tuple:", numbers)
print("Squared Tuple:", squares)
