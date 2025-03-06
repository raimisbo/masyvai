import random

# ====================== MASYVAI ===================

# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.

random_digits = []
for _ in range(30):
    random_digits.append(random.randint(5, 25))
print(random_digits)

# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;

digits = 0
for number in random_digits:
    if number > 10:
        digits += 1
        # print(number)
print(f'{digits} reiksmes, didesnes uz 10')

# Raskite didžiausią masyvo reikšmę;

max_value = 0
for digit in random_digits:
    if digit > max_value:
        max_value = digit
print(f'{max_value} yra maksimali reiksme')

# Suskaičiuokite visų reikšmių sumą

sum = sum(random_digits)
print(f'{sum} yra reiksmiu suma')

sum = 0
for digit in random_digits:
    sum += digit
print(F'{sum} yra reiksmiu suma')

# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;

random_digits_2 = []
position = 0
for i in random_digits:
    # print(f'{position} indeksas, {i} reiksme')
    random_digits_2.append(i-(position))
    position +=1
print(random_digits_2)

# for i in random_digits:
#     print(f'{position} {i}')
#     position += 1

# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
# e.1
# random_digits.extend([random.randint(5,25)
# for _ in range(10)])
# print(random_digits)

# e.2
num_digits = 10
for _ in range(num_digits):
    random_dig = random.randint(5,25)
    random_digits.append(random_dig)
print(random_digits)

# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;

# f.1
random_digits_even = random_digits[::2]
print(f'f.1 Poriniai indeksai {random_digits_even}')
random_digits_odd = random_digits[1::2]
print(f'f.1 Neporiniai indeksai: {random_digits_odd}')

# f.2
random_digits_even1 = []
random_digits_odd1 = []
for i in range(0, len(random_digits)):
    if i % 2 == 0:
        # print(i, random_digits[i])
        random_digits_even1.append(random_digits[i])
    else:
        random_digits_odd1.append(random_digits[i])
print("f.2 Poriniai indeksai: ", random_digits_even1)
print("f.2 Neporiniai indeksai: ", random_digits_odd1)

# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;


for i in range(0, len(random_digits), 2):
    if random_digits[i] > 15:
        random_digits[i] = 0
print(f'Pakeistos reiksmes i 0, jei buvo  > 5: ', random_digits)

# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;

print("--- uzd 2.h ---")
print(random_digits)
for i in range(0, len(random_digits)):
    if random_digits[i] > 10:
        print(i)
        break

print("----uzd.3----")

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.

raides = ["A","B","C","D"]
masyvas_r = []

for i in range(0,200):
    raides_vieta = random.randint(0,3)
    raide = raides[raides_vieta]
    masyvas_r.append(raide)

sk_A = 0
sk_B = 0
sk_C = 0
sk_D = 0

for raide in masyvas_r:
    if raide == "A":
        sk_A += 1
    if raide == "B":
        sk_B += 1
    if raide == "C":
        sk_C += 1
    if raide == "D":
        sk_D += 1

print(masyvas_r)
print(f'A: {sk_A}, B: {sk_B}, C: {sk_C}, D: {sk_D}')


print('-----uzd.4-----')

# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.

for _ in range(len(masyvas_r)):
    for i in range(len(masyvas_r) - 1):
        if masyvas_r[i] > masyvas_r[i + 1]:
            masyvas_r[i], masyvas_r[i + 1] = masyvas_r[i + 1], masyvas_r[i]

print(masyvas_r)
# pasiaiskinti

print("-----uzd.5------")

# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.


raides = ["A","B","C","D"]
mas_r1 = []
mas_r2 = []
mas_r3 = []
mas_sum = []


for i in range(0,200):
    raides_vieta = random.randint(0,3)
    raide = raides[raides_vieta]
    mas_r1.append(raide)

for i in range(0,200):
    raides_vieta = random.randint(0,3)
    raide = raides[raides_vieta]
    mas_r2.append(raide)

for i in range(0,200):
    raides_vieta = random.randint(0,3)
    raide = raides[raides_vieta]
    mas_r3.append(raide)

for i in range(len(mas_r1)):
    mas_sum.append(mas_r1[i] + mas_r2[i] + mas_r3[i])
print(mas_sum)

unikomb = []
for komb in mas_sum:
    if komb not in unikomb:
        unikomb.append(komb)
komb_sk = len(unikomb)
print(f'{komb_sk} skirtingos reiksmes.TAIP!!!')

# kombinacija = "BBD"
# if kombinacija in mas_sum:
#     print(f'Taigi {kombinacija} YRA sarase')
# else:
#     print(f'Tiesiog nepasiseke :(')


print("-----Uzd.6------")

# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100.
# Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).

mas_1 = []
mas_2 = []
for _ in range(100):
    num = random.randint(100, 999)
    while num in mas_1:
        num = random.randint(100, 999)
    mas_1.append(num)

for _ in range(100):
    num = random.randint(100, 999)
    while num in mas_2:
        num = random.randint(100, 999)
    mas_2.append(num)

print(f'Pirmas masyvas {mas_1}')
print(f'Antras masyvas {mas_2}')

print("------------Uzd.7------------")

# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame
# 6 uždavinio masyve.

mas_3 = [num for num in mas_1 if num not in mas_2]

print(f'Reiksmes is pirmo masyvo, bet ne is antro {mas_3}')

print("-------------uzd.8-------------")

# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.

mas_4 = []
for num in mas_1:
    if num in mas_2:
        mas_4.append(num)

print(f'Reiksmes, pasikartojancios abiejuose masyvuose {mas_4}')

print("---------uzd.9----------")

# Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25.
# Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.


num_1 = random.randint(5,25)
num_2 = random.randint(5,25)

mas = [num_1, num_2]
print(mas)
for i in range(1,9):
    mas.append(mas[i-1] + mas[i])
print(mas)


print("============Uzd.10=============")

# Sugeneruokite 101 elemento masyvą su atsitiktiniais skaičiais nuo 0 iki 300. Reikšmes kurios tame masyve yra ne unikalios pergeneruokite iš naujo taip, kad visos reikšmės masyve būtų unikalios. Išrūšiuokite masyvą taip, kad jo didžiausia reikšmė būtų masyvo viduryje, o einant nuo jos link masyvo pradžios ir pabaigos reikšmės mažėtų. Paskaičiuokite pirmos ir antros masyvo dalies sumas (neskaičiuojant vidurinės). Jeigu sumų skirtumas (modulis, absoliutus dydis) yra didesnis nei | 30 | rūšiavimą kartokite. (Kad sumos nesiskirtų viena nuo kitos daugiau nei per 30)


mas_10 = []
dydis = 101

while len(mas_10) < dydis:
    num = random.randint(0,300)
    if num not in mas_10:
        mas_10.append(num) #pakrautas ciklas be pasikartojanciu
# print(mas_10)

for i in range(len(mas_10)):
        for r in range(i + 1, len(mas_10)):
            if mas_10[i] > mas_10[r]:                    #isrikiuotas > (galima <)
                mas_10[i], mas_10[r] = mas_10[r], mas_10[i]
print(mas_10)















