import pandas as pd
import numpy as np
import csv
import unicodedata
import re
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Input

def limpar_texto(texto):
    if not isinstance(texto, str):
        return ""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore")
    return texto.decode("utf-8")

def treinar_modelo():
    dados = pd.read_csv("intencoes_usuario.csv", encoding="utf-8")
    x = dados["frase"]
    y = dados["intencao"]
    
    codificador = LabelEncoder()
    y_codificado = codificador.fit_transform(y)
    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x, y_codificado, test_size=0.2, random_state=42
    )
    
    vetorizador = CountVectorizer()
    x_treino_vet = vetorizador.fit_transform(x_treino).toarray()
    x_teste_vet = vetorizador.transform(x_teste).toarray()
    
    modelo = Sequential()
    modelo.add(Input(shape=(x_treino_vet.shape[1],)))
    modelo.add(Dense(64, activation='relu'))
    modelo.add(Dense(32, activation="relu"))
    modelo.add(Dense(16, activation="relu"))
    modelo.add(Dense(len(codificador.classes_), activation="softmax"))
    
    modelo.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    modelo.fit(x_treino_vet, y_treino, epochs=30, batch_size=8, verbose=0)
    print("Modelo de intenções treinado com sucesso.")
    return modelo, vetorizador, codificador

def salvar_feedback(mensagem, categoria_correta):
    caminho = Path("intencoes_usuario.csv")
    if caminho.exists() and caminho.stat().st_size > 0:
        with caminho.open("rb+") as arquivo:
            arquivo.seek(-1, 2)
            ultimo_caractere = arquivo.read(1)
            if ultimo_caractere not in [b"\n", b"\r"]:
                arquivo.write(b"\n")
                
    with caminho.open("a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([mensagem, categoria_correta])
    print("Novo exemplo salvo no dataset de treino.")

def extrair_entidade(frase, coluna, dataframe):
    frase_limpa = limpar_texto(frase)
    
    # Tradutor de gêneros PT-BR para o padrão EN do arquivo CSV
    if coluna == "genre":
        de_para_generos = {
            "comedia": "Comedy", "terror": "Horror", "acao": "Action", 
            "aventura": "Adventure", "drama": "Drama", "romance": "Romance", 
            "ficcao": "Sci-Fi", "suspense": "Thriller", "misterio": "Mystery", 
            "animacao": "Animation", "crime": "Crime", "fantasia": "Fantasy",
            "documentario": "Documentary", "biografia": "Biography", "guerra": "War"
        }
        for pt, en in de_para_generos.items():
            if pt in frase_limpa:
                return en

    # Busca por correspondência de nomes (Atores e Diretores)
    valores_unicos = dataframe[coluna].dropna().unique()
    for valor in valores_unicos:
        valor_limpo = limpar_texto(str(valor))
        if valor_limpo in frase_limpa and len(valor_limpo) > 2:
            return valor
            
    return None 

# Treina o modelo de intenções
modelo, vetorizador, codificador = treinar_modelo()

# Carrega o seu banco de dados de filmes real
try:
    df_filmes = pd.read_csv("movies_per_year.csv", encoding="utf-8")
    print("Banco de dados de filmes carregado com sucesso!")
except FileNotFoundError:
    print("Erro crítico: O arquivo 'movies_per_year.csv' não foi encontrado!")
    exit()

# Inicialização da memória de filtros do usuário
filtros_usuario = {"ator": None, "genero": None, "diretor": None, "ano": None}

while True:
    mensagem = input("\nDigite os dados ou 'sair': ")
    if mensagem.lower() == "sair":
        print("Sistema Encerrado.")
        break

    mensagem_vet = vetorizador.transform([mensagem]).toarray()
    previsao = modelo.predict(mensagem_vet, verbose=0)
    categoria_numero = np.argmax(previsao)
    categoria_prevista = codificador.inverse_transform([categoria_numero])[0]

    print("Categoria prevista: ", categoria_prevista)
    resposta = input("A classificação está correta? (s/n) ")
    
    classificacao_valida = False
    
    if resposta.lower() == "s":
        print("Ótimo! O sistema acertou.")
        classificacao_valida = True
    elif resposta.lower() == "n":
        print("Categorias disponíveis: ")
        for categoria in codificador.classes_:
            print("-", categoria)

        categoria_correta = input("Digite a categoria correta: ")
        if categoria_correta in codificador.classes_:
            salvar_feedback(mensagem, categoria_correta)
            print("Retreinando o modelo...")
            modelo, vetorizador, codificador = treinar_modelo()
            classificacao_valida = True
        else:
            print("Categoria inválida. O exemplo não foi salvo.")
    else:
        print("Resposta inválida. Digite apenas s ou n.")

    # EXTRAÇÃO GLOBAL: Varre a frase buscando TODAS as entidades possíveis de uma vez
    if classificacao_valida:
        ator_f = extrair_entidade(mensagem, "star", df_filmes)
        diretor_f = extrair_entidade(mensagem, "director", df_filmes)
        genero_f = extrair_entidade(mensagem, "genre", df_filmes)
        
        # Procura por um ano (4 dígitos numéricos) na frase
        ano_busca = re.search(r'\b\d{4}\b', mensagem)
        ano_f = ano_busca.group(0) if ano_busca else None

        # Atualiza a memória apenas se algo real foi extraído
        if ator_f: filtros_usuario["ator"] = ator_f
        if diretor_f: filtros_usuario["diretor"] = diretor_f
        if genero_f: filtros_usuario["genero"] = genero_f
        if ano_f: filtros_usuario["ano"] = ano_f

    # Conta quantos filtros válidos temos ativos na memória
    categorias = sum(1 for valor in filtros_usuario.values() if valor is not None)
        
    # 🎬 Sistema de recomendação baseado nos filtros ativos
    if categorias >= 1:
        print("\n🤖 Assistente: Buscando filmes no sistema...")
        filmes_filtrados = df_filmes.copy()
        
        if filtros_usuario["ator"] is not None:
            termo = filtros_usuario["ator"].lower()
            filmes_filtrados = filmes_filtrados[filmes_filtrados['star'].str.lower().str.contains(termo, na=False)]
            
        if filtros_usuario["diretor"] is not None:
            termo = filtros_usuario["diretor"].lower()
            filmes_filtrados = filmes_filtrados[filmes_filtrados['director'].str.lower().str.contains(termo, na=False)]
            
        if filtros_usuario["genero"] is not None:
            termo = filtros_usuario["genero"].lower()
            filmes_filtrados = filmes_filtrados[filmes_filtrados['genre'].str.lower().str.contains(termo, na=False)]
            
        if filtros_usuario["ano"] is not None:
            termo = str(filtros_usuario["ano"])
            filmes_filtrados = filmes_filtrados[filmes_filtrados['year'].astype(str).str.contains(termo, na=False)]

        # Exibição dos resultados 
        if not filmes_filtrados.empty:
            print(f"\n🍿 Encontrei {len(filmes_filtrados)} filme(s) correspondente(s):")
            for index, linha in filmes_filtrados.head(5).iterrows():
                print(f"🎥 {linha['title']} ({linha['year']}) | Nota IMDb: {linha['rating_imdb']} | Elenco: {linha['star']} | Gênero: {linha['genre']}")
            
            # Limpa a memória para permitir uma nova busca do zero
            filtros_usuario = {"ator": None, "genero": None, "diretor": None, "ano": None}
        else:
            print("\nNão encontrei nenhum filme com essa combinação exata de filtros.")
            print(f"Filtros gerados: {filtros_usuario}")
            print("A memória de filtros foi limpa para uma nova tentativa.")
            filtros_usuario = {"ator": None, "genero": None, "diretor": None, "ano": None}
            
    else:
        print(f"\n🤖 Assistente: Filtros acumulados: {filtros_usuario}")
        print("Ainda não consegui extrair dados suficientes para a busca. Tente incluir nomes de atores, diretores, anos ou gêneros conhecidos.")
