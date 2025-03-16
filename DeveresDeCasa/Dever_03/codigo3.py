with open("dados.csv", "w") as lista:
    lista.write("Nome,Idade\n")
    lista.write("Ana,25\n")
    lista.write("Bruno,30\n")
    lista.write("Carla,22\n")
    lista.write("Daniel,28\n")
    lista.write("Eduardo,35\n")

dados = []
with open("dados.csv", "r") as lista:
    next(lista) 
    for linha in lista:
        nome, idade = linha.strip().split(",")
        dados.append((nome, int(idade)))  

#print("Lista do CSV:")
#for nome, idade in dados:
#    print(nome)

mais_velho = max(dados, key=lambda x: x[1])  

nome_digitado = input("\nDigite um nome: ")

encontrado = False
for nome, idade in dados:
    if nome.lower() == nome_digitado.lower(): 
        encontrado = True
        print(f"{nome} tem {idade} anos.")
        
       
        if idade == mais_velho[1]:
            print(f"{nome} é a pessoa mais velha da lista.")
        else:
            print(f"{nome} não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print("Nome não encontrado.")