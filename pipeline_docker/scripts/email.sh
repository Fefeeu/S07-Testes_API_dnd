#!/bin/bash
set -euo pipefail

STATUS="${1:-}"
BUILD_URL="${2:-}"
DESTINATARIO="${3:-}"

if [[ -z "$STATUS" || -z "$BUILD_URL" || -z "$DESTINATARIO" ]]; then
    echo "[ERRO] Uso: $0 <sucesso|falha> <build_url> <destinatario>"
    echo "       Exemplo: $0 sucesso http://localhost:8080/job/dnd-pipeline/1/ aluno@email.com"
    exit 1
fi

if [[ "$STATUS" != "sucesso" && "$STATUS" != "falha" ]]; then
    echo "[ERRO] Status deve ser 'sucesso' ou 'falha'. Recebido: '$STATUS'"
    exit 1
fi

# Lê o endereço do remetente salvo pelo docker_entry.sh
GMAIL_USER=$(cat /etc/gmail_user 2>/dev/null || echo "noreply@gmail.com")

# Data/hora em que o pipeline rodou
TIMESTAMP=$(date '+%d/%m/%Y às %H:%M:%S')

# Data/hora do commit - extraída pelo Jenkinsfile e passada como variável
COMMIT_TIMESTAMP="${COMMIT_TIMESTAMP:-N/A}"

# Informações do commit - injetadas pelo Jenkins ou pelo Jenkinsfile
COMMIT_AUTOR="${GIT_AUTHOR_NAME:-desconhecido}"
COMMIT_HASH="${GIT_COMMIT:-N/A}"
COMMIT_HASH_CURTO="${COMMIT_HASH:0:7}"

# Relatório
RELATORIO_URL="http://localhost:8081"
JOB_NAME="${JOB_NAME:-Pipeline DnD 5e}"
BUILD_NUMBER="${BUILD_NUMBER:-N/A}"

# Status individual dos testes Newman — passado pelo Jenkinsfile
NEWMAN_STATUS="${NEWMAN_STATUS:-N/A}"

if [[ "$STATUS" == "sucesso" ]]; then
    EMOJI="✅"
    ASSUNTO="[SUCESSO] DnD Pipeline — Build #${BUILD_NUMBER} concluído sem falhas"
    MENSAGEM_PRINCIPAL="Todos os endpoints da API foram validados com sucesso."
    DETALHES="A suíte completa de testes Newman foi executada e nenhuma requisição retornou erro."
else
    EMOJI="❌"
    ASSUNTO="[FALHA] DnD Pipeline — Build #${BUILD_NUMBER} encontrou problemas"
    MENSAGEM_PRINCIPAL="Um ou mais testes falharam durante a execução do pipeline."
    DETALHES="Revise os logs do Jenkins e o relatório HTML para identificar quais endpoints falharam."
fi

# Email que será enviado:
CORPO_EMAIL=$(cat <<EOF
From: DnD Pipeline <${GMAIL_USER}>
To: ${DESTINATARIO}
Subject: ${ASSUNTO}
Content-Type: text/plain; charset=UTF-8
MIME-Version: 1.0

${EMOJI} RESULTADO DO PIPELINE — ${JOB_NAME}
================================================

Status do build  : $(echo "$STATUS" | tr '[:lower:]' '[:upper:]')
Build            : #${BUILD_NUMBER}
Executado em     : ${TIMESTAMP}

INFORMAÇÕES DO COMMIT
---------------------
Autor            : ${COMMIT_AUTOR}
Hash             : ${COMMIT_HASH_CURTO}
Data do commit   : ${COMMIT_TIMESTAMP}

${MENSAGEM_PRINCIPAL}
${DETALHES}

RESULTADO DOS TESTES
--------------------
- Newman — DnD 5e API : ${NEWMAN_STATUS}

LINKS ÚTEIS
-----------
📋 Build no Jenkins      : ${BUILD_URL}
📊 Relatório HTML        : ${RELATORIO_URL}/api-report.html

--
Notificação automática — Pipeline de CI/CD DnD 5e API
EOF
)

# Mensagens de status do envio do email:
echo "[INFO] Enviando e-mail para '${DESTINATARIO}'..."

if echo "$CORPO_EMAIL" | msmtp --file=/etc/msmtp -a default "$DESTINATARIO"; then
    echo "[OK] E-mail enviado com sucesso para ${DESTINATARIO}"
    exit 0
else
    echo "[AVISO] Falha ao enviar e-mail. Verifique as credenciais do Gmail."
    echo "        O pipeline continuará normalmente."
    exit 0
fi