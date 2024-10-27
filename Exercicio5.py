import math
num = int(input('Digite um número: '))
if num < 0:
    print('\033[31mNão existe raiz de número negativo.\033[m')
else:
    raiz = math.sqrt(num)
    print(f'a raíz quadrada de \033[34m{num}\033[m é aproximadamente \033[31m{raiz:.1f}\033[m')

