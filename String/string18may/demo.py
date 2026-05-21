s=input()
l=len(s)
i=0
b=""
while i<l:
    word = ""
    if i!=" ":
        word=word+i
        b=b+word
    else:
        i=i+1
        break
    i=i+1
print(b)