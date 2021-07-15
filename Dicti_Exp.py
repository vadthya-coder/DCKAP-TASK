import json
test_string=input()
dit=json.loads(test_string)
exp=input()
exp=exp.replace("and","&")
exp=exp.replace("or","|")
exp=exp.replace(" ","")
lens=len(exp)
i,j,sti=0,0,0
stack=[]

while i< lens:
    if exp[i]=="|":
        i=i+2
    elif exp[i]=="&":
        stack.append(exp[i+1])
        sti=sti+1
        i=i+2
    elif exp[i]=="(" or exp[i]==")":
        i=i+1
    else:
        char=exp[i]
        if char in dit.keys():
            stack.append(exp[i])
            sti=sti+1
            i=i+1
        else:
            i=i+2

output=""
i=0
while i<sti:
    if stack[i]!="(":
        output=output+dit[stack[i]]
    i=i+1
print(output)