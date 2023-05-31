from tabulate import tabulate 
a= input("enter your number:")
alamat_khas=["!","@","#","$","%","^","&","*",")","(","_","+","?","<",">","/","\ "," "]
shomreh={}
uniqueChars=set(a)
for i in a:
    if i in shomreh and i not in alamat_khas:
        shomreh[i]+=1 
    elif i not in shomreh and i not in alamat_khas:
        shomreh[i]=1
print(tabulate(shomreh.items(),headers=["Name", "Frequnecy"],tablefmt="grid"))