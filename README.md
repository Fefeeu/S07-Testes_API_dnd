# Projeto S07 - Automação de Testes de API (DevOps)

## 👥 Contribuição e Autores (Time)
O desenvolvimento técnico foi distribuído de forma igualitária entre todos os integrantes, o que pode ser verificado através do histórico de commits significativos no repositório:

- Pedro Henrique Ribeiro Dias

- Felipe Ferreira de Carvalho Gabriel Pereira

- Felipe Silva Loschi

- Guilherme Souza Emergente

## Sistema: Execução de Testes Automatizados da API de D&D (Dungeons & Dragons)

Este projeto tem como objetivo demonstrar a aplicação prática de conceitos modernos de DevOps, como a conteinerização utilizando **Docker**, automação de pipelines CI/CD com **Jenkins** (através de infraestrutura como código com `Jenkinsfile`) e a orquestração de múltiplos microsserviços usando **Docker Compose**.

A aplicação consiste em uma esteira automatizada que valida as requisições e regras da API pública de D&D através de coleções de testes desenvolvidas no Postman e executadas via CLI.

---

## 🚀 Instalação e Execução

### Pré-requisitos
* **Docker** instalado na máquina.
* Um servidor SMTP (como Gmail) configurado para o envio de notificações por e-mail.

### Configuração do Ambiente
Antes de subir os containers, configure as credenciais necessárias criando um arquivo `.env` na raiz do projeto (use o arquivo `.env.example` como referência):

### Como Executar
Para subir toda a infraestrutura de forma integrada, execute o seguinte comando no terminal:

```Coloca aqui os comandos```

## 🛠️ Funcionalidades e Arquitetura do Projeto
O ecossistema é composto por 4 containers trabalhando em conjunto para a orquestração do projeto:

```tabela aqui insira```

### Comunicação entre Containers & Volumes
- Comunicação: O container do Jenkins interage diretamente com o test-runner para disparar a execução da collection do Postman.
- 

- Volumes (Persistência): 

## 🔄 Pipeline CI/CD (Jenkinsfile)
O pipeline foi inteiramente construído utilizando Infraestrutura como Código (IaC). Nenhuma etapa foi configurada através da interface gráfica do Jenkins.

O fluxo de execução do Jenkinsfile segue estritamente as etapas obrigatórias:
- Checkout: Clonagem do repositório público do GitHub.
- Execução dos Testes: O executor roda a collection mapeada em Collections_postman/collection_postman.json através do Newman, exigindo uma cobertura de sucesso nos testes de $\ge90\%$.
- Build / Empacotamento: 
- Notificação: Disparo do script automatizado (pipeline_docker/scripts/email.sh) utilizando variáveis de ambiente injetadas, sem nenhuma credencial exposta no código (antipattern hardcoded).

# 🧠 Seção: Uso de Inteligência Artificial
Em conformidade com a transparência exigida na avaliação, documentamos abaixo os critérios de utilização de ferramentas de IA no desenvolvimento do projeto:

## 1. Modelos Utilizados


## 2. Escopo de Aplicação


## 3. Dinâmica de Trabalho


## 4. Prompts Utilizados (exemplo)

