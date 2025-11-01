from fonte.modulos.candidatos.capturada_dados import CapturadaDados
from fonte.modulos.orange_hrm.portal_orange import PortalOrangeHRM
from fonte.modulos.botcity.workshop_botcity import download_arquivo
from playwright.sync_api import sync_playwright
from fonte import logging, pasta_entrada
import os


if __name__ == "__main__":
    download_arquivo(url=os.environ.get("URL_ARQUIVO_CANDIDATOS"),
                     destination="banco.sql.csv")
    caminho_arquivo = os.path.join(pasta_entrada, "banco.sql.csv")
    capturador = CapturadaDados(caminho_arquivo)
    dados = capturador.ler_dados()
    if dados:
        with sync_playwright() as playwright:
            with PortalOrangeHRM(playwright) as portal:
                portal.login()
                for dado in dados:
                    logging.info(f"Iniciando cadastro do candidato: {dado.get('full_name')}")
                    arq_resume = capturador.cria_resume_candidato(dados_candidato=dado)
                    portal.cadastra_candidato(dados_candidato=dado, resume_candidato=arq_resume)
                capturador.remove_arquivo_temporario()
    else:
        logging.info("Nenhum dado encontrado para processar.")
