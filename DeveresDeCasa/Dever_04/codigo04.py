import random
import pandas as pd


frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

try:
    with open("minhas_frutas.txt", "w") as arquivo:
        for fruta in frutas:
            quantidade = random.randint(0, 100)
            arquivo.write(f"{fruta},{quantidade}\n")
except IOError:
    print("Erro ao criar o arquivo")
    exit()

try:
    df = pd.read_csv('minhas_frutas.txt', names=['Fruta', 'Quantidade'], sep=',')

    df_agrupado = df.groupby('Fruta', as_index=False)['Quantidade'].sum()

    print("\nRelatório de Frutas:")
    print(df_agrupado)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
except Exception as e:
    print(f"Erro inesperado: {e}")