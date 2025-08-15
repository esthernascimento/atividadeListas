#1- Apresente o total de itens da exibida abaixo com os meses do ano.
#Retorno de um número inteiro
listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print(len(listaMeses))
print(60* '*')



#2- Junte as duas listas em uma terceira lista vazia.
#Concatene as duas listas
primeiroSemestre = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
segundoSemestre = ['Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
listaAno = primeiroSemestre + segundoSemestre
print(listaAno)
print(60* '*')



#3- Imprima de maneira separada o primeiro e último item da lista
listaValores = [2200, 3400, 5750, 800, 2000, 1350]
print('Primero item', listaValores[0])
print('Último item', listaValores[-1])
print(60* '*')



#4- Adicione o nome Paula Fernandes na posição 2
nomes = ['Suzy', 'Janaina', 'Claudevan', 'Maria Clara']
print(nomes)
nomes.insert(2, 'Paula Fernandes')
print(nomes)
print(60* '*')



#5- Alterar o nome Sony para Sony Vaio
#Remova o nome Compaq da lista.
nomes2 = ['Dell', 'Apple', 'Sony', 'Compaq', 'Positivo', 'Lenovo']
print(nomes2)
nomes2[2] = 'Sony Vaio'
print(nomes2)
nomes2.remove('Compaq')
print(nomes2)
print(60* '*')



#6- Imprima em ordem numérica crescente (do menor para o maior) a lista exibida abaixo
listadeNumeros = [230, 430, 100, 2, 670, 1212, 321, 89, 6, 34, 20, 9, 99, 710]
listadeNumeros.sort(reverse=False)
print(listadeNumeros)
print(60* '*')



#7- Imprima em ordem numérica decrescente (do maior para o menor) a lista exibida abaixo
listadeNumeros = [230, 430, 100, 2, 670, 1212, 321, 89, 6, 34, 20, 9, 99, 710]
listadeNumeros.sort(reverse=True)
print(listadeNumeros)
print(60* '*')


#8- Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a soma de todos os números pares da lista. A entrada dos valores deve ser informada pelo usuário.
listaPares = []
paresSoma = 0
for i in range(10):
    print("Digite o valor número", i + 1, ":")
    valorDigitado = int(input())
    listaPares.append(valorDigitado)
    if valorDigitado % 2 == 0:
        paresSoma += valorDigitado
print("Soma dos números pares:", paresSoma)
print(60 * '#')



#9- Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a média dos números da lista. Mais uma vez os valores devem ser digitados pelo usuário.
listaMedia = []
for i in range(10):
    print("Digite o valor número", i + 1, ":")
    valorDigitado = int(input())
    listaMedia.append(valorDigitado)
media = sum(listaMedia) / len(listaMedia)
print("Média dos números:", media)
print(60 * '#')



#10- Criar uma lista de atividades digitadas pelo usuário e exibir essas atividades.
listaAtividades = []
for i in range (1 ,5):
    listaAtividades.append(input('Digite um valor para inserir à lista: '))
print(listaAtividades)
print(60* '#')



