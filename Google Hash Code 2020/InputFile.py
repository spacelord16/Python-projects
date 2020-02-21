file=open("answer.txt","r")
A=(file.read(6)).split(" ")
B=A[0]
L=A[1]
print(A)
score_1=(file.read(12)).split(" ")
print(score_1)

lib_0_info=(file.read(6)).split(" ")
print(lib_0_info)

lib_0_books=(file.read(10)).split(" ")
print(lib_0_books)

lib_1_info=(file.read(6)).split(" ")
print(lib_1_info)

lib_1_books=(file.read(8)).split(" ")
print(lib_1_books)
