l=list(map(int,input('Enter card points: ').split()))
k=int(input("Enter k: "))
c=0
for _ in range(k):
  if l[0]>l[-1]:
    c+=l[0]
    l.remove(l[0])
  elif l[0]<l[-1]:
    c+=l[-1]
    l.pop()
  else:
    c+=l[-1]
    l.pop()
print(c)