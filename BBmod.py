def guess():
    import random
    dic = dct()
    list_keys=[]
    for i in dic.keys():
        list_keys.append(i)
    right,wrong,x=0,0,1
    while x<=len(dic):
        rand = random.choice(list_keys)
        print("Guess capital of: ", rand)
        answer = input("Enter city: ")
        if dic[rand]==answer:
            print("Yes")
            right+=1
            x+=1
            list_keys.remove(rand)
        else:
            print("No")
            wrong+=1
            x+=1
            list_keys.remove(rand)
    print(right,wrong)
def dct():
    countries={"Russia":"Moscow","USA":"Washington","China":"Beijin",
               "Japan":"Tokyo","France":"Paris"}
    return countries
guess()