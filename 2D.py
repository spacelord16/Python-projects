matrix_a=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ];
matrix_b=[
    [10,11,12],
    [13,14,15],
    [16,17,18],
    ];
for row in matrix_a:
    for item in row:
        print(item);

for row in matrix_b:
    for item in row:
        print(item);

print(matrix_a + matrix_b);
