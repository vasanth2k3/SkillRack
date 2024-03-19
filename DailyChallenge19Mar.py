a=input().strip()
dig=""
for i in a:
if i.isalpha(): 
  print(i,end="")
else:
  dig+=i
print(dig)
