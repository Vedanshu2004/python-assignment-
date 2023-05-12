print("************** CODING THE LANGUAGE **************")
A = input("enter the any word : ")
b = A[1:len(A)]
print(b+A[0])
s = input("Enter random word :")
d = input("Enter random word :")
f= s + b + A[0] + d
g = f[::-1]
print(g)
print("************* DECODING THE LANGUAGE *************")
h = g[::-1]
i = h[len(s): len(A)+len(s)]
print(i)
j = i[len(i)-1]
print(j + b)


