import random
print("Keling o'yin o'ynaymiz.\nMen son o'ylayman siz topasiz ")
def kompyuter():
    son = random.randint(1 , 10)   
    urinish = 0
    while True:
        taxmin = int(input("Taxmingizni kiriting >>>  "))
        urinish += 1
        if taxmin < son :
            print("O'ylagan sonim broz katta ")
        elif taxmin > son :
            print("O'ylagan sonim broz kichik")
        else :
            break
        # return urinish
    print(f"Malades {urinish} urinishda to'g'ri topdiz ")
# kompyuter()
while True:
        kompyuter()
          
        davom = input("davom etamizmi etsak [ ha ] deb yozing   ")
        if davom != "ha":
            print("O'yin tugadi")
            break
        
import random       
def top():
    past = 1
    tepa = 10
    urinishlar = 0
    while True:
        surov = input("Keling endi siz son o'ylaysiz men uni topaman 😉    ")
        if surov == "yo'q" or surov == 'shartmas':
            print("Tushunarli.\nXayir")
            break
   

        soni = random.randint(past, tepa)
        while True:
            javob = input(f"Siz {soni} ni o'yladingiz. To'g'ri topgan bo'lsam [ T ] ni bosing,\
agar sziki katta bo'lsa [ I ] ni bosing\n\
agar kichik bo'lsa [ K ] ni bosing " ).upper()
    
            urinishlar += 1
        
            if javob == 'I':
               past = soni - 1
            #    
            # soni = random.randint(past, tepa)
            elif javob == 'K':
                tepa =soni + 1
            else:# elif javob == "T":
                print(f"Men {urinishlar}ta urinishda topdim ")
                break
            soni =  random.randint(past, tepa)
            # return urinishlar

while True:
            top()
            davom = input("Davom etamizmi yana.\nO'ynasak [ ha ] deb yozing ")
            if davom.upper()!= "HA": 
                print("O'yin tugadi ")
                break
            
            
            
kompyuter()
top()