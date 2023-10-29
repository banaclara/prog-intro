q = []

while len(q) < 20:
    new = int(input('Digite um número: '))
    q.append(new)

maior = max(q)
posi1 = q.index(maior)

print(f'O maior valor na lista é {maior} e ele ocupa o índice {posi1} (ou seja, a posição {posi1 + 1}).')

menor = min(q)
posi2 = q.index(menor)

print(f'O menor valor na lista é {menor} e ele ocupa o índice {posi2} (ou seja, a posição {posi2 + 1}).')