import pandas as pd
from sklearn.tree import DecisionTreeClassifier


dados_reais = {
    'IMC': [16.0, 17.5, 18.5, 22.0, 25.0, 27.5, 30.0, 35.0, 40.0, 45.0],
    'Classificacao': [
        'Magreza grave',
        'Magreza moderada',
        'Magreza leve',
        'Saudável',
        'Sobrepeso',
        'Pré-obeso',
        'Obeso Grau I',
        'Obeso Grau II',
        'Obeso Grau III',
        'Obeso Grau III'
    ],
    'Obeso': [False, False, False, False, False, True, True, True, True, True]  
}

df = pd.DataFrame(dados_reais)
df.to_csv('dados_imc_real.csv', index=False)
print("Arquivo 'dados_imc_real.csv' criado com sucesso!\n")

dados = pd.read_csv('dados_imc_real.csv')
X = dados[['IMC']]  
y = dados['Obeso'] 

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 25:
        return "Saudável"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

while True:
    try:
        entrada = input("\nDigite um valor de IMC (ou 'sair'): ")
        if entrada.lower() == 'sair':
            break

        imc = float(entrada)
        if imc <= 0:
            print("ERRO: IMC deve ser positivo!")
            continue

        classificacao = classificar_imc(imc)
        obesidade = modelo.predict([[imc]])[0]

        print(f"\nIMC: {imc:.1f}")
        print(f"Classificação OMS: {classificacao}")
        print(f"Risco de obesidade: {'Sim' if obesidade else 'Não'}")

    except ValueError:
        print("Valor inválido! Digite um número ou 'sair'.")