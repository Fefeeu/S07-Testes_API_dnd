# Projeto S07 - Automação de Testes de API (DevOps)

## 👥 Contribuição e Autores (Time)

O desenvolvimento técnico foi distribuído de forma igualitária entre todos os 
integrantes, o que pode ser verificado através do histórico de commits 
significativos no repositório:

- Pedro Henrique Ribeiro Dias
- Felipe Ferreira de Carvalho
- Gabriel Pereira
- Felipe Silva Loschi
- Guilherme Souza Emergente

## Sistema: Execução de Testes Automatizados da API de D&D

Este projeto demonstra a aplicação prática de conceitos modernos de DevOps:
conteinerização com **Docker**, automação de pipelines CI/CD com **Jenkins**
(via `Jenkinsfile`) e orquestração de múltiplos serviços com **Docker Compose**.

A aplicação consiste em uma esteira automatizada que valida endpoints da API
pública de D&D 5e através de coleções de testes desenvolvidas no Postman e
executadas via Newman (CLI).

---

## 🚀 Instalação e Execução

### Pré-requisitos

- **Docker** e **Docker Compose** instalados na máquina
- Conta Gmail com senha de aplicativo gerada para envio de notificações

### Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
JENKINS_ADM_USER=user_jenkins
JENKINS_ADM_PASSWORD=password_jenkins

GMAIL_USER=seu-email@gmail.com
GMAIL_PASS=sua-senha-de-aplicativo
EMAIL_DESTINATARIO=destinatario@email.com

MONGO_INITDB_ROOT_USERNAME=user_mongo
MONGO_INITDB_ROOT_PASSWORD=senha_mongo
MONGO_INITDB_DATABASE=db_de_testes
```

> ⚠️ Nunca commite o arquivo `.env` real. Ele está no `.gitignore`.

### Como Executar

```bash
docker compose -f docker-compose.yml up --build -d
```

---

## 🛠️ Funcionalidades e Arquitetura

O ecossistema é composto por 5 containers trabalhando em conjunto:

| Container     | Papel                                          | Imagem         |
|---------------|------------------------------------------------|----------------|
| jenkins       | Orquestra o pipeline CI/CD                     | Dockerfile local |
| newman        | Container auxiliar de testes Newman            | Dockerfile local |
| nginx         | Serve arquivos estáticos do projeto            | Dockerfile local |
| db            | Persiste o histórico de execuções (MongoDB)    | Docker Hub     |
| mongo-express | Visualização e administração do MongoDB        | Docker Hub     |

### Comunicação entre Containers

O container **jenkins** se comunica diretamente com o **db** (MongoDB) para
persistir os logs de execução do pipeline. O **mongo-express** também se
comunica com o **db** para exibir os dados via interface web na porta 8081.
Todos os containers estão na mesma rede Docker (`pipeline`).

### Volumes (Persistência)

- `db_data` — persiste os dados do MongoDB entre reinicializações do container

---

## 🔄 Pipeline CI/CD (Jenkinsfile)

O pipeline foi inteiramente construído via Infraestrutura como Código (IaC).
Nenhuma etapa foi configurada pela interface gráfica do Jenkins.

Etapas do pipeline:

1. **Checkout** — clonagem do repositório público do GitHub
2. **Setup** — criação dos diretórios de saída necessários
3. **Testes** — execução da collection via Newman com cobertura ≥ 90%
4. **Build/Empacotamento** — geração do pacote `.tar.gz` com os artefatos do projeto
5. **Save Log** — persistência das métricas de execução no MongoDB
6. **Archive Artifacts** — relatório HTML e pacote arquivados no Jenkins
7. **Notificação** — disparo do `email.sh` com status e link do build, usando variáveis de ambiente sem credenciais expostas no código

---

## 🔗 Link Docker Hub

- **Imagem no Docker Hub:** https://hub.docker.com/r/guilhermeguiko/server

---

## 🧠 Uso de Inteligência Artificial

Em conformidade com a transparência exigida na avaliação, documentamos abaixo
o uso de ferramentas de IA no desenvolvimento do projeto.

### 1. Modelos Utilizados

- **Claude (Anthropic)** — utilizado como principal assistente ao longo do
  desenvolvimento

### 2. Escopo de Aplicação

A IA foi utilizada nas seguintes frentes:

- Compreensão e explicação de conceitos de Docker, Dockerfile e Docker Compose
- Orientação na estruturação do pipeline Jenkins e escrita do Jenkinsfile
- Adaptação dos scripts de notificação por e-mail (`email.sh`, `docker_entry.sh`, `msmtp.template`) para o contexto do projeto
- Revisão e correção do Dockerfile do Jenkins
- Sugestões de boas práticas de versionamento e mensagens de commit
- Revisão deste README
- Escrita e revisão do `casc.yaml` para configuração automática do Jenkins
- Explicação da estrutura de configuração automática do servidor Jenkins via CasC

### 3. Dinâmica de Trabalho

A IA foi utilizada de forma assistida — nenhum trecho foi copiado sem leitura
e compreensão prévia. O fluxo adotado foi: o integrante responsável pela tarefa
consultava a IA para entender o conceito, recebia uma explicação, e então
implementava ou adaptava o código com base no entendimento adquirido.

A IA não substituiu decisões de arquitetura — essas foram tomadas pelo grupo
(como a escolha dos 5 containers e a divisão de responsabilidades entre eles).

### 4. Prompts Utilizados (exemplos reais)

### Exemplo 1: Contextualização do Projeto e Primeiros Passos

*Contexto do Projeto:*
*No projeto anterior, nosso grupo desenvolveu uma coleção de testes no Postman para a API oficial do D&D 5e. Agora, para este novo projeto, precisamos seguir estritamente as diretrizes especificadas no documento "Projeto_S07_NP2.pdf", focando no desenvolvimento e na aplicação prática da infraestrutura DevOps. Durante a nossa conversa, vou pedir orientações sobre os conceitos de DevOps que estamos aplicando aqui.*

*Primeiro quero entender o Dockerfile do ambiente de testes (que no nosso caso será a base com o Jenkins). Depois disso, criarei o `Jenkinsfile` com as instruções corretas do pipeline.*

*Vou te enviar o Dockerfile de exemplo que o professor disponibilizou. Quero entender detalhadamente o que significa cada instrução dele e como eu montaria essa estrutura do zero. Em seguida como devo estruturar o dockerfile do jenkins para nosso projeto*

> Resposta: Satisfatória, abordou linha por linha explicando a sintaxe do Dockerfile, o que eu deveria manter para meu projeto e por que de cada utilização dos comandos listados.

### Exemplo 2: Análise de Plugins e Estrutura do Entrypoint

*Antes de avançarmos para o desenvolvimento do script de e-mail e do `docker_entry.sh`, preciso entender a fundo o ecossistema de plugins do Jenkins e a lógica de inicialização do container. Vou enviar a lista de plugins do projeto de exemplo do professor para avaliarmos o que realmente se aplica ao nosso escopo.*

*Quero entender:*
- *Quais desses plugins são estritamente necessários para o nosso projeto NP2, quais seriam úteis e o que cada um deles faz na prática.*
- *O que é o Docker Entrypoint, por que ele é necessário, como ele deve ser estruturado corretamente e qual é o papel do comando `exec "$@"` no final do script.*

> Resposta: Satisfatória, abordou linha a linha os comandos e a estrutura correta de um arquivo `docker_entry.sh` e por que ele deve ser criado e utilizado.

### Exemplo 3: Depuração de Erros no Pipeline

*O pipeline está falhando com o erro `AccessDeniedException` ao tentar criar o workspace. O log mostra: `java.nio.file.AccessDeniedException: /var/jenkins_home/workspace/run-jenkinsfile@script`. Como resolvo esse problema no docker-compose?*

> Resposta: Satisfatória, identificou que o volume `.:/var/jenkins_home/workspace/projeto-s07` estava causando conflito de permissões e orientou a remoção do volume para que o Jenkins gerenciasse o workspace internamente.

### Exemplo 4: Chat com desenvolvimento do Newman

[Chat com Claude na parte do Newman](https://claude.ai/share/c8efc3ac-2684-4d0b-bb8c-6dddfac78478)

### 5. O que não foi feito com ajuda de IA

- Definição da arquitetura dos 5 containers e seus papéis
- Escolha da API do D&D 5e como sistema a ser testado
- Escrita e organização da collection Postman
- Commits e versionamento do repositório
- Decisões sobre nomes de variáveis de ambiente e estrutura de pastas
- Mudanças feitas pós entendimento com a IA
