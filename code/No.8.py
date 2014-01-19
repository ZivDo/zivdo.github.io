import os
file=open('No.2ForTest.py')
for lines in file:
    line=lines.strip()
    line1=line.split('=',1)
    if line1[0].strip()=='numbers':
        numbers1=line1[1].strip()
#        print numbers1
        numbers2=numbers1.split('[',1)
#        print numbers2[1]
        numbers3=numbers2[1].split(']',1)
#        print numbers3
        numbers4=numbers3[0].split(',')
#        print numbers4
        newNumbers=[]
        finalNumbers=[]
        for i in range(len(numbers4)):
            numbers5=numbers4[i].split("'")
            newNumbers.append(numbers5[1])
#        print newNumbers
        for j in range(len(newNumbers)):
            ele=int(newNumbers[j])
            finalNumbers.append(ele)
#        print finalNumbers
                        
def bubble(No):
    for k in range(len(No)-1):
        for v in range(len(No)-1):
            if No[v]>No[v+1]:
                No[v],No[v+1]=No[v+1],No[v]
    return No

print bubble(finalNumbers)
    
             
        