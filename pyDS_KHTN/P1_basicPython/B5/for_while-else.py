numInput = 7
# python có cú pháp for else và while else, else sẽ kích nếu các vòng lặp trên chạy hết, ko bị break thoát loop sớm.
# Viết theo js thì phải set flag hoặc dùng some / any / every
print("numInput:" , numInput) #check update value
for numCheck in range(1,numInput+1):
    if numCheck == 1 :
        sum = 1 
        sumString = "1"
    else:
        prime = True
        for divider in range (2, numCheck):
            if(numCheck % divider == 0) : 
                # prime = False
                break;
        if prime : 
            sum += numCheck
            sumString += f" + {numCheck}"
    numCheck += 1
sumString += f' = {sum}'
print(sumString)        

