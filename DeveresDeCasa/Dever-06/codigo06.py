from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_and_prepare_data():
    """Carrega e prepara os dados"""
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['target'])
    return iris, df

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_and_prepare_data():
    """Carrega e prepara os dados"""
    iris = load_iris()
    feature_names_pt = [
        'comprimento_sépal3
        a',
        'largura_sépala',
        'comprimento_pétala',
        'largura_pétala'
    ]
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=feature_names_pt + ['classe'])
    return iris, df

def train_model(X_train, y_train, n_neighbors=3):
    """Treina o modelo KNN"""
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, iris):
    """Avalia o desempenho do modelo"""
    y_pred = model.predict(X_test)

    target_names_pt = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    print("\n=== Métricas de Avaliação ===")
    print(f"Acurácia do modelo: {accuracy_score(y_test, y_pred):.2%}")
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred, target_names=target_names_pt))


def classify_new_sample(model, iris):
    """Classifica uma nova amostra baseada em input do usuário"""
    print("\n=== Classificação de Nova Amostra ===")
    try:
        features = []
        feature_names_pt = [
            'Comprimento da sépala (cm)',
            'Largura da sépala (cm)',
            'Comprimento da pétala (cm)',
            'Largura da pétala (cm)'
        ]

        for feature in feature_names_pt:
            value = float(input(f"{feature}: "))
            features.append(value)

        prediction = model.predict([features])
        class_names_pt = {
            0: 'Iris-setosa',
            1: 'Iris-versicolor',
            2: 'Iris-virginica'
        }
        print(f"\nA flor foi classificada como: {class_names_pt[prediction[0]]}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

def main():
    """Fluxo principal do programa"""
    # 1. Carregar e preparar dados
    iris, df = load_and_prepare_data()
    X = iris.data
    y = iris.target

    # 2. Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)

    # 3. Treinar modelo
    model = train_model(X_train, y_train, n_neighbors=5)

    # 4. Avaliar modelo
    evaluate_model(model, X_test, y_test, iris)

    # 5. Classificar nova amostra
    classify_new_sample(model, iris)

if __name__ == "__main__":
    main()