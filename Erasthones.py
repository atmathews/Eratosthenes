import time
def sieve(num):
    timestart = float(time.time())
    iniArray = []
    for i in range(3,num+1,2):      # Creating a list of numbers up to the given number, doesn't include
        iniArray.append(i)

    primeArray = [3]
    pla = 0
    inc = 0

    while(pla<len(primeArray)):
        while(inc < len(iniArray)):
            prime = primeArray[pla]
            num = iniArray[inc]
            if((num%prime == 0) & (prime!=num) &(num > prime)):
                iniArray.pop(inc)
            else:
                inc += 1

        if(pla+1!=len(iniArray)):
            primeArray.append(iniArray[pla+1])
        pla +=1
        inc =0

    iniArray.insert(0,2)
    print(iniArray)
    print(float(time.time())-timestart)

initalNum = input("Enter number to primize")
sieve(initalNum)