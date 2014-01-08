numbers = [ "8", "6", "3", "9", "5", "2", "4", "1", "7" ]

for j in range(len(numbers)-1):
    
    for i in range(len(numbers)-1):
    
        if i==len(numbers)-1-j:
            break
        elif numbers[i]>numbers[i+1]:
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
#    for t in range(len(numbers)-1):
#        if numbers[t]<numbers[t+1]:
#            pass
#        else:
#            break
print(numbers)
