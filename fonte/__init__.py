from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import logging
import os


load_dotenv()
pasta_projeto = Path(__file__).resolve().parents[1]
pasta_projeto = (pasta_projeto / "fonte")
pasta_entrada = pasta_projeto.joinpath(pasta_projeto, "dados", "entrada")
pasta_saida = pasta_projeto.joinpath(pasta_projeto, "dados", "saida")
pasta_logs = pasta_projeto.joinpath(pasta_projeto, "dados", "logs")
os.makedirs(pasta_entrada, exist_ok=True)
os.makedirs(pasta_saida, exist_ok=True)
os.makedirs(pasta_logs, exist_ok=True)
data_atual = datetime.now().strftime("%Y%m%d")
arquivo_log = pasta_logs / f"{data_atual}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=arquivo_log,
    encoding='utf-8'
)