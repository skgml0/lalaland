alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s=input().upper()
p=[]
for i in alphabet:
    p.append(s.count(i))
#print(p,'------',max(p),'혹시 같은개수?',p.index(max(p)))
if p.count(max(p))>=2:
    print('?')
else:
    print(alphabet[p.index(max(p))])