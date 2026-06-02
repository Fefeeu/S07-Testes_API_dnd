#!/bin/bash
set -e

echo "=========================================="
echo "  Pipeline DnD 5e API — Iniciando Jenkins"
echo "=========================================="

# garantindo que o diretório de relatórios existe com permissões corretas
mkdir -p /relatorios
chown jenkins:jenkins /relatorios
chmod 755 /relatorios
echo "[OK] Diretório /relatorios configurado."

# Ajusta permissão do socket Docker para o Jenkins conseguir executar comandos
if [[ -S /var/run/docker.sock ]]; then
    chmod 666 /var/run/docker.sock
    echo "[OK] Permissão do Docker socket ajustada."
else
    echo "[AVISO] Docker socket não encontrado em /var/run/docker.sock."
    echo "        Certifique-se de que o volume está montado no docker-compose.yml."
fi

# Gera o arquivo de configuração do msmtp substituindo os placeholders
# pelas variáveis de ambiente definidas no Docker Compose
if [[ -n "${GMAIL_USER:-}" && -n "${GMAIL_PASS:-}" ]]; then
    sed \
        -e "s/GMAIL_USER_PLACEHOLDER/${GMAIL_USER}/g" \
        -e "s/GMAIL_PASS_PLACEHOLDER/${GMAIL_PASS}/g" \
        /etc/msmtprc.template > /etc/msmtprc
    chmod 600 /etc/msmtprc
    chown jenkins:jenkins /etc/msmtprc
    echo "[OK] Configuração do msmtp gerada com sucesso."
else
    echo "[AVISO] GMAIL_USER ou GMAIL_PASS não definidos."
    echo "        O envio de e-mail não funcionará."
fi

echo "[INFO] Iniciando Jenkins como usuário jenkins..."
exec gosu jenkins /usr/bin/tini -- /usr/local/bin/jenkins.sh "$@"