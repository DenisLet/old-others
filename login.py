def get_login_name(first,last,id):
    set1=first[0:3]
    set2=last[0:3]
    set3=id[-3:]
    login_name=set1+set2+set3
    return login_name
