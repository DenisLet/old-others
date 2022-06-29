a=int(input("Введите первый аргумент: "))
b=int(input("Введите второй аргумент: "))
c=input("Введите третий аргумент: ")
if c == "+":
       print(a, "+", b, "=", a+b )
elif c == "-":
      print(a, "-", b, "=", a-b)
elif c == "*":
      print(a, "*", b, "=, a*b")
elif c == "/":
      print(a, "/", b, "=", a/b)
else:
      print("Неизвестная операция ")