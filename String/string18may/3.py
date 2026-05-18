'''3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''

s=input("Enter complaint:")
sp=0
l=len(s)
for i in range(l):
    if s[i]==" ":
        if s[-1]==" ":
            sp=sp-1
        sp+=1
    

print("Total word=: ",sp+1)
