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

random_digits_even = random_digits[::2]
print(f'Poriniai indeksai {random_digits_even}')
random_digits_odd = random_digits[1::2]
print(f'Neporiniai indeksai: {random_digits_odd}')

random_digits_even1 = []
random_digits_odd1 = []
for i in range(0, len(random_digits)):
    if i % 2 == 0:
        # print(i, random_digits[i])
        random_digits_even1.append(random_digits[i])
    else:
        random_digits_odd1.append(random_digits[i])
print("Poriniai indeksai: ", random_digits_even1)
print("Neporiniai indeksai: ", random_digits_odd1)






