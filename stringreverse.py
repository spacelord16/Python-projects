wrd=input("Enter a word");
wrd=str(wrd);
reverse=wrd[::-1];
print(reverse);
if wrd==reverse:
    print("This word is palindrome");
else:
    print("This word is not palindrome");
