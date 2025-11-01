from fonte import pasta_saida
import csv
import os


class CapturadaDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def ler_dados(self):
        dados = []
        with open(self.caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                primeiro_nome, nome_do_meio, ultimo_nome = self.separar_nome_completo(linha.get("full_name", ""))
                linha["first_name"] = primeiro_nome
                linha["middle_name"] = nome_do_meio
                linha["last_name"] = ultimo_nome
                dados.append(linha)
        return dados
    
    def separar_nome_completo(self, nome_completo: str):
        partes = nome_completo.strip().split()
        if len(partes) == 0:
            return None, None, None  # Nome vazio
        elif len(partes) == 1:
            return partes[0], None, None  # Só primeiro nome
        elif len(partes) == 2:
            return partes[0], None, partes[1]  # Primeiro e último nome
        else:
            primeiro_nome = partes[0]
            ultimo_nome = partes[-1]
            nome_do_meio = " ".join(partes[1:-1])
            return primeiro_nome, nome_do_meio, ultimo_nome

    def cria_resume_candidato(self, dados_candidato: dict) -> str:
        nome_arquivo = f"resume_{dados_candidato.get('full_name').lower()}.txt"
        caminho_arquivo = os.path.join(pasta_saida, nome_arquivo)
        with open(caminho_arquivo, mode='w', encoding='utf-8') as arquivo:
            texto_resume = '\n'.join([
                dados_candidato.get("full_name", ""),
                dados_candidato.get("email", ""),
                dados_candidato.get("vacancy", "")
            ])
            arquivo.write(texto_resume)
        return caminho_arquivo

    def remove_arquivo_temporario(self):
        arquivos = os.listdir(pasta_saida)
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_saida, arquivo)
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)


if __name__ == "__main__":
    capturador = CapturadaDados("fonte/dados/entrada/banco.sql.csv")
    dados = capturador.ler_dados()
    for dado in dados:
        capturador.cria_resume_candidato(dado)
        print(dado)