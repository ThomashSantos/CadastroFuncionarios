import requests
from fonte import pasta_entrada
import os


def download_arquivo(url, destination):
    response = requests.get(url, stream=True)
    caminho_destino = os.path.join(pasta_entrada, destination)
    with open(caminho_destino, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


if __name__ == "__main__":
    url_arquivo = "https://workshop.botcity.dev/assets/candidatos.csv"
    nome_arquivo = "banco.sql.csv"
    download_arquivo(url_arquivo, nome_arquivo)