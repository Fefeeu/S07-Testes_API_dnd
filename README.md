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
GMAIL_USER=seu-email@gmail.com
GMAIL_PASS=sua-senha-de-aplicativo
EMAIL_DESTINATARIO=destinatario@email.com
```

> ⚠️ Nunca commite o arquivo `.env` real. Ele está no `.gitignore`.

### Como Executar

```bash
execução
```

---

## 🛠️ Funcionalidades e Arquitetura

O ecossistema é composto por 5 containers trabalhando em conjunto:

| Container    | Papel                                      | Imagem         |
|--------------|--------------------------------------------|----------------|
| jenkins      | Orquestra o pipeline CI/CD                 | Dockerfile local |
| test-runner  | Executa os testes Newman da collection     | Docker Hub     |
| nginx        | Serve o relatório HTML gerado pelo Newman  | Docker Hub     |
| db           | Persiste o histórico de execuções          | Docker Hub     |
| mongo-express |  Visualização do mongodb | |

### Comunicação entre Containers

O container **jenkins** se comunica com o **test-runner** para disparar a
execução da collection. O **test-runner** salva o relatório HTML em um volume
compartilhado, que o **nginx** serve na porta 8081.

### Volumes (Persistência)

- `relatorios_volume` — compartilhado entre test-runner e nginx, persiste os
  relatórios HTML gerados pelo Newman
- `jenkins_home` — persiste as configurações, jobs e histórico do Jenkins
- `db_data` — persiste o histórico de execuções do banco de dados

---

## 🔄 Pipeline CI/CD (Jenkinsfile)

O pipeline foi inteiramente construído via Infraestrutura como Código (IaC).
Nenhuma etapa foi configurada pela interface gráfica do Jenkins.

Etapas do pipeline:

1. **Checkout** — clonagem do repositório público do GitHub
2. **Testes** — execução da collection via Newman com cobertura ≥ 90%
3. **Build/Empacotamento** — o relatório HTML e o resultado dos testes são
   arquivados como artefatos no Jenkins
4. **Notificação** — disparo do `script_email.sh` com status, autor do commit
   e links para os relatórios, usando variáveis de ambiente sem credenciais
   expostas no código

---

## 🔗 Links

- **Repositório GitHub:** (inserir link)
- **Imagem no Docker Hub:** (inserir link)

---

## 🧠 Uso de Inteligência Artificial

Em conformidade com a transparência exigida na avaliação, documentamos abaixo
o uso de ferramentas de IA no desenvolvimento do projeto.

### 1. Modelos Utilizados

- **Claude (Anthropic)** — utilizado como principal assistente ao longo do
  desenvolvimento

  Claude foi a escolha mais óbvia pela sua qualidade ao se tratar de problemas de programção, além da excelente feature de criação de pastas de projetos, onde são passadas instruções e dados sobre um projeto e diversos chats podem ser adicionados a este projeto, com todos seguindo as instruções previamente definidas.

### 2. Escopo de Aplicação

A IA foi utilizada nas seguintes frentes:

- Compreensão e explicação de conceitos de Docker, Dockerfile e Docker Compose
- Orientação na estruturação do pipeline Jenkins e escrita do Jenkinsfile
- Adaptação dos scripts de notificação por e-mail (`script_email.sh`,
  `docker-entrypoint.sh`, `msmtprc.template`) para o contexto do projeto
- Revisão e correção do Dockerfile do Jenkins
- Sugestões de boas práticas de versionamento e mensagens de commit
- Revisão deste README
- Escrita e revisão de códigos burocráticos tais como casc.yaml
- Explicação da estrutura de configuração automática do servidor Jenkins

### 3. Dinâmica de Trabalho

A IA foi utilizada de forma assistida — nenhum trecho foi copiado sem leitura
e compreensão prévia. O fluxo adotado foi: o integrante responável pela tarefa
consultava a IA para entender o conceito, recebia uma explicação, e então
implementava ou adaptava o código com base no entendimento adquirido.

A IA não substituiu decisões de arquitetura — essas foram tomadas pelo grupo
(como a escolha dos 4 containers e a divisão de responsabilidades entre eles).

### 4. Prompts Utilizados (exemplos reais)

### Exemplo 1: Contextualização do Projeto e Primeiros Passos

*Contexto do Projeto:*
*No projeto anterior, nosso grupo desenvolveu uma coleção de testes no Postman para a API oficial do D&D 5e (anexei o JSON dessa collection oficial na estrutura do projeto que criei utilizando a feature de projetos do claude, com instruções detalhadas de como me orientar a etender a resposta). Agora, para este novo projeto, precisamos seguir estritamente as diretrizes especificadas no documento "Projeto_S07_NP2.pdf", focando no desenvolvimento e na aplicação prática da infraestrutura DevOps. Durante a nossa conversa, vou pedir orientações sobre os conceitos de DevOps que estamos aplicando aqui.*

*Primeiro quero entender o Dockerfile do ambiente de testes (que no nosso caso será a base com o Jenkins). Depois disso, criarei o `Jenkinsfile` com as instruções corretas do pipeline.* 

*Vou te enviar o Dockerfile de exemplo que o professor disponibilizou. Quero entender detalhadamente o que significa cada instrução dele e como eu montaria essa estrutura do zero. Em seguida como devo estruturar o dockerfile do jenkins para nosso projeto*

> Resposta: Satisfatória, abordou linha por linha explicando a sintaxe do dockerfile, o que eu deveria manter para meu projeto e por que de cada utilização dos comandos listados. 

### Exemplo 2: Análise de Plugins e Estrutura do Entrypoint

*Antes de avançarmos para o desenvolvimento do script de e-mail e do `docker_entrypoint.sh`, preciso entender a fundo o ecossistema de plugins do Jenkins e a lógica de inicialização do container. Vou enviar a lista de plugins do projeto de exemplo do professor para avaliarmos o que realmente se aplica ao nosso escopo.*

*Quero entender:*
* *Quais desses plugins são estritamente necessários para o nosso projeto NP2, quais seriam úteis e o que cada um deles faz na prática.*
* *O que é o Docker Entrypoint, por que ele é necessário, como ele deve ser estruturado corretamente e qual é o papel do comando `exec "$@"` no final do script.*

> Resposta: satisfatória, abordou linha a linha os comandos e a estrutura correta de um arquivo docker_entrypoint.sh e por que ele deve ser criado e utilizado.

[Chat com Claude na parte do Newman](https://claude.ai/share/c8efc3ac-2684-4d0b-bb8c-6dddfac78478)

### 5. O que não foi feito por IA

- Definição da arquitetura dos 4 containers e seus papéis
- Escolha da API do D&D 5e como sistema a ser testado
- Escrita e organização da collection Postman
- Commits e versionamento do repositório
- Decisões sobre nomes de variáveis de ambiente e estrutura de pastas
- Mudanças feitas pós entendimento com a IA