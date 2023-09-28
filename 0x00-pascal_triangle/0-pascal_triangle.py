def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            # Calculate the current row using the previous row
            prev_row = triangle[-1]
            current_row = [1]  # First element is always 1
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)  # Last element is always 1
            triangle.append(current_row)

    return triangle

# Example usage:
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
