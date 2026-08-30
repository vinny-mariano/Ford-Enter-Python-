import pandas as pd
import numpy as np
import csv
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

def treinar_modelo():

    dados = pd.read_csv("mensagens.csv", encoding="utf-8")
    x = dados["mensagem"]
    y = dados["categoria"]

    codificador = LabelEncoder()
    y_codificado = codificador.fit_transform(y)
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y_codificado, test_size=0.2, random_state=42)

    vetorizador = CountVectorizer()
    x_treino_vet = vetorizador.fit_transform(x_treino).toarray()
    x_teste_vet = vetorizador.transform(x_teste).toarray()

    modelo = Sequential()
    modelo.add(Dense(32, activation="relu", input_shape=(x_treino_vet.shape[1],)))
    modelo.add(Dense(16, activation="relu"))
    modelo.add(Dense(len(codificador.classes_), activation="softmax"))
    modelo.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    modelo.fit(x_treino_vet, y_treino,epochs=30, batch_size=8, verbose=0)
    perda, acuracia = modelo.evaluate(x_teste_vet, y_teste, verbose=0)

    print("Modelo treinado.")
    print("Acurácia:", round(acuracia, 2))

    return modelo, vetorizador, codificador

def salvar_feedback(mensagem, categoria_correta):
    caminho = Path("mensagens.csv")

    if caminho.exists() and caminho.stat().st_size > 0:
        with caminho.open("rb+") as arquivo:
            arquivo.seek(-1,2)
            ultimo_caractere = arquivo.read(1)

            if ultimo_caractere not in [b"\n", b"\r"]:
                arquivo.write(b"\n")

    with caminho.open("a",newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([mensagem, categoria_correta])
    print("Novo exemplo salvo no dataset.")

modelo, vetorizador, codificador = treinar_modelo()

while True:
    mensagem = input("\nDigite uma mensagem ou 'sair':")
    if mensagem.lower() =="sair":
        print("Sistema Encerrado.")
        break

    mensagem_vet = vetorizador.transform([mensagem]).toarray()

    previsao = modelo.predict(mensagem_vet, verbose=0)
    categoria_numero = np.argmax(previsao)
    categoria_prevista = codificador.inverse_transform([categoria_numero])[0]

    print("Categoria prevista: ", categoria_prevista)

    resposta = input("A classificação está correta? (s/n)")

    if resposta.lower() == "s":
        print("òtimo! O sistema acertou.")

    elif resposta.lower() == "n":
        print("Categorias disponíveis: ")

        for categoria in codificador.classes_:
            print("-", categoria)

        categoria_correta = input("Digite a categoria correta: ")

        if categoria_correta in codificador.classes_:
            salvar_feedback(mensagem, categoria_correta)
            print("Retreinando o modelo com o novo exemplo...")
            modelo, vetorizador, codificador = treinar_modelo()

        else:
            print("Categoria inválida. O exemplo não foi salvo.")

    else:
        print("Resposta inválida. Digite apenas s ou n.")