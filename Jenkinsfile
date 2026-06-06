pipeline {
    agent any

    environment {
        DESTINATARIO = credentials('email-destinatario')
        REPORTS_DIR = 'newman_reports'
        DIST_DIR = 'dist'
        MONGO_INITDB_ROOT_USERNAME = credentials('mongo-user')
        MONGO_INITDB_ROOT_PASSWORD = credentials('mongo-pass')
        MONGO_INITDB_DATABASE = credentials('mongo-db')

    }

    stages {
        stage('Setup') {
            steps {
                echo 'Preparando o ambiente para execução...'
                // Garante que os diretórios de saída existam no workspace
                sh "mkdir -p ${REPORTS_DIR} ${DIST_DIR}"
            }
        }

        stage('Test (Run Postman Tests)') {
            steps {
                echo 'Iniciando os testes automatizados da API com Newman...'
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    // Roda o Newman apontando para a pasta correta da sua estrutura
                    // Cobertura >= 90% avaliada pelo sucesso das asserções da collection
                    sh """
                        newman run newman/collection_tests.json \
                            -e "newman/Environment dnd5e.postman_environment.json" \
                            --reporters cli,html \
                            --reporter-html-export ${REPORTS_DIR}/report_testes.html
                    """
                }
                sh "ls -la ${REPORTS_DIR}/"
            }
        }


        stage('Build & Package') {
            steps {
                echo 'Empacotando os artefatos do projeto (Requisito Obrigatório)...'
                // Cria um pacote (tar/zip) contendo as collections e scripts oficiais (Requisito: Pacote)
                sh """
                    tar -czf ${DIST_DIR}/projeto-dnd5e-api-bbuild.tar.gz \
                        Collection_official/ \
                        data/db_manager.py \
                        data/requirements.txt
                """
            }
        }

        stage('Save Log to Database') {
            steps {
                echo 'Registrando métricas e logs no banco de dados...'
                // Executa o script de banco passando as dependências de forma silenciosa
                // Nota: Idealmente seu Jenkins Agent deve possuir o python instalado via docker_entry.sh
                sh """
                    ls -la newman_reports/ || echo "Pasta newman_reports não existe"
                    pip install -r data/requirements.txt --break-system-packages -q
                    python3 data/db_manager.py
                """
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Arquivando o pacote e os relatórios no Jenkins (Requisito Obrigatório)...'
                // Salva o relatório de testes e o pacote gerado diretamente no Jenkins
                archiveArtifacts artifacts: "${REPORTS_DIR}/*.html, ${DIST_DIR}/*.tar.gz", 
                fingerprint: true, 
                allowEmptyArchive: false
            }
        }
    }

    post {
        success {
            script {
                def buildUrl = env.BUILD_URL ?: 'N/A'
                def reportPath = "${env.WORKSPACE}/${env.REPORTS_DIR}/report_testes.html"
                echo "Enviando e-mail de sucesso para o endereço configurado na env: ${env.DESTINATARIO}"
                sh "bash pipeline_docker/scripts/email.sh sucesso '${buildUrl}' '${env.DESTINATARIO}' '${reportPath}'"
            }
        }
        failure {
            script {
                def buildUrl = env.BUILD_URL ?: 'N/A'
                def reportPath = "${env.WORKSPACE}/${env.REPORTS_DIR}/report_testes.html"
                echo "Enviando e-mail de falha para o endereço configurado na env: ${env.DESTINATARIO}"
                sh "bash pipeline_docker/scripts/email.sh falha '${buildUrl}' '${env.DESTINATARIO}' '${reportPath}'"
            }
        }
    }
}
