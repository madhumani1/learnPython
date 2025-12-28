rows = 5
# Left-angled triangle
for i in range(1, rows + 1):
    print("*" * i)  # Print i stars for each row
print("=====================================================")  # Blank line between patterns

# Right-angled triangle
for i in range(1, rows + 1):
    # print spaces first, then stars
    print(" " * (rows - i) + "*" * i)


print("=====================================================")  # Blank line between patterns
# Centered triangle
rows = 5

for i in range(1, rows + 1):
    # spaces + stars
    print(" " * (rows - i) + "*" * (2 * i - 1))

print("=====================================================")  # Blank line between patterns

# Diamond shape
rows = 5
for i in range(1, rows + 1):
    # upper part of diamond
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    # lower part of diamond
    print(" " * (rows - i) + "*" * (2 * i - 1))
print("=====================================================")  # Blank line between patterns
# Square pattern
rows = 5
for i in range(rows):
    print("* " * rows)  # Note the space after '*'
print("=====================================================")  # Blank line between patterns
