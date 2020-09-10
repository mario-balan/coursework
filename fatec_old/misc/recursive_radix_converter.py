# a recursive radix converter:

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   global counter
   counter+=1
   if n < base:
      print(base**counter, convertString[n])
      return convertString[n]
   else:
      print(base**counter,convertString[n%base])
      return toStr(n//base,base) + convertString[n%base]

counter=0
print(toStr(11,2))
print('recursões:', counter)

