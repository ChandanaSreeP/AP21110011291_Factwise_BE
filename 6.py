s=(input("Enter no: "))
d1={'1':3,'2':3,'3':5,'4':4,'5':5,'6':3,'7':5,'8':5,'9':4,'10':3,'11':6,'12':6,'13':8,'14':8,'15':7,'16':7,'17':9,'18':8,'19':8,'20':6}
# 20-99
d2={'2':6,'3':6,'4':5,'5':5,'6':5,'7':7,'8':6,'9':6} 

def l1(s):
  return d1[s]
def l2(s):
  if s[0]=='1':
    return d1[s]
  else:
    return l1(s[1])+d2[s[0]]
def l3(s):
  return d1[s[0]]+10+l2(s[1:])

if len(s)==1:
  print(l1(s))
elif len(s)==2:
  print(l2(s))
elif len(s)==3:
  print(l3(s))
elif len(s)==4:
  print(4)
else:
  print('List index out of range')