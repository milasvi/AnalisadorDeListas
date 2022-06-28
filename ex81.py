#bibliotecas
import emoji

#cabeçalho
print('-='*11)
print(' Analisador de Listas')
print('-='*11, '\n')

#variáveis 
lista = list()
pares = list()
impares = list()
maior = 0

#programa
while True:
    num = int(input("Digite um valor:"))
    if num not in lista:
        lista.append(num)
    else:
        print(emoji.emoji.emojize('Valor repetido :warning:  (não adicionado)'))
    if num not in pares and num % 2 == 0:
        pares.append(num)
    if num not in impares and num % 2 != 0:
        impares.append(num)
    res = str(input('Deseja continuar?'))
    while res.capitalize().split()[0] != 'S' and res.capitalize().split()[0] != 'N':
        res = str(input('\033[0;31mResposta inválida\033[m'))
    if res.capitalize().split()[0] == 'N':
        break

#análise
print('\n', '-'*22 ,'\n', f'Analisando sua lista...\n', '-'*22, '\n')
print(f'Foram digitados {len(lista)} números; \nA ordem descrecente da lista é {sorted(lista, key=int, reverse=True)};')
if 5 in lista:
    print('O valor 5 está presente;')
else:
    print('O valor 5 não está presente;')
if num > maior:
    maior = num
    print(f'O maior número digitado foi {num};')
print(f'Os números pares digitados foram {pares}; \nOs númares ímpares foram {impares}\nFim do programa! \n.')