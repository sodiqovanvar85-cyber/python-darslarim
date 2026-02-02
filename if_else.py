# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())


# login = input("Loginni kiriting:  ")
# if login.lower() == "admin":
#     print("Hush kelibsiz Admin")
# else:
#     print(f"kechirasiz {login} logini xato!")

# son1 = int(input("1-sonni kiriting   "))
# son2 = int(input("2-sonni kiriting   "))
# if son1 == son2:
#     print("sonlar o'zaro teng")
# elif son1 > son2 :
#     print(f"{son1},{son2}dan katta")
# else:
#     print(f"{son1},{son2}dan kichik")




# son = int(input("istalgan son kiriting. Men +, - ekanini aytaman  "))
# if son >=0:
#     print("bu son musbat ")
# else:
#     print("bu son manfiy")


# import math
# son = int(input("son kiriting men ildizini hisoblab beraman  "))
# print(f"{math.sqrt(son)}") if son > 0 else print("ildiz manfiy bo'lmaydi")
foydalanuvchilar = ['salom','admin','login','anvar','sonlar']
login = input("login kiriting ")
# for foydalanuvchi in foydalanuvchilar:
if  login in foydalanuvchilar:
        print ("bu login band boshqa kiriting ")
else:
        print (f"Hush kelibsiz,{login} ")
        
