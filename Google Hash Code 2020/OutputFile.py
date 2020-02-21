file=open("Output_1.txt","w")
file.write(L)
file.write(K)
file.close()

file=open("Output_1.txt","r")
print(file.read())
file.close()


# def order_of_signup(args):
#     pass
#
#
# def order_of_books(args):
#     pass
#
#
# def write_output():
#     with open("submission.txt", "w+") as file:
#         file.write(str(len(order_of_signup)) + "\n")
#         for i in range(len(order_of_signup)):
#             file.write(str(order_of_signup[i]) + " " + str(len(order_of_books[order_of_signup[i]]))+"\n")
#             for item in order_of_books[order_of_signup[i]]:
#                 file.write(str(item) + " ")
#             file.write("\n")