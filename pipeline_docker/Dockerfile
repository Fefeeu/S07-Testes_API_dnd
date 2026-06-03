FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    gnupg \
    lsb-release \
    gosu \
    msmtp \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) \
        signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
        https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" \
        > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -f docker && usermod -aG docker jenkins

# necessario criar um entrypoint pra função de notificação quando iniciar
COPY scripts/docker_entry.sh /usr/local/bin/docker_entry.sh
RUN chmod +x /usr/local/bin/docker_entry.sh

# adicionar no copy o caminho do plugin do jenkins
COPY jenkins/plugin.txt /usr/share/jenkins/ref/plugin.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugin.txt

# copia o arquivo de configuração casc.yaml para dentro da imagem
COPY jenkins/casc.yaml /var/jenkins_home/casc.yaml
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yaml

# COPY scripts/msmtprc.template /etc/msmtprc.template dando erro

EXPOSE 8080 50000

ENTRYPOINT ["/usr/local/bin/docker_entry.sh"]