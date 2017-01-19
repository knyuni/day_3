a = [4,66,7]
b =  [66,77,7,4]
aList = []
if len(a) and len(b) > 0:
  if a.count == b.count:
    c=0
  else:
    c= list(set(i for i in b if i not in a))
 
else:
  c=0
print (c)