import sys
import os


while True:
    contador_1 = 10
    contador_2 = 11
    calc_1 = []
    calc_2 = []

    cpf = input('Digite o seu CPF: ') \
        .replace('.','') \
        .replace('-','') \
        .replace(' ','')
    
    entrada_e_sequencial = cpf == cpf[0] * len(cpf)

    if entrada_e_sequencial:
        print('Você enviou dados sequenciais.')
        sys.exit()

    cpf_fatiado = cpf[0:9]

    for prim in cpf_fatiado:
        prim = int(prim) * contador_1
        calc_1.append(prim)
        contador_1 -= 1

    prim = (sum(calc_1) * 10) % 11

    prim = prim if prim <= 9 else 0

    for seg in cpf_fatiado:
        seg = int(seg) * contador_2
        calc_2.append(seg)
        contador_2 -= 1
    
    seg = (sum(calc_2) + prim * contador_2) * 10 % 11

    seg = seg if seg <= 9 else 0

    cpf_completo = cpf_fatiado + str(prim) + str(seg)

    if cpf_completo == cpf:
        print('CPF válido')
    else:
        print ('CPF inválido')
    
    print(f'CPF após conta = {cpf_completo}')

    resp = input('Deseja Realizar outra Validação ? (s/n) : ')
    resp.lower()

    if resp == 's':
        os.system('cls')
        continue
    
    else:
        os.system('cls')
        break