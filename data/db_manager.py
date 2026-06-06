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

URL = f"mongodb://{usuario}:{senha}@db:27017/"

client = MongoClient(URL)
db = client[banco]

def salva_log(
        data,
        dia_semana,
        horario,
        total_iterations,
        total_assertions,
        total_failed_tests,
        total_skiped_tests,
        file_information,
        timings_and_data,
        summary):

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
        "total_skiped_tests": total_skiped_tests,
        "file_information": file_information,
        "timings_and_data": timings_and_data,
        "summary": summary
    }

    db.historico.insert_one(log)
    print(f"Log de id: {id} salvo")
    client.close()

def get_info_relatorio(caminho_arquivo):
    
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # data e hora
    data_hora_tag = soup.find("h5", class_="text-center")
    data_hora_texto = data_hora_tag.text.strip()
    partes = data_hora_texto.split(", ")
    dia_semana = partes[0]
    resto = partes[1]
    data = " ".join(resto.split(" ")[:3])
    horario = resto.split(" ")[3]

    # cards do sumário (iterations, assertions, failed, skipped)
    cards = soup.find_all("h1", class_="display-1")
    total_iterations  = int(cards[0].text.strip())
    total_assertions  = int(cards[1].text.strip())
    total_failed      = int(cards[2].text.strip())
    total_skipped     = int(cards[3].text.strip())

    # file information — busca todos os card-body e filtra pelo conteúdo
    file_information = {"collection": "", "environment": ""}
    timings_and_data = {"duracao_total": "", "dados_recebidos": "", "tempo_medio_resposta": ""}

    todos_card_body = soup.find_all("div", class_="card-body")

    for card in todos_card_body:
        texto = card.get_text()

        if "Collection:" in texto and "Environment:" in texto:
            for strong in card.find_all("strong"):
                label = strong.text.strip()
                valor = strong.next_sibling
                if valor:
                    valor = valor.strip()
                if "Collection:" in label:
                    file_information["collection"] = valor
                if "Environment:" in label:
                    file_information["environment"] = valor

        if "Total run duration:" in texto:
            for strong in card.find_all("strong"):
                label = strong.text.strip()
                valor = strong.next_sibling
                if valor:
                    valor = valor.strip()
                if "Total run duration:" in label:
                    timings_and_data["duracao_total"] = valor
                if "Total data received:" in label:
                    timings_and_data["dados_recebidos"] = valor
                if "Average response time:" in label:
                    timings_and_data["tempo_medio_resposta"] = valor

    # summary table
    tabela = soup.find("table")
    linhas = tabela.find_all("tr")[1:]

    summary = {}
    chaves = ["requests", "prerequest_scripts", "test_scripts", "assertions", "skipped_tests"]
    for i, linha in enumerate(linhas):
        colunas = linha.find_all("td")
        if len(colunas) >= 3 and i < len(chaves):
            summary[chaves[i]] = {
                "total": colunas[1].text.strip(),
                "failed": colunas[2].text.strip()
            }

    return (data, dia_semana, horario,
            total_iterations, total_assertions, total_failed, total_skipped,
            file_information, timings_and_data, summary)

if __name__ == "__main__":
    caminho_html = "newman_reports/report_testes.html"

    if not os.path.exists(caminho_html):
        print("Nenhum relatório encontrado")
    else:
        print(f"Processando relatório: {caminho_html}")
        
        (data, dia_semana, horario, iterations, assertions, failed, skipped, 
         file_information, timings_and_data, summary) = get_info_relatorio(caminho_html)

        salva_log(data, dia_semana, horario,
                iterations, assertions, failed, skipped,
                file_information, timings_and_data, summary)
