lista = [1, 2, 3, 7, 8, 9, 9, 10, 12, 15, 17, 20, 23, 77]

def busca(lista, valor):
    tamanho = len(lista)
    inicio = 0
    final = tamanho - 1

    while True:
        meio = (inicio + final) // 2

        if inicio == final and valor != lista[meio]:
            return None

        if valor < lista[meio]:
            final = meio
        
        elif valor > lista[meio]:
            inicio = meio

            if inicio + 1 == final:
                inicio = final

        else:
            return meio


print('Buscando')
retorno = busca(lista, 17)
print(retorno)
