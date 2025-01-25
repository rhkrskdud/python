sibal = ['c=','c-','dz=','d-','lj','nj','s=','z=']

s = input()

for i in sibal:
    s = s.replace(i,'ㅗ') #특정 문자가 있을때마다 치환.. 
    
print(len(s))