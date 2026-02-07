import random
sonlar = list(range(1,10+1))
print(sonlar)
sonlar =random.randint(1,10)
print(sonlar) 

barcha_q_t = 2**sonlar
print(f"barcha qism to'plamlari soni {barcha_q_t} ga teng ")
xosmas_q_t = 2
print(f"xosmas qism to'plamlari soni {xosmas_q_t} ga teng ")
xos_q_t = (2 ** sonlar) - 2
print(f"xos qism to'plamlar soni {xos_q_t} ga teng")
bush_bulmagan_q_t = (2 ** sonlar) - 1
print(f'bo\'sh bo\'lmagan qism to\'plamlar soni ( {bush_bulmagan_q_t} )\
 ga teng ')
ikkita_kesishmaydigan_q_t = 2**(sonlar-1)
print(f"2 ta kesishmaydigan qismlar to'plami ( {ikkita_kesishmaydigan_q_t})\
 ga teng")
