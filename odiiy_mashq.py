ism = input("Ismingiz nima ? ").capitalize()
print(f"{ism} salom tanishganmdan hursandman",sep='\n')
yil = input(f'\n{ism} nechanchi yilda tug\'ilgansiz ? ')
yosh =2026 - int(yil) 
print(ism, 'siz', str(yil)+'-yilda tug\'ilgansiz', "hozir", str(yosh) +'-yoshdasiz') 
tanishish = input(f'\n{ism} keling tanishamiz 😃 (ha,albatta: yo\'q , shartmas): ')
if tanishish == 'ha' or tanishish == 'albatta' or tanishish == "aha" or tanishish == "ho'p" or tanishish == 'mayli':
    print(f"Aha. Hursand bo'ldim 🥰 , {ism} ")
    ahvoli =input(f'\n{ism} ahvoling yaxshimi (ha ; yo\'q)').lower() 
    if ahvoli == 'ha' or ahvoli == 'yaxshi':
        print(f"{ahvoli.title()} juda ajoyib.Shunday bo'lsin 🤩")
    else:
        print("Ha hali yaxshi bo'lib ketadi.O'ylanma")
else:
    print("Kayfiyating yo'qga o'xshayapti.Mayli keyinroq")

# uqish = input(f"{ism} {yosh}da ekansiz o'qiysizmi")
if yosh < 18 :
    print("Hali maktab o'qir ekansiz. A'lo bahoga o'qing ")
elif yosh == 18:
    print("18 yoshda ekansiz. siz bu yil davlat imtixonini topshirasiz OMAD tilayman")
else:
    uqish = input(f"\n{ism} {yosh}da ekansiz o'qiysizmi(ha / yo'q )").lower()

    # print(f"{ism} {yosh}da ekansiz ")
    # uqish = input(f"{ism} {yosh}da ekansiz o'qiysizmi(ha / yo'q )").lower()
    if uqish =='ha' or uqish == "o'qiyman":
        print(f"{ism} malades oliy malumotli ekansiz.O'qishda omad")
    else:
        print("Demak o'qishga kirolmagansiz. Hechqisi yo'q hayot hali oldinda")
        
        
        
    
    
    
    
        
        
    
    
    