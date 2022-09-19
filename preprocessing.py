import json

file1 = open('data.json', 'r')
Lines = file1.readlines()

count=1

state=[]
income=[]
sale=[]
pro=[]

for line in Lines:
    line =line.strip()
    if line != '[' and line != '{' and line != '},' and line != '}' and line != ']':
        key,value=line.split(": ")
        if count==1:
            value = value.split('"')
            state.append(value[1])
            count=2
        elif count==2:
            value = value.split('"')        
            if len(value)==1:
                value=value[0].split(",")
                income.append(float(value[0]))
            elif value[1]=='':
                income.append(0)
            else:
                income.append(float(value[1]))
            count=3
        elif count==3:
            value = value.split('"')        
            if len(value)==1:
                value=value[0].split(",")
                sale.append(float(value[0]))
            elif value[1]=='':
                sale.append(0)
            else:
                sale.append(float(value[1]))
            count=4
        else:
            value = value.split('"')        
            if len(value)==1:
                value=value[0].split(",")
                pro.append(int(value[0]))
            elif value[1]=='':
                pro.append(0)
            else:
                pro.append(int(value[1]))
            count=1

x = {
    "State":state,
    "IncomeTax":income,
    "SaleTax":sale,
    "PropertyTax":pro
    }

with open('newdata.json', 'w') as f:
    json.dump(x,f, ensure_ascii=False, indent=4)
