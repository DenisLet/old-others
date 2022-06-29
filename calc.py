import random
min1=float(input("Enter minimum coef: "))
max1=float(input("Enter max coef: "))
def get_coef():
    coef=round(random.uniform(min1,max1),2)
    return coef
def main():
    target=int(input("Enter target: "))
    value=int(input("Enter initial value: "))
    calc(target,value)
def calc(target,value):
    count=1
    tot=1
    while value<=target:
        kef=get_coef()
        value=value*kef
        tot*=kef
        print(count,round(value,1),round(tot,2),kef,sep="---")
        count+=1
    print("The goal has been achieved!")

main()