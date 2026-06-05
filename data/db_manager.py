from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

import glob
import os

load_dotenv()

usuario = os.getenv("MONGO_INITDB_ROOT_USERNAME")
senha = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
banco = os.getenv("MONGO_INITDB_DATABASE")

URL = f"mongodb://{usuario}:{senha}@localhost:27017/"

client = MongoClient(URL)
db = client[banco]

def salva_log(
        data, 
        dia_semana, 
        horario, 
        total_iterations, 
        total_assertions, 
        total_failed_tests,
        total_skiped_tests):
    
    id = db.historico.count_documents({})

    log = {
        "_id": id,
        "data_execucao": data,
        "dia_semana": dia_semana,
        "horario": horario,
        "total_de_testes": (total_assertions + total_failed_tests + total_skiped_tests),
        "total_iterations": total_iterations,
        "total_assertions": total_assertions,
        "total_failed_tests": total_failed_tests,
        "total_skiped_tests": total_skiped_tests
    }

    db.historico.insert_one(log)

    print(f"Log de id: {id} salvo")
    client.close()
    
def get_info_relatorio(caminho_relatorio):
    
    with open(caminho_relatorio, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    data_hora_tag = soup.find("h5", class_="text-center")
    data_hora_texto = data_hora_tag.text.strip()

    partes = data_hora_texto.split(", ")
    dia_semana = partes[0]
    resto = partes[1]
    data = " ".join(resto.split(" ")[:3])
    horario = resto.split(" ")[3]

    cards = soup.find_all("h1", class_="display-1")

    total_iterations  = int(cards[0].text.strip())
    total_assertions  = int(cards[1].text.strip())
    total_failed      = int(cards[2].text.strip())
    total_skipped     = int(cards[3].text.strip())

    return (data, dia_semana, horario, total_iterations, total_assertions, total_failed, total_skipped)


if __name__ == "__main__":
    ARQUIVO_DE_CONTROLE = "ultimo_relatorio/ultimo_processado.txt"

    arquivos_html = glob.glob("ultimo_relatorio/*.html")

    if not arquivos_html:
        print("Nenhum relatório encontrado")
    else:
        caminho_atual = arquivos_html[0]
        nome_atual = os.path.basename(caminho_atual)

        try:
            with open(ARQUIVO_DE_CONTROLE, "r") as f:
                ultimo_processado = f.read().strip()
        except FileNotFoundError:
            ultimo_processado = ""

        if nome_atual == ultimo_processado:
            print(f"Relatório '{nome_atual}' já foi colocado no Banco de Dados.")
        else:
            data, dia_semana, horario, iterations, assertions, failed, skipped = get_info_relatorio(caminho_atual)

            salva_log(data, dia_semana, horario, iterations, assertions, failed, skipped)

            with open(ARQUIVO_DE_CONTROLE, "w") as f:
                f.write(nome_atual)
