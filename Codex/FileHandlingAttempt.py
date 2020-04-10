f=open("Practice.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n"%(i+1))
f.close()


f=open("Practice.txt","r")
if f.mode=="r":
    contents=f.read()
    print(contents)