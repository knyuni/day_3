a = [4,66,7]
b =  [66,77,7,4]
aList = []
if len(a) and len(b) > 0:
  if a.count == b.count:
    c=0
  else:
    c= list(set(a)^set(b))
 # c= set(a).symmetric_difference(b)
else:
  c=0
print (c)