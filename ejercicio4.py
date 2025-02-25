""" Tirar dos dados, mostrar el resultado mayor,
si uno de los dos es 20 escribe CRÍTICO
si los dos son 1 escribe PIFIA """

import random

dado = range(1, 21)

res_1 = random.choice(dado)
print(f"resultado 1: {res_1}")
res_2 = random.choice(dado)
print(f"resultado 2: {res_2}")

if res_1 == 1 and res_2 == 1:
    print("PIFIA")
elif res_1 == 20 or res_2 == 20:
    print("CRÍTICO")
elif res_1 > res_2:
    print(res_1)
else:
    print(res_2)