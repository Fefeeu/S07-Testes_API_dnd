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

RUN npm install -g newman

RUN groupadd -f docker && usermod -aG docker jenkins

# necessario criar um entrypoint pra função de notificação quando iniciar
COPY scripts/docker_entry.sh /usr/local/bin/docker_entry.sh
RUN chmod +x /usr/local/bin/docker_entry.sh

# copiando o script de email.sh para a imagem
COPY scripts/email.sh /usr/local/bin/email.sh
RUN chmod +x /usr/local/bin/email.sh

# adicionar no copy o caminho do plugin do jenkins
COPY jenkins/plugin.txt /usr/share/jenkins/ref/plugin.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugin.txt

# cria a variavel de ambiente do casc.yaml com base no volume do docker compose
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc_configs/casc.yaml

# desliga a inicialização guiada
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

COPY scripts/msmtp.template /etc/msmtp.template

EXPOSE 8080 50000

ENTRYPOINT ["/usr/local/bin/docker_entry.sh"]