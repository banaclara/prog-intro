def somarpares(vetor):
    result = 0
    for n in vetor:
        if n % 2 == 0:
            result += n
    return result

lista = [1, 2, 3, 4, 5, 6]

print(somarpares(lista))