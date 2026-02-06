A = int (input("Enter a number: "))
B = int (input("Enter another number: "))
C = int (input("Enter another number: "))

if(A>=B) and (A<=C):
    largest = A
if(B>=C) and (B<=A):
    largest = B
else:
    largest = C

print("the Largest number is ",largest)