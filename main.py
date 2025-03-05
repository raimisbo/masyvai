import random

# ================================= MASYVAI =================================

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


